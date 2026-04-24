from __future__ import annotations

import json
import re
import subprocess
from collections import OrderedDict
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

BASE_URL = "https://liaoxuefeng.com"
INDEX_PATH = "/books/python/introduction/index.html"
START_PATH = "/books/python/basic/index.html"
SOURCE_DIR_NAME = "liaoxuefeng-python-introduction-from-basic"
DISTILLED_JSON_NAME = "liaoxuefeng-python-introduction-from-basic.distilled.json"
DISTILLED_MD_NAME = "liaoxuefeng-python-introduction-from-basic.distilled.md"


def fetch_html(path: str) -> str:
    result = subprocess.run(
        [
            "curl",
            "-L",
            "-fsS",
            "-A",
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            BASE_URL + path,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def extract_chapter_urls(index_html: str) -> list[str]:
    matches = re.findall(r'href="(/books/python/[^"]+/index\.html)"', index_html)
    unique_matches = list(OrderedDict.fromkeys(matches))
    start = unique_matches.index(START_PATH)
    return unique_matches[start:]


def build_page_file_name(order: int, chapter_url: str) -> str:
    slug = chapter_url.strip("/").replace("/", "-").replace(".", "-")
    return f"{order:03d}-{slug}.json"


def extract_title(html: str) -> str:
    m = re.search(r"<div id=\"gsi-chapter-title\">\s*<h1>(.*?)</h1>", html, re.S)
    if not m:
        raise ValueError("failed to extract chapter title")
    return clean_inline_html(m.group(1))


def extract_content_html(html: str) -> str:
    patterns = [
        r'(?s)<div id="gsi-chapter-content">(.*?)</div>\s*<hr class="gsc-border">',
        r'(?s)<div id="gsi-chapter-content">(.*?)<div id="gsi-chapter-prev-next"',
    ]
    for pattern in patterns:
        m = re.search(pattern, html)
        if m:
            return m.group(1)
    raise ValueError("failed to extract chapter content")


def clean_inline_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


class ContentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.current_tag: str | None = None
        self.current_buffer: list[str] = []
        self.blocks: list[dict] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style", "svg"}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in {"h2", "h3", "h4", "p", "li", "pre"}:
            self.current_tag = tag
            self.current_buffer = []
        elif tag == "br" and self.current_tag in {"p", "li", "pre"}:
            self.current_buffer.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg"} and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if self.current_tag == tag:
            text = "".join(self.current_buffer)
            if self.current_tag == "pre":
                cleaned = unescape(text).strip()
            else:
                cleaned = clean_inline_html(text)
            if cleaned:
                self.blocks.append({"type": self.current_tag, "text": cleaned})
            self.current_tag = None
            self.current_buffer = []

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self.current_tag:
            self.current_buffer.append(data)


def parse_content(content_html: str) -> dict:
    parser = ContentParser()
    parser.feed(content_html)

    headings = [block["text"] for block in parser.blocks if block["type"] in {"h2", "h3", "h4"}]
    code_blocks = [block["text"] for block in parser.blocks if block["type"] == "pre"]
    text_blocks = [block for block in parser.blocks if block["type"] in {"p", "li"}]

    return {
        "blocks": parser.blocks,
        "headings": headings,
        "code_blocks": code_blocks,
        "text_block_count": len(text_blocks),
    }


def shorten_text(text: str, limit: int = 160) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def distill_chapter(page: dict) -> dict:
    blocks = page["blocks"]
    sections: list[dict] = []
    current = {"heading": "导读", "points": [], "code_examples": 0}

    for block in blocks:
        block_type = block["type"]
        text = block["text"]
        if block_type in {"h2", "h3", "h4"}:
            if current["points"] or current["code_examples"]:
                sections.append(current)
            current = {"heading": text, "points": [], "code_examples": 0}
            continue
        if block_type == "pre":
            current["code_examples"] += 1
            continue
        if block_type in {"p", "li"}:
            current["points"].append(text)

    if current["points"] or current["code_examples"]:
        sections.append(current)

    chapter_summary_parts: list[str] = []
    for section in sections:
        for point in section["points"]:
            if point:
                chapter_summary_parts.append(point)
            if len(chapter_summary_parts) >= 2:
                break
        if len(chapter_summary_parts) >= 2:
            break

    distilled_sections = []
    for section in sections:
        distilled_sections.append(
            {
                "heading": section["heading"],
                "summary": shorten_text(" ".join(section["points"][:2]), 220),
                "point_count": len(section["points"]),
                "code_examples": section["code_examples"],
            }
        )

    return {
        "order": page["order"],
        "url": page["url"],
        "title": page["title"],
        "section_slug": page["section_slug"],
        "section_title": page["section_title"],
        "chapter_summary": shorten_text(" ".join(chapter_summary_parts), 260),
        "headings": page["headings"],
        "code_block_count": len(page["code_blocks"]),
        "distilled_sections": distilled_sections,
    }


def build_markdown(distilled_pages: list[dict]) -> str:
    grouped: OrderedDict[str, list[dict]] = OrderedDict()
    for page in distilled_pages:
        grouped.setdefault(page["section_title"], []).append(page)

    lines = [
        "# 廖雪峰 Python 教程蒸馏",
        "",
        f"- 来源: {BASE_URL + INDEX_PATH}",
        "- 范围: 第五节 `Python基础` 到教程结尾",
        f"- 章节数: {len(distilled_pages)}",
        "",
    ]

    for section_title, pages in grouped.items():
        lines.append(f"## {section_title}")
        lines.append("")
        for page in pages:
            lines.append(f"### {page['order']:03d}. {page['title']}")
            lines.append(f"- URL: {BASE_URL + page['url']}")
            lines.append(f"- 摘要: {page['chapter_summary']}")
            lines.append(f"- 代码块数量: {page['code_block_count']}")
            for section in page["distilled_sections"][:6]:
                lines.append(f"- 小节 `{section['heading']}`: {section['summary']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def collect_pages() -> tuple[list[dict], dict]:
    index_html = fetch_html(INDEX_PATH)
    chapter_urls = extract_chapter_urls(index_html)
    pages: list[dict] = []
    current_section_slug = ""
    current_section_title = ""

    for order, chapter_url in enumerate(chapter_urls, start=1):
        html = fetch_html(chapter_url)
        title = extract_title(html)
        content_html = extract_content_html(html)
        parsed = parse_content(content_html)

        parts = chapter_url.strip("/").split("/")
        if len(parts) == 4:
            current_section_slug = parts[2]
            current_section_title = title

        page = {
            "order": order,
            "url": chapter_url,
            "title": title,
            "section_slug": current_section_slug,
            "section_title": current_section_title,
            "content_html": content_html,
            "blocks": parsed["blocks"],
            "headings": parsed["headings"],
            "code_blocks": parsed["code_blocks"],
            "text_block_count": parsed["text_block_count"],
        }
        pages.append(page)

    metadata = {
        "source_url": BASE_URL + INDEX_PATH,
        "start_path": START_PATH,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "chapter_count": len(pages),
    }
    return pages, metadata


def write_outputs(project_root: Path, pages: list[dict], metadata: dict) -> None:
    source_root = project_root / "source" / SOURCE_DIR_NAME
    pages_dir = source_root / "pages"
    tmp_root = project_root / "tmp" / "web"

    pages_dir.mkdir(parents=True, exist_ok=True)
    tmp_root.mkdir(parents=True, exist_ok=True)

    manifest = {
        **metadata,
        "pages_dir": str(pages_dir.relative_to(project_root)),
        "pages": [],
    }

    distilled_pages = []
    for page in pages:
        file_name = build_page_file_name(page["order"], page["url"])
        page_path = pages_dir / file_name
        page_path.write_text(
            json.dumps(page, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        manifest["pages"].append(
            {
                "order": page["order"],
                "title": page["title"],
                "url": BASE_URL + page["url"],
                "section_title": page["section_title"],
                "file": str(page_path.relative_to(project_root)),
            }
        )
        distilled_pages.append(distill_chapter(page))

    (source_root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    distilled_payload = {
        **metadata,
        "distilled_from": str((source_root / "manifest.json").relative_to(project_root)),
        "pages": distilled_pages,
    }
    (tmp_root / DISTILLED_JSON_NAME).write_text(
        json.dumps(distilled_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (tmp_root / DISTILLED_MD_NAME).write_text(
        build_markdown(distilled_pages),
        encoding="utf-8",
    )


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    pages, metadata = collect_pages()
    write_outputs(project_root, pages, metadata)


if __name__ == "__main__":
    main()

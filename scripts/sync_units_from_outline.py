from __future__ import annotations

import json
import re
from pathlib import Path


INDEX_FILES = ["unit.json", "refs.md"]
DEFAULT_SOURCE_REFS = [
    "source/《Python基础教程第3版》.pdf",
    "source/liaoxuefeng-python-introduction-from-basic/manifest.json",
    "tmp/pdfs/《Python基础教程第3版》.json",
]
DEFAULT_REFS_TEMPLATE = """# <大单元> / <小单元> 资料索引

> 这个目录只保存可选知识索引，不是当天任务输出目录。

- 固定大纲：`<outline-id>`
- 推荐资料：
<source-refs-bullets>
"""


def outline_id_to_unit_label(stable_id: str) -> str:
    return stable_id.removeprefix("outline-").replace("-", ".")


def sanitize_minor_title(title: str) -> str:
    value = title.strip()
    value = re.sub(r"[\\\\/:*?\"<>|]+", "-", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def build_unit_specs(outline_data: dict) -> list[dict]:
    specs: list[dict] = []

    def visit(node: dict, major_title: str, parent_node: dict | None) -> None:
        stable_id = node["stable_id"]
        specs.append(
            {
                "stable_id": stable_id,
                "fixed_outline_ref": stable_id,
                "major_unit": major_title,
                "minor_unit": node["title"],
                "minor_unit_dir": (
                    f"{outline_id_to_unit_label(stable_id)}-"
                    f"{sanitize_minor_title(node['title'])}"
                ),
                "parent_outline_ref": (
                    parent_node["stable_id"] if parent_node is not None else None
                ),
                "path_titles": node.get("path_titles", [major_title, node["title"]]),
                "prerequisites": node.get("prerequisites", []),
                "children_outline_ids": [
                    child["stable_id"] for child in node.get("children", [])
                ],
                "source_refs": DEFAULT_SOURCE_REFS,
                "index_files": INDEX_FILES,
            }
        )
        for child in node.get("children", []):
            visit(child, major_title=major_title, parent_node=node)

    for major_node in outline_data.get("outline", []):
        major_title = major_node["title"]
        for child in major_node.get("children", []):
            visit(child, major_title=major_title, parent_node=major_node)

    return specs


def build_unit_meta(spec: dict) -> dict:
    return {
        "stable_id": spec["stable_id"],
        "major_unit": spec["major_unit"],
        "minor_unit": spec["minor_unit"],
        "fixed_outline_ref": spec["fixed_outline_ref"],
        "parent_outline_ref": spec["parent_outline_ref"],
        "path_titles": spec["path_titles"],
        "prerequisites": spec["prerequisites"],
        "children_outline_ids": spec["children_outline_ids"],
        "source_refs": spec["source_refs"],
        "index_files": spec["index_files"],
    }


def render_bullets(items: list[str]) -> str:
    if not items:
        return "- （待补充）"
    return "\n".join(f"- `{item}`" for item in items)


def render_template(content: str, spec: dict) -> str:
    replacements = {
        "<大单元>": spec["major_unit"],
        "<小单元>": spec["minor_unit"],
        "<outline-id>": spec["fixed_outline_ref"],
        "outline-x-x": spec["fixed_outline_ref"],
        "大单元名": spec["major_unit"],
        "小单元名": spec["minor_unit"],
        "<source-refs-bullets>": render_bullets(spec["source_refs"]),
    }
    for source, target in replacements.items():
        content = content.replace(source, target)
    return content


def sync_units_from_outline(
    outline_path: Path, template_dir: Path, output_root: Path
) -> list[Path]:
    outline_data = json.loads(outline_path.read_text(encoding="utf-8"))
    specs = build_unit_specs(outline_data)
    created_paths: list[Path] = []

    output_root.mkdir(parents=True, exist_ok=True)

    for spec in specs:
        unit_dir = output_root / spec["major_unit"] / spec["minor_unit_dir"]
        unit_dir.mkdir(parents=True, exist_ok=True)
        created_paths.append(unit_dir)

        unit_meta_path = unit_dir / "unit.json"
        if not unit_meta_path.exists():
            unit_meta_path.write_text(
                json.dumps(build_unit_meta(spec), ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

        refs_path = unit_dir / "refs.md"
        if not refs_path.exists():
            template_path = template_dir / "refs.md"
            template_text = (
                template_path.read_text(encoding="utf-8")
                if template_path.exists()
                else DEFAULT_REFS_TEMPLATE
            )
            refs_path.write_text(
                render_template(template_text, spec),
                encoding="utf-8",
            )

    return created_paths


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    sync_units_from_outline(
        outline_path=project_root / "plan" / "outline.json",
        template_dir=project_root / "study" / "templates" / "unit",
        output_root=project_root / "study" / "units",
    )


if __name__ == "__main__":
    main()

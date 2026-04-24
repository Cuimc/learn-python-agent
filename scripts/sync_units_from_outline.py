from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


TEMPLATE_FILES = [
    "lesson.md",
    "practice.py",
    "answers.md",
    "notes.md",
    "mistakes.md",
]


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
                "task_mode": "mainline",
                "dynamic_reason": "根据固定大纲正常推进",
                "output_files": TEMPLATE_FILES,
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
        "task_mode": spec["task_mode"],
        "dynamic_reason": spec["dynamic_reason"],
        "output_files": spec["output_files"],
    }


def render_template(content: str, spec: dict) -> str:
    replacements = {
        "<大单元>": spec["major_unit"],
        "<小单元>": spec["minor_unit"],
        "<outline-id>": spec["fixed_outline_ref"],
        "outline-x-x": spec["fixed_outline_ref"],
        "大单元名": spec["major_unit"],
        "小单元名": spec["minor_unit"],
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

        for template_name in TEMPLATE_FILES:
            target_path = unit_dir / template_name
            if target_path.exists():
                continue
            template_path = template_dir / template_name
            content = template_path.read_text(encoding="utf-8")
            target_path.write_text(render_template(content, spec), encoding="utf-8")

        unit_meta_path = unit_dir / "unit.json"
        if not unit_meta_path.exists():
            unit_meta_path.write_text(
                json.dumps(build_unit_meta(spec), ensure_ascii=False, indent=2) + "\n",
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

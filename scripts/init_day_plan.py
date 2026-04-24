from __future__ import annotations

import json
from pathlib import Path
import shutil

DAY_CONTENT_FILES = [
    "lesson.md",
    "practice.py",
    "answers.md",
    "notes.md",
    "mistakes.md",
]


def render_units_bullets(units_for_today: list[dict]) -> str:
    lines = []
    for unit in units_for_today:
        lines.append(
            "- "
            f"{unit['major_unit']} / {unit['minor_unit']} "
            f"(`{unit['fixed_outline_ref']}` -> `{unit['unit_path']}`)"
        )
    return "\n".join(lines)


def render_day_plan(template_text: str, context: dict) -> str:
    day_plan = context["day_plan"]
    focus = context.get("focus", {})
    units_bullets = render_units_bullets(day_plan["units_for_today"])
    replacements = {
        "<day-id>": day_plan["current_day_id"],
        "<day-plan-path>": day_plan["current_day_plan_path"],
        "<theme>": focus.get("theme", ""),
        "<units-bullets>": units_bullets,
    }
    for source, target in replacements.items():
        template_text = template_text.replace(source, target)
    return template_text


def resolve_source_unit_path(study_root: Path, unit: dict) -> Path:
    return study_root.parent / unit["unit_path"]


def build_day_meta(context: dict) -> dict:
    day_plan = context["day_plan"]
    focus = context.get("focus", {})
    return {
        "day_id": day_plan["current_day_id"],
        "day_dir": day_plan["current_day_dir"],
        "plan_path": day_plan["current_day_plan_path"],
        "theme": focus.get("theme", ""),
        "source_units": day_plan["units_for_today"],
    }


def seed_day_file(day_dir: Path, file_name: str, template_dir: Path, context: dict, study_root: Path) -> None:
    target_path = day_dir / file_name
    if target_path.exists():
        return

    units_for_today = context["day_plan"]["units_for_today"]
    for unit in units_for_today:
        source_path = resolve_source_unit_path(study_root, unit) / file_name
        if source_path.exists():
            shutil.copyfile(source_path, target_path)
            return

    template_path = template_dir / file_name
    if template_path.exists():
        target_path.write_text(template_path.read_text(encoding="utf-8"), encoding="utf-8")


def init_study_day(study_root: Path, template_dir: Path, context_path: Path) -> Path:
    context = json.loads(context_path.read_text(encoding="utf-8"))
    day_plan = context["day_plan"]
    study_root.mkdir(parents=True, exist_ok=True)

    day_dir = study_root / day_plan["current_day_id"]
    day_dir.mkdir(parents=True, exist_ok=True)

    plan_path = day_dir / "plan.md"
    if not plan_path.exists():
        template_text = (template_dir / "plan.md").read_text(encoding="utf-8")
        plan_path.write_text(
            render_day_plan(template_text=template_text, context=context),
            encoding="utf-8",
        )

    for file_name in DAY_CONTENT_FILES:
        seed_day_file(
            day_dir=day_dir,
            file_name=file_name,
            template_dir=template_dir,
            context=context,
            study_root=study_root,
        )

    day_meta_path = day_dir / "day.json"
    if not day_meta_path.exists():
        day_meta_path.write_text(
            json.dumps(build_day_meta(context), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    return day_dir


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    init_study_day(
        study_root=project_root / "study",
        template_dir=project_root / "skills" / "templates" / "day",
        context_path=project_root / "state" / "current-context.json",
    )


if __name__ == "__main__":
    main()

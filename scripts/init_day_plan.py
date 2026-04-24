from __future__ import annotations

import json
from pathlib import Path


DAY_STUDY_FILES = [
    "lesson.md",
    "practice.py",
    "answers.md",
    "notes.md",
    "mistakes.md",
]

DEFAULT_PLAN_TEMPLATE = """# <day-id> 学习计划

> day-first workflow：计划写入 `plan/days/`，当天任务写入 `study/<day-id>/`。

## Day

- 编号：`<day-id>`
- 计划文件：`<day-plan-path>`
- 当天学习目录：`<day-study-dir>`
- 今日主题：<theme>

## 固定大纲引用

<outline-refs-bullets>

## 学习资料来源

<source-refs-bullets>

## 今日目标

- 先完成当天 lesson 的阅读和例子理解
- 运行并完成当天 `practice.py`
- 在 `notes.md` 和 `mistakes.md` 记录结果，供动态大纲回写

## 今日产出

- `plan/days/<day-id>.md`
- `study/<day-id>/lesson.md`
- `study/<day-id>/practice.py`
- `study/<day-id>/answers.md`
"""

DEFAULT_DAY_FILE_TEMPLATES = {
    "lesson.md": """# <day-id> lesson

> 当前 focus：<focus-title>
> 主题：<theme>

## 今日学习内容

- 待根据固定大纲、动态大纲和资料来源生成正式 lesson
""",
    "practice.py": '''"""<day-id> practice scaffold."""

from __future__ import annotations


def main() -> None:
    print("TODO: generate day-first practice tasks from outline and source refs")


if __name__ == "__main__":
    main()
''',
    "answers.md": """# <day-id> answers

> 对应当天 `practice.py` 的答案与讲解。

## 说明

- 待生成正式答案
- 解释为什么这样设计更好
- 记录常见误区与边界输入
""",
    "notes.md": """# <day-id> notes

## 今天确认的知识点

- 

## 还不稳定的地方

- 
""",
    "mistakes.md": """# <day-id> mistakes

## 错误记录

- 

## 下次需要补强的点

- 
""",
}


def render_bullets(items: list[str]) -> str:
    if not items:
        return "- （待补充）"
    return "\n".join(f"- `{item}`" for item in items)


def render_text(template_text: str, context: dict) -> str:
    current_day = context["current_day"]
    focus = context.get("current_focus", {})
    replacements = {
        "<day-id>": current_day["day_id"],
        "<day-plan-path>": current_day["plan_path"],
        "<day-study-dir>": context.get(
            "current_day_study_dir", current_day["study_dir"]
        ),
        "<theme>": focus.get("theme", ""),
        "<focus-title>": focus.get("title", ""),
        "<outline-refs-bullets>": render_bullets(context.get("outline_refs", [])),
        "<source-refs-bullets>": render_bullets(context.get("source_refs", [])),
    }
    for source, target in replacements.items():
        template_text = template_text.replace(source, target)
    return template_text


def render_day_plan(template_text: str, context: dict) -> str:
    return render_text(template_text=template_text, context=context)


def build_generated_files(context: dict) -> list[str]:
    current_day = context["current_day"]
    return [current_day["plan_path"]] + [
        f"{current_day['study_dir']}/{file_name}" for file_name in DAY_STUDY_FILES
    ] + [f"{current_day['study_dir']}/day.json"]


def build_day_meta(context: dict) -> dict:
    current_day = context["current_day"]
    return {
        "day_id": current_day["day_id"],
        "plan_path": current_day["plan_path"],
        "study_dir": current_day["study_dir"],
        "outline_refs": context.get("outline_refs", []),
        "source_refs": context.get("source_refs", []),
        "weak_points_used": context.get("weak_points_used", []),
        "generated_files": build_generated_files(context),
    }


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def init_day_plan(
    project_root: Path, context_path: Path, plan_template_path: Path
) -> dict[str, Path]:
    context = json.loads(context_path.read_text(encoding="utf-8"))
    current_day = context["current_day"]

    plan_path = project_root / current_day["plan_path"]
    study_dir = project_root / current_day["study_dir"]

    plan_path.parent.mkdir(parents=True, exist_ok=True)
    study_dir.mkdir(parents=True, exist_ok=True)

    template_text = (
        plan_template_path.read_text(encoding="utf-8")
        if plan_template_path.exists()
        else DEFAULT_PLAN_TEMPLATE
    )
    write_if_missing(plan_path, render_day_plan(template_text=template_text, context=context))

    for file_name in DAY_STUDY_FILES:
        write_if_missing(
            study_dir / file_name,
            render_text(DEFAULT_DAY_FILE_TEMPLATES[file_name], context),
        )

    write_if_missing(
        study_dir / "day.json",
        json.dumps(build_day_meta(context), ensure_ascii=False, indent=2) + "\n",
    )

    return {"plan_path": plan_path, "study_dir": study_dir}


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    init_day_plan(
        project_root=project_root,
        context_path=project_root / "state" / "current-context.json",
        plan_template_path=project_root / "skills" / "templates" / "day-plan-template.md",
    )


if __name__ == "__main__":
    main()

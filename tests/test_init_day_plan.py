import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


def load_module():
    module_path = Path("scripts/init_day_plan.py")
    spec = importlib.util.spec_from_file_location("init_day_plan", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def sample_context():
    return {
        "current_day": {
            "day_id": "day-001",
            "plan_path": "plan/days/day-001.md",
            "study_dir": "study/day-001",
        },
        "current_day_study_dir": "study/day-001",
        "current_focus": {
            "title": "Python基础 / 数据类型和变量",
            "theme": "数据类型、变量和最小 Python 表达",
            "task_mode": "mainline",
            "reason": "当前先建立 Python 基础数据表达能力，再推进到字符串和容器。",
        },
        "outline_refs": ["outline-5-1", "outline-5-2"],
        "source_refs": [
            "source/《Python基础教程第3版》.pdf",
            "source/liaoxuefeng-python-introduction-from-basic/manifest.json",
            "tmp/pdfs/《Python基础教程第3版》.json",
        ],
        "weak_points_used": ["bool 与 truthy/falsy 的差异"],
        "next_actions": [
            "阅读 plan/days/day-001.md",
            "学习 study/day-001/lesson.md",
            "运行 study/day-001/practice.py",
            "填写 study/day-001/notes.md 和 mistakes.md",
        ],
    }


class InitDayPlanTest(unittest.TestCase):
    def test_render_day_plan_replaces_day_source_and_outline_placeholders(self):
        module = load_module()
        template = "\n".join(
            [
                "# <day-id> 学习计划",
                "主题：<theme>",
                "今日目录：<day-study-dir>",
                "大纲引用：",
                "<outline-refs-bullets>",
                "资料来源：",
                "<source-refs-bullets>",
                "输出：<day-plan-path>",
            ]
        )

        rendered = module.render_day_plan(
            template_text=template,
            context=sample_context(),
        )

        self.assertIn("# day-001", rendered)
        self.assertIn("主题：数据类型、变量和最小 Python 表达", rendered)
        self.assertIn("今日目录：study/day-001", rendered)
        self.assertIn("- `outline-5-1`", rendered)
        self.assertIn("- `outline-5-2`", rendered)
        self.assertIn("- `source/《Python基础教程第3版》.pdf`", rendered)
        self.assertIn("plan/days/day-001.md", rendered)

    def test_init_day_plan_creates_day_first_outputs_without_copying_units(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            plan_template_path = root / "day-plan-template.md"
            plan_template_path.write_text(
                "# <day-id>\n主题：<theme>\n目录：<day-study-dir>\n<outline-refs-bullets>\n<source-refs-bullets>\n",
                encoding="utf-8",
            )

            source_unit_dir = (
                root / "study" / "units" / "Python基础" / "5.1-数据类型和变量"
            )
            source_unit_dir.mkdir(parents=True)
            (source_unit_dir / "lesson.md").write_text(
                "# source lesson\n",
                encoding="utf-8",
            )
            (source_unit_dir / "practice.py").write_text(
                "# source practice\n",
                encoding="utf-8",
            )
            (source_unit_dir / "answers.md").write_text(
                "# source answers\n",
                encoding="utf-8",
            )
            (source_unit_dir / "notes.md").write_text(
                "# source notes\n",
                encoding="utf-8",
            )
            (source_unit_dir / "mistakes.md").write_text(
                "# source mistakes\n",
                encoding="utf-8",
            )

            context_path = root / "current-context.json"
            context_path.write_text(
                json.dumps(sample_context(), ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            result = module.init_day_plan(
                project_root=root,
                context_path=context_path,
                plan_template_path=plan_template_path,
            )

            self.assertEqual(result["study_dir"].name, "day-001")
            self.assertTrue(result["plan_path"].exists())
            self.assertTrue((result["study_dir"] / "day.json").exists())
            self.assertTrue((result["study_dir"] / "lesson.md").exists())
            self.assertTrue((result["study_dir"] / "practice.py").exists())
            self.assertTrue((result["study_dir"] / "answers.md").exists())
            self.assertTrue((result["study_dir"] / "notes.md").exists())
            self.assertTrue((result["study_dir"] / "mistakes.md").exists())
            self.assertIn(
                "study/day-001",
                result["plan_path"].read_text(encoding="utf-8"),
            )
            self.assertNotEqual(
                (result["study_dir"] / "lesson.md").read_text(encoding="utf-8"),
                "# source lesson\n",
            )

            meta = json.loads((result["study_dir"] / "day.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["day_id"], "day-001")
            self.assertEqual(meta["plan_path"], "plan/days/day-001.md")
            self.assertEqual(meta["study_dir"], "study/day-001")
            self.assertEqual(meta["outline_refs"], ["outline-5-1", "outline-5-2"])
            self.assertEqual(meta["source_refs"][0], "source/《Python基础教程第3版》.pdf")
            self.assertEqual(meta["weak_points_used"], ["bool 与 truthy/falsy 的差异"])
            self.assertIn("study/day-001/practice.py", meta["generated_files"])
            self.assertEqual(
                (source_unit_dir / "lesson.md").read_text(encoding="utf-8"),
                "# source lesson\n",
            )
            self.assertEqual(
                (source_unit_dir / "practice.py").read_text(encoding="utf-8"),
                "# source practice\n",
            )

            result["plan_path"].write_text("manual plan\n", encoding="utf-8")
            second_result = module.init_day_plan(
                project_root=root,
                context_path=context_path,
                plan_template_path=plan_template_path,
            )

            self.assertEqual(second_result["plan_path"], result["plan_path"])
            self.assertEqual(
                result["plan_path"].read_text(encoding="utf-8"),
                "manual plan\n",
            )


if __name__ == "__main__":
    unittest.main()

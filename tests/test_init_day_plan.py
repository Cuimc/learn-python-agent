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
        "focus": {
            "theme": "数据类型、变量和最小 Python 表达",
        },
        "day_plan": {
            "current_day_id": "day1",
            "current_day_plan_path": "study/day1/plan.md",
            "current_day_dir": "study/day1",
            "units_for_today": [
                {
                    "major_unit": "Python基础",
                    "minor_unit": "5.1-数据类型和变量",
                    "fixed_outline_ref": "outline-5-1",
                    "unit_path": "study/units/Python基础/5.1-数据类型和变量/",
                },
                {
                    "major_unit": "函数",
                    "minor_unit": "6.1-调用函数",
                    "fixed_outline_ref": "outline-6-1",
                    "unit_path": "study/units/函数/6.1-调用函数/",
                },
            ],
        }
    }


class InitDayPlanTest(unittest.TestCase):
    def test_render_day_plan_replaces_day_and_unit_placeholders(self):
        module = load_module()
        template = "\n".join(
            [
                "# <day-id> 学习计划",
                "主题：<theme>",
                "今日单元：",
                "<units-bullets>",
                "输出：<day-plan-path>",
            ]
        )

        rendered = module.render_day_plan(
            template_text=template,
            context=sample_context(),
        )

        self.assertIn("# day1", rendered)
        self.assertIn("主题：数据类型、变量和最小 Python 表达", rendered)
        self.assertIn("- Python基础 / 5.1-数据类型和变量", rendered)
        self.assertIn("- 函数 / 6.1-调用函数", rendered)
        self.assertIn("study/day1/plan.md", rendered)

    def test_init_study_day_creates_day_package_and_preserves_existing_content(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            template_dir = root / "templates" / "day"
            template_dir.mkdir(parents=True)
            (template_dir / "plan.md").write_text(
                "# <day-id>\n主题：<theme>\n<units-bullets>\n",
                encoding="utf-8",
            )
            (template_dir / "lesson.md").write_text(
                "# day lesson template\n",
                encoding="utf-8",
            )
            (template_dir / "practice.py").write_text(
                "# day practice template\n",
                encoding="utf-8",
            )
            (template_dir / "answers.md").write_text(
                "# day answers template\n",
                encoding="utf-8",
            )
            (template_dir / "notes.md").write_text(
                "# day notes template\n",
                encoding="utf-8",
            )
            (template_dir / "mistakes.md").write_text(
                "# day mistakes template\n",
                encoding="utf-8",
            )
            (template_dir / "day.json").write_text(
                "{\"day_id\": \"<day-id>\", \"source_units\": []}\n",
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

            output_root = root / "study"
            output_path = module.init_study_day(
                study_root=output_root,
                template_dir=template_dir,
                context_path=context_path,
            )

            self.assertEqual(output_path.name, "day1")
            self.assertTrue(output_path.exists())
            self.assertTrue((output_path / "plan.md").exists())
            self.assertTrue((output_path / "day.json").exists())
            self.assertEqual(
                (output_path / "lesson.md").read_text(encoding="utf-8"),
                "# source lesson\n",
            )
            self.assertEqual(
                (output_path / "practice.py").read_text(encoding="utf-8"),
                "# source practice\n",
            )
            self.assertIn(
                "Python基础 / 5.1-数据类型和变量",
                (output_path / "plan.md").read_text(encoding="utf-8"),
            )
            meta = json.loads((output_path / "day.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["day_id"], "day1")
            self.assertEqual(meta["source_units"][0]["fixed_outline_ref"], "outline-5-1")

            (output_path / "plan.md").write_text("manual plan\n", encoding="utf-8")
            second_path = module.init_study_day(
                study_root=output_root,
                template_dir=template_dir,
                context_path=context_path,
            )

            self.assertEqual(second_path, output_path)
            self.assertEqual(
                (output_path / "plan.md").read_text(encoding="utf-8"),
                "manual plan\n",
            )


if __name__ == "__main__":
    unittest.main()

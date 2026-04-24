import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


def load_module():
    module_path = Path("scripts/sync_units_from_outline.py")
    spec = importlib.util.spec_from_file_location(
        "sync_units_from_outline", module_path
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def sample_outline():
    return {
        "outline": [
            {
                "title": "Python基础",
                "stable_id": "outline-5",
                "children": [
                    {
                        "title": "数据类型和变量",
                        "stable_id": "outline-5-1",
                        "children": [],
                        "prerequisites": [],
                        "path_titles": ["Python基础", "数据类型和变量"],
                    }
                ],
                "path_titles": ["Python基础"],
            },
            {
                "title": "函数式编程",
                "stable_id": "outline-8",
                "children": [
                    {
                        "title": "高阶函数",
                        "stable_id": "outline-8-1",
                        "children": [
                            {
                                "title": "map/reduce",
                                "stable_id": "outline-8-1-1",
                                "children": [],
                                "prerequisites": ["outline-6-1"],
                                "path_titles": [
                                    "函数式编程",
                                    "高阶函数",
                                    "map/reduce",
                                ],
                            }
                        ],
                        "prerequisites": ["outline-6"],
                        "path_titles": ["函数式编程", "高阶函数"],
                    }
                ],
                "path_titles": ["函数式编程"],
            },
        ]
    }


class SyncUnitsFromOutlineTest(unittest.TestCase):
    def test_build_unit_specs_flattens_outline_into_major_and_minor_units(self):
        module = load_module()

        specs = module.build_unit_specs(sample_outline())

        self.assertEqual(
            [spec["major_unit"] for spec in specs],
            ["Python基础", "函数式编程", "函数式编程"],
        )
        self.assertEqual(
            [spec["minor_unit_dir"] for spec in specs],
            ["5.1-数据类型和变量", "8.1-高阶函数", "8.1.1-map-reduce"],
        )
        self.assertEqual(specs[-1]["parent_outline_ref"], "outline-8-1")
        self.assertEqual(specs[-1]["prerequisites"], ["outline-6-1"])

    def test_sync_units_creates_scaffold_and_preserves_existing_files(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            outline_path = tmp_path / "outline.json"
            outline_path.write_text(
                json.dumps(sample_outline(), ensure_ascii=False, indent=2)
            )

            template_dir = tmp_path / "templates" / "unit"
            template_dir.mkdir(parents=True)
            (template_dir / "lesson.md").write_text("# lesson\n")
            (template_dir / "practice.py").write_text("# practice\n")
            (template_dir / "answers.md").write_text("# answers\n")
            (template_dir / "notes.md").write_text("# notes\n")
            (template_dir / "mistakes.md").write_text("# mistakes\n")
            (template_dir / "unit.json").write_text("{\"stable_id\": \"outline-x-x\"}\n")

            output_root = tmp_path / "study" / "units"
            module.sync_units_from_outline(
                outline_path=outline_path,
                template_dir=template_dir,
                output_root=output_root,
            )

            lesson_path = (
                output_root / "Python基础" / "5.1-数据类型和变量" / "lesson.md"
            )
            unit_meta_path = (
                output_root / "函数式编程" / "8.1.1-map-reduce" / "unit.json"
            )

            self.assertTrue(lesson_path.exists())
            self.assertTrue(unit_meta_path.exists())

            unit_meta = json.loads(unit_meta_path.read_text())
            self.assertEqual(unit_meta["fixed_outline_ref"], "outline-8-1-1")
            self.assertEqual(unit_meta["major_unit"], "函数式编程")
            self.assertEqual(unit_meta["minor_unit"], "map/reduce")

            lesson_path.write_text("manual notes\n")
            module.sync_units_from_outline(
                outline_path=outline_path,
                template_dir=template_dir,
                output_root=output_root,
            )

            self.assertEqual(lesson_path.read_text(), "manual notes\n")


if __name__ == "__main__":
    unittest.main()

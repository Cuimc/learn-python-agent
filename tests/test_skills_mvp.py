from __future__ import annotations

import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class SkillsMvpTest(unittest.TestCase):
    def test_only_core_intent_skills_remain(self):
        intent_files = sorted(
            path.name
            for path in (PROJECT_ROOT / "skills" / "intents").glob("*.md")
            if path.name != "README.md"
        )
        self.assertEqual(
            intent_files,
            [
                "explain_api.md",
                "generate_day.md",
                "review_day.md",
                "summarize_week.md",
            ],
        )

    def test_only_core_shared_rules_remain(self):
        shared_files = sorted(
            path.name
            for path in (PROJECT_ROOT / "skills" / "shared").glob("*.md")
            if path.name != "README.md"
        )
        self.assertEqual(
            shared_files,
            [
                "project-rules.md",
                "quality-check.md",
                "teaching-style.md",
            ],
        )

    def test_legacy_skill_files_are_moved_to_docs(self):
        legacy_names = [
            "learn-methods.lisp",
            "learn-plan.lisp",
            "project-init.md",
        ]
        for name in legacy_names:
            self.assertFalse((PROJECT_ROOT / "skills" / name).exists())
            self.assertTrue((PROJECT_ROOT / "docs" / "legacy-skills" / name).exists())

    def test_router_uses_generate_day_as_only_day_generation_entry(self):
        router_text = (PROJECT_ROOT / "router" / "intents.yaml").read_text(
            encoding="utf-8"
        )
        self.assertIn("generate_day:", router_text)
        self.assertIn("skill_path: skills/intents/generate_day.md", router_text)
        self.assertNotIn("generate_next_task:", router_text)
        self.assertNotIn("generate_exercises:", router_text)
        self.assertNotIn("harder_exercises:", router_text)
        self.assertNotIn("review_session_result:", router_text)
        self.assertNotIn("next_week_plan:", router_text)
        self.assertIn("forbidden_outputs:", router_text)
        self.assertIn("- study/units/**", router_text)
        self.assertIn("primary: plan/days/<day-id>.md", router_text)
        self.assertIn("- study/<day-id>/practice.py", router_text)

    def test_skills_readme_mentions_four_core_intents_and_units_as_index(self):
        readme_text = (PROJECT_ROOT / "skills" / "README.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("4 个核心 intent", readme_text)
        self.assertIn("generate_day", readme_text)
        self.assertIn("review_day", readme_text)
        self.assertIn("study/units", readme_text)
        self.assertIn("索引", readme_text)

    def test_templates_reference_day_first_outputs(self):
        template_text = (
            PROJECT_ROOT / "skills" / "templates" / "day-plan-template.md"
        ).read_text(encoding="utf-8")
        self.assertIn("plan/days/<day-id>.md", template_text)
        self.assertIn("study/<day-id>/lesson.md", template_text)
        self.assertNotIn("对应 unit 下的", template_text)

        week_template_text = (
            PROJECT_ROOT / "skills" / "templates" / "week-plan-template.md"
        ).read_text(encoding="utf-8")
        self.assertIn("plan/days/<day-id>.md", week_template_text)
        self.assertIn("study/<day-id>/", week_template_text)
        self.assertNotIn("study/units", week_template_text)


if __name__ == "__main__":
    unittest.main()

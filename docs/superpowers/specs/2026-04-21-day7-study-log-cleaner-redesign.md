# Day 7 Study Log Cleaner Redesign

## Goal

Rebuild `study/week3/day7/` so it matches the new lesson standard and presents Day 7 as a real Week 3 integration project instead of a short outline.

## Scope

Files to rebuild:

- `study/week3/day7/lesson.md`
- `study/week3/day7/main.py`
- `study/week3/day7/file_utils.py`
- `study/week3/day7/data/raw_log.txt`
- `study/week3/day7/data/cleaned_log.txt`
- `study/week3/day7/data/report.json`

## Chosen Direction

Treat Day 7 as a project day:

- `lesson.md` explains how the week’s topics connect into one runnable script.
- `main.py` keeps only orchestration logic.
- `file_utils.py` keeps reusable processing helpers.
- `data/` contains one intentionally messy input file plus generated outputs that match the lesson.

## Content Rules

- Keep the outline-style lesson headings used in Week 3.
- Expand each key section with concrete explanation and examples.
- Add one connected example that shows input -> clean -> report -> save -> self-check.
- Explicitly explain why Day 7 now moves from “single skill” to “small project”.

## Project Rules

- Use only Week 3 knowledge: files, text cleaning, JSON, exceptions, `Path`, multi-file split.
- Keep the code beginner-readable.
- Keep output messages explicit and easy to compare with the lesson text.
- Keep self-check minimal: prove the cleaned result is not empty.

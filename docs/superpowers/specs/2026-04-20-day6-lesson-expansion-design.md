# Day 6 Lesson Expansion Design

## Goal

Expand `study/week3/day6/lesson.md` from a short outline into a beginner-friendly lesson note while preserving the existing study-note structure used in adjacent days.

## Constraints

- Keep the existing major headings so Day 6 still matches the surrounding Week 3 notes.
- Write for a beginner audience.
- Add concrete Python examples rather than abstract explanations.
- Keep the scope focused on `pathlib.Path` and a first step toward splitting logic into `file_utils.py`.

## Chosen Approach

Use a hybrid structure:

- Preserve the current outline sections.
- Add short tutorial-style explanation blocks under each section.
- Add code examples directly where concepts are introduced.
- Add a small "common mistakes" section for the most likely beginner confusions.

## Content Additions

### 1. Why paths should become objects

Explain why raw string paths are fragile:

- easy to mistype separators
- harder to inspect filename/suffix/parent directory
- mixing path building and path checking becomes messy

### 2. Parameter-level explanation

Expand each item:

- `Path("data") / "file.txt"`
- `path.exists()`
- `path.name`
- `path.suffix`

Each item gets:

- what it means
- what it returns
- one minimal example

### 3. JS / TS bridge

Clarify:

- `path.join()` is mainly for composing path strings
- `existsSync()` checks existence
- `pathlib` wraps composition and inspection on one object

### 4. Day task walkthrough

Turn the task list into a connected example showing:

- creating a `Path` object for the data directory
- creating the directory if needed
- preparing file paths
- checking existence and printing metadata
- moving repeated text helpers into `file_utils.py`

### 5. Common mistakes

Cover likely beginner mistakes:

- treating `Path` exactly like a plain string everywhere
- confusing `/` in `Path` composition with division
- assuming `suffix` returns all suffixes
- assuming `exists()` distinguishes files from directories

## Non-Goals

- No advanced `pathlib` APIs beyond what Day 6 introduces.
- No full packaging or module architecture lesson.
- No refactor of other lesson files.

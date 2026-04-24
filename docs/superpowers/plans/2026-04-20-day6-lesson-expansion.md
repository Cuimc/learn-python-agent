# Day 6 Lesson Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the Day 6 lesson into a beginner-friendly note with detailed explanations, examples, and common pitfalls while preserving the existing outline structure.

**Architecture:** Keep the existing Markdown headings in `study/week3/day6/lesson.md`, then enrich each section with concise explanations and runnable examples. Store the approved design and this plan in `docs/superpowers/` so the reasoning and execution record stay separate from the study note itself.

**Tech Stack:** Markdown, existing study note structure, Python code examples

---

### Task 1: Record the approved design

**Files:**
- Create: `docs/superpowers/specs/2026-04-20-day6-lesson-expansion-design.md`

- [ ] **Step 1: Write the design summary**

```markdown
# Day 6 Lesson Expansion Design

## Goal

Expand `study/week3/day6/lesson.md` from a short outline into a beginner-friendly lesson note while preserving the existing study-note structure used in adjacent days.
```

- [ ] **Step 2: Save the chosen content additions**

```markdown
## Content Additions

### 1. Why paths should become objects
### 2. Parameter-level explanation
### 3. JS / TS bridge
### 4. Day task walkthrough
### 5. Common mistakes
```

### Task 2: Record the execution plan

**Files:**
- Create: `docs/superpowers/plans/2026-04-20-day6-lesson-expansion.md`

- [ ] **Step 1: Write the plan header**

```markdown
# Day 6 Lesson Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
```

- [ ] **Step 2: List the concrete edit target**

```markdown
### Task 3: Expand the lesson content

**Files:**
- Modify: `study/week3/day6/lesson.md`
```

### Task 3: Expand the lesson content

**Files:**
- Modify: `study/week3/day6/lesson.md`

- [ ] **Step 1: Replace the short outline-only sections with enriched explanations**

````markdown
## 今天只学什么

`pathlib.Path`、多文件拆分

以前我们经常把路径当成普通字符串来写，比如 `"data/file.txt"`。
Day 6 要开始建立一个更稳的习惯：把路径当成对象处理。
````

- [ ] **Step 2: Add parameter-level examples**

````markdown
### 1）`Path("data") / "file.txt"`

```python
from pathlib import Path

file_path = Path("data") / "file.txt"
print(file_path)
```
````

- [ ] **Step 3: Add the JS / TS comparison explanation**

````markdown
## JS / TS 桥接

如果你有 JS / TS 背景，可以把它理解成：

- `path.join("data", "file.txt")`
- 再配合 `existsSync("data/file.txt")`
````

- [ ] **Step 4: Add one connected workflow example and common mistakes**

````markdown
## 一个连起来的小例子

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
```
````

- [ ] **Step 5: Review the final Markdown for clarity**

Run: `sed -n '1,260p' study/week3/day6/lesson.md`
Expected: the lesson keeps its original section order and now includes explanations, examples, and a common-mistakes section

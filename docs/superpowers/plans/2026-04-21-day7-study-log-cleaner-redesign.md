# Day 7 Study Log Cleaner Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the Day 7 lesson and project files so the day works as a coherent Week 3 mini-project under the new lesson standard.

**Architecture:** Keep `lesson.md` as the teaching document, keep `main.py` as the orchestration entrypoint, keep `file_utils.py` as the reusable helper module, and make the `data/` files match the actual project flow. The lesson and project outputs should describe the same pipeline and the script should regenerate the output files cleanly.

**Tech Stack:** Markdown, Python 3 standard library (`pathlib`, `json`)

---

### Task 1: Rewrite the teaching document

**Files:**
- Modify: `study/week3/day7/lesson.md`

- [ ] **Step 1: Replace the short outline with the new standard lesson structure**

```markdown
## 今天只学什么

不再学单个新语法，而是把这周的文件读写、文本清洗、JSON、异常、路径、多文件拆分串成一个最小项目。
```

- [ ] **Step 2: Add parameter-level explanations**

```markdown
### 1）`BASE_DIR = Path(__file__).resolve().parent`
### 2）`clean_lines(raw_lines)`
### 3）`build_report(RAW_LOG_PATH, raw_lines, cleaned_lines)`
### 4）`run_self_check(report)`
```

- [ ] **Step 3: Add one connected workflow example**

```markdown
## 一个连起来的小例子

raw_lines = read_lines(RAW_LOG_PATH)
cleaned_lines = clean_lines(raw_lines)
report = build_report(RAW_LOG_PATH, raw_lines, cleaned_lines)
```

### Task 2: Rebuild the project code

**Files:**
- Modify: `study/week3/day7/main.py`
- Modify: `study/week3/day7/file_utils.py`

- [ ] **Step 1: Keep `main.py` focused on input -> process -> output -> self-check**

```python
def main():
    raw_lines = read_lines(RAW_LOG_PATH)
    cleaned_lines = clean_lines(raw_lines)
    report = build_report(RAW_LOG_PATH, raw_lines, cleaned_lines)
```

- [ ] **Step 2: Keep `file_utils.py` focused on reusable helpers**

```python
def clean_lines(lines):
    ...

def build_report(input_path, raw_lines, cleaned_lines):
    ...
```

### Task 3: Rebuild the sample data and verify outputs

**Files:**
- Modify: `study/week3/day7/data/raw_log.txt`
- Modify: `study/week3/day7/data/cleaned_log.txt`
- Modify: `study/week3/day7/data/report.json`

- [ ] **Step 1: Create a messy raw log with blanks and mixed casing**

```text
  learn Python file io

clean text lines
```

- [ ] **Step 2: Run the project**

Run: `python3 study/week3/day7/main.py`
Expected: prints summary lines and writes `cleaned_log.txt` plus `report.json`

- [ ] **Step 3: Re-read generated outputs**

Run: `sed -n '1,220p' study/week3/day7/data/cleaned_log.txt` and `sed -n '1,220p' study/week3/day7/data/report.json`
Expected: output content matches the raw log after cleaning and report counting

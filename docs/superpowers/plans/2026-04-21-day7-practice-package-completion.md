# Day 7 Practice Package Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the missing Day 7 exercise file and wire it into the lesson so the package includes both teaching and practice.

**Architecture:** Keep `lesson.md` as the teaching note and add a separate `practice.py` that imports the existing Day 7 helpers. The practice file should mirror the Day 7 project flow, not introduce unrelated drills.

**Tech Stack:** Markdown, Python 3 standard library, existing `study/week3/day7/file_utils.py`

---

### Task 1: Add the exercise file

**Files:**
- Create: `study/week3/day7/practice.py`

- [ ] **Step 1: Add header and example area**

```python
# Day 7 练习文件：study_log_cleaner
# 运行方式：python3 practice.py
```

- [ ] **Step 2: Add three exercise types**

```python
# 练习 1：热身
# 练习 2：动手实现
# 练习 3：找 bug / 解释原因
```

### Task 2: Link the lesson to the practice file

**Files:**
- Modify: `study/week3/day7/lesson.md`

- [ ] **Step 1: Add a short practice entry**

```markdown
完成项目主流程后，再去做同目录下的 `practice.py`。
```

### Task 3: Verify package state

**Files:**
- Create: `study/week3/day7/practice.py`
- Modify: `study/week3/day7/lesson.md`

- [ ] **Step 1: Run the practice file**

Run: `python3 study/week3/day7/practice.py`
Expected: the example area prints results and the file runs without syntax errors

- [ ] **Step 2: Confirm package files exist**

Run: `python3 -c "from pathlib import Path; print((Path('study/week3/day7') / 'practice.py').exists())"`
Expected: `True`

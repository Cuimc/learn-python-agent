# Lesson Generation Style Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Encode the Day 6 lesson-writing style into the reusable learning-rule files so future generated lessons follow the same structure and depth.

**Architecture:** Update the planning file with explicit lesson structure and quality rules, then update the teaching file with expansion rules that turn an outline into a beginner-friendly lesson. Verify the new rules exist in both files and that both Lisp files still load cleanly.

**Tech Stack:** Emacs Lisp, Markdown, shell verification with `rg` and `emacs --batch`

---

### Task 1: Update planning-layer rules

**Files:**
- Modify: `skills/learn-plan.lisp`

- [ ] **Step 1: Add an outline-style lesson rule block**

```lisp
(defconst 学习计划/提纲式lesson规则
  '((默认章节 . ("今天只学什么" "来源绑定" "今天目标" "参数级重点" "JS / TS 桥接" "今天任务" "今日最小结论" "理解检查"))))
```

- [ ] **Step 2: Add quality constraints that force explanation depth**

```lisp
"参数级重点不能只列 API 名称；每个重点至少讲清：它是什么、效果或返回值、最小示例、常见用途"
```

### Task 2: Update teaching-layer rules

**Files:**
- Modify: `skills/learn-methods.lisp`

- [ ] **Step 1: Add outline-expansion teaching rules**

```lisp
(defun 引擎/提纲式lesson展开规则 ()
  '("保留提纲结构，但每一节都要补解释和例子"))
```

- [ ] **Step 2: Require connected examples and transition explanations**

```lisp
"如果今天任务之间本来就是一条小流程，必须补一个“连起来的小例子”"
"如果当天引入拆文件、工程化、对象化等新习惯，必须解释为什么现在开始这样做"
```

### Task 3: Verify rule presence and file validity

**Files:**
- Modify: `skills/learn-plan.lisp`
- Modify: `skills/learn-methods.lisp`

- [ ] **Step 1: Run rule-presence checks**

Run: `rg -n "参数级重点不能只列 API 名称|一个连起来的小例子|保留提纲结构，但每一节都要补解释和例子" skills/learn-plan.lisp skills/learn-methods.lisp`
Expected: matching lines from both files

- [ ] **Step 2: Run a syntax load**

Run: `emacs --batch -Q -l skills/learn-plan.lisp -l skills/learn-methods.lisp`
Expected: exit code 0

# Quality Check

> 共享质量检查：生成 day、review day、周总结前后都要过一遍。

## 知识边界检查

1. 先读取本次计划中的主题、任务和显式知识点
2. 列出本次允许出现的语法点、API、内置函数、方法、模块
3. 对照已学知识和本次计划知识，扫描 lesson、practice、answers 中的调用
4. 发现超纲内容时，先补最小知识块，再继续正式生成

## lesson / practice 质量

- lesson 必须有知识解释、最小示例、真实用法和常见误区
- `practice.py` 必须可运行，不能退化成纯文字题单
- `answers.md` 不能只给结果，要解释为什么这样设计
- 如果当天内容只剩一个过窄知识点或 1 到 2 个过于简单的任务，视为不合格

## review 质量

- `notes.md` 和 `mistakes.md` 至少要能支撑下一次 `review_day`
- 回写状态时，要明确本次是 `good`、`mixed` 还是 `poor`
- 复盘结果只能影响后续 `plan/days/` 和 `study/<day-id>/`，不要回写 unit 内容

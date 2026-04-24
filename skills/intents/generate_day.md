# generate_day

> day-first workflow 的唯一日任务生成入口。

## 输入顺序

严格按下面顺序组织上下文：

1. 读取 `source/` 和 `tmp/pdfs/`，锁定当天资料来源
2. 读取 `plan/outline.json`，确认固定大纲当前位置和相邻可推进节点
3. 读取 `state/dynamic-outline.json` 与 `state/weak-points.json`，判断本次是 `mainline`、`reinforcement` 还是 `fallback`
4. 读取 `state/current-context.json`，确认当前 `day_id`、`focus`、`outline_refs`、`source_refs` 和输出目录

## 输出目录

- 计划只写入 `plan/days/<day-id>.md`
- 当天学习包只写入 `study/<day-id>/`
- 标准产物：
  - `study/<day-id>/lesson.md`
  - `study/<day-id>/practice.py`
  - `study/<day-id>/answers.md`
  - `study/<day-id>/notes.md`
  - `study/<day-id>/mistakes.md`
  - `study/<day-id>/day.json`

## 禁止项

- 不要生成或修改 `study/units/**/lesson.md`
- 不要生成或修改 `study/units/**/practice.py`
- 不要生成或修改 `study/units/**/answers.md`
- 不要生成或修改 `study/units/**/notes.md`
- 不要生成或修改 `study/units/**/mistakes.md`

## lesson 规则

- 面向“有编程基础的前端开发者”
- 写成教程正文，不要写成提示清单
- 默认覆盖 `2-4` 个强相关知识点，不要只围绕一个过窄知识点展开
- 至少包含：
  - `1` 个核心概念点
  - `1` 个接口 / 参数 / 数据结构设计点
  - `1` 个真实脚本组织或使用点

## practice 规则

- `practice.py` 必须是可运行文件
- 默认至少提供 `5` 组任务
- 必须覆盖：
  - `2` 个实现题
  - `1` 个边界输入题
  - `1` 个改错 / 重构题
  - `1` 个主流程整合题

## extra_practice 规则

这是原 `harder_exercises` 的子模式，只能作为 `generate_day` 内部增强，不是独立主流程入口。

- 当 `state/weak-points.json` 或动态大纲显示当前主题不稳时启用
- 增加工程场景、调试要求、异常处理或输入复杂度
- 难度提升不能只靠增加题量

## 结果要求

- 解释“为什么这次任务这样安排”
- `day.json` 中写清 `outline_refs`、`source_refs`、`weak_points_used`
- 如需更新 `state/current-context.json`，只更新 day-first 所需字段

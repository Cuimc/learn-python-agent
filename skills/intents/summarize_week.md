# summarize_week

> 汇总一周学习成果，并顺手产出下一周的最小可执行安排。

## 输入检查

- 读取 `state/dynamic-outline.json`
- 读取 `state/learning-progress.json`
- 读取 `state/weak-points.json`
- 回看 `plan/days/`
- 回看本周已完成的 `study/<day-id>/`
- 必要时参考 `source/` 和 `tmp/pdfs/`

## 输出要求

- 汇总本周完成内容、重复错误模式和当前掌握情况
- 明确哪些固定大纲节点已稳定，哪些还需要补强
- 给出下一周的最小推进建议
- 如果需要生成周计划，统一落到 `plan/` 与 `plan/days/`
- 更新：
  - `state/current-context.json`
  - `state/dynamic-outline.json`
  - `state/learning-progress.json`

## day-first 约束

- 周级建议应指向后续 `plan/days/<day-id>.md` 和 `study/<day-id>/`
- 不要把下周任务写入 `study/units/**`

# review_day

> 根据一天的学习结果回写状态，并决定下一次是推进还是补强。

## 输入检查

- 读取 `state/dynamic-outline.json`
- 读取 `state/weak-points.json`
- 读取 `state/current-context.json`
- 回看 `plan/days/<day-id>.md`
- 回看 `study/<day-id>/notes.md` 和 `study/<day-id>/mistakes.md`

## 输出要求

- 判断本次结果属于 `good`、`mixed`、`poor` 中哪一类
- 更新动态大纲中的节点状态、掌握度和补强动作
- 更新薄弱点计数和严重度
- 同步更新 `state/current-context.json`，明确下一次 focus、outline_refs、source_refs 和输出目录
- 必要时更新 `study/<day-id>/day.json` 中的完成状态
- 同步更新 `plan/current-outline.md` 的可读摘要

## 禁止项

- 不要把复盘或补强结果写回 `study/units/**`
- 不要为复盘单独生成新的 unit 内容文件

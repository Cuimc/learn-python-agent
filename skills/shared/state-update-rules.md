# State Update Rules

> 共享规则：生成学习内容后，按需更新 `state/`。

## 更新原则

- 只更新受当前任务影响的字段
- 保持 JSON 结构稳定
- 日期统一使用 `YYYY-MM-DD`

## 最小更新建议

- 生成周计划后：
  更新 `learning-progress.json` 中的 `next_recommended_topics`
- 生成练习后：
  如发现明显薄弱点，补充 `weak-points.json`
- 做完一周总结后：
  更新 `current-context.json` 中的 `focus` 和 `next_actions`

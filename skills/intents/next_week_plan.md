# next_week_plan

> 为下一周生成学习计划的 intent skill 占位文件。

## 输入检查

- 读取 `state/dynamic-outline.json`
- 读取 `state/learner-profile.json`
- 读取 `state/learning-progress.json`
- 读取 `state/weak-points.json`
- 回看最近完成的 `study/units/`

## 输出要求

- 写入 `plan/`
- 包含每日主题、最小行动、项目推进和复习安排
- 明确哪些内容延续当前周，哪些是新主题
- 如果当前主线节点不稳定，优先生成补强安排，而不是直接推进后续节点
- 每天任务要标明是“主线推进”还是“补强复习”

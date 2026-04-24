# review_session_result

> 根据一次学习结果更新动态大纲和后续调度。

## 输入检查

- 读取 `state/dynamic-outline.json`
- 读取 `state/weak-points.json`
- 读取 `state/current-context.json`
- 回看本次学习包 `study/dayN/` 下的 `notes.md` 和 `mistakes.md`

## 输出要求

- 判断本次结果属于 `good`、`mixed`、`poor` 中哪一类
- 更新对应节点状态、薄弱点计数和补强动作
- 明确下一次是继续推进、轻复习还是暂停主线补强
- 必要时更新 `study/dayN/day.json` 中的完成状态
- 同步更新 `plan/current-outline.md` 的可读摘要

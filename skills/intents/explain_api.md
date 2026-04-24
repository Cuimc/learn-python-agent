# explain_api

> 解释指定 Python API 的参数、返回值、真实用法与常见误区。

## 输入检查

- 读取 `plan/outline.json`，确认当前 API 所属知识范围
- 读取 `state/current-context.json`，确认当前 `day_id`、`focus`、`outline_refs`
- 优先检索 `source/` 和 `tmp/pdfs/` 中的资料

## 输出要求

- 默认写入 `study/<day-id>/lesson.md` 或补充到当天 lesson
- 如有必要，把个人误区写入 `study/<day-id>/notes.md`
- 解释时必须补齐：
  - API 解决什么问题
  - 常见签名
  - 关键参数
  - 返回值
  - 最小示例
  - 真实场景示例
  - 至少两个常见误区
- 尽量给出 JS / TS 类比，但不要喧宾夺主

## 禁止项

- 不要把解释结果写入 `study/units/**`

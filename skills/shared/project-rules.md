# Project Rules

> 共享项目规则：所有 intent 默认遵守。

## 项目定位

- 面向“前端转 Python / AI Agent”的学习者
- 主参考资料优先来自：
  - `source/`
  - `tmp/pdfs/`
  - `plan/outline.json`
  - `state/dynamic-outline.json`

## day-first workflow

- 固定大纲：`plan/outline.json`
- 动态状态：`state/dynamic-outline.json`
- 当前上下文：`state/current-context.json`
- 单日计划只写入 `plan/days/<day-id>.md`
- 单日学习包只写入 `study/<day-id>/`
- `study/units/` 只作为可选知识索引，不是任务输出层

## 写入约束

- 不要覆盖已有人工内容，除非明确要求
- 所有写文件 intent 都必须遵守：
  - plan 写入 `plan/days/`
  - day 学习包写入 `study/<day-id>/`
  - 不写入 `study/units/**`

## 状态更新规则

- 只更新受当前任务影响的字段
- `state/current-context.json` 只描述当前 day、当前 focus、outline_refs、source_refs 和输出目录
- 日期统一使用 `YYYY-MM-DD`

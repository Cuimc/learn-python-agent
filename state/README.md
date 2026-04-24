# State

本目录保存学习者状态，供后续 agent 持续读写。

## 原则

- 以 JSON 为主，便于脚本和 agent 直接处理
- 字段尽量稳定，避免频繁变更结构
- 每次生成学习内容后，只更新必要字段

## 文件说明

- `learner-profile.json`: 学习者背景、目标、节奏
- `learning-progress.json`: 已完成 day、已完成单元、当前单元、项目进度
- `weak-points.json`: 薄弱点、误区、复习建议
- `current-context.json`: 当前阶段、当前 day 学习包、当前学习单元、下一步动作
- `dynamic-outline.json`: 动态学习大纲的真实数据源，负责主线、节点、依赖和调整记录

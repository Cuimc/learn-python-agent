# Skills

本目录存放当前学习工作流使用的最小技能集。

## 当前只保留 4 个核心 intent

- `generate_day`
- `review_day`
- `explain_api`
- `summarize_week`

其中：

- `generate_day` 是唯一的“生成今天任务”入口
- `generate_exercises`、`harder_exercises` 不再作为独立入口，而是 `generate_day` 的内部子模式
- `review_day` 负责单日复盘和状态回写
- `summarize_week` 负责周总结和下周最小安排

## 目录职责

- `shared/`: 只保留项目规则、教学风格、质量检查
- `intents/`: 4 个核心 intent 的执行说明
- `templates/`: day-first workflow 使用的模板

## day-first 约定

- 单日计划写入 `plan/days/<day-id>.md`
- 单日学习包写入 `study/<day-id>/`
- `study/units/` 是索引层，不是任务输出层

## 历史文件

- 历史 skill 已移动到 `docs/legacy-skills/`

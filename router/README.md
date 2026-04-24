# Router

本目录存放学习工作流的意图路由配置。

## 用途

- 将用户请求归类为固定 intent
- 为每个 intent 指定默认输入、输出位置与推荐 skill
- 作为后续脚本或 agent 的统一入口配置

## 维护规则

- 新增 intent 时，先补充 `intents.yaml`
- 保持命名稳定，避免随意改动已有 key
- 输出路径尽量绑定到 `plan/`、`study/dayN/`、`study/units/`、`state/`

## 当前文件

- `intents.yaml`: 核心路由表

## 动态大纲约定

- 任务生成优先读取 `state/dynamic-outline.json`
- 周计划和单次任务都不能只按固定顺序推进
- 如果学习结果写回了薄弱点或补强动作，后续路由要优先处理补强块
- 单日学习包统一写到 `study/dayN/`
- 学习单元目录统一使用 `study/units/<大单元>/<小单元>/`

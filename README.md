# Python Learning Agent

## 项目目标
- 用 Codex + 资料库 + skills 生成渐进式 Python 学习计划
- 面向前端转 Python / AI Agent 学习者
- 以项目导向、小步推进为核心

## 目录说明
- plan/: 周计划与路线图
- skills/: 规则与模板
- study/: 学习产出（`dayN` 学习包 + `units` 单元库）
- state/: 学习状态
- source/: 原始资料与蒸馏资料
- evals/: 输出质量检查
- scripts/: 辅助脚本

## 工作流
1. 用户输入需求
2. router 判断意图
3. 先读取 `state/dynamic-outline.json` 判断当前主线节点与补强队列
4. 选择对应 skill 与教学风格配置
5. 检索主参考书与必要资料
6. 先根据大纲和动态大纲选择当天引用的 unit，再生成 `study/dayN/` 学习包
7. eval 检查
8. 将学习结果回写到 state，并动态调整后续任务

## 当前阶段
- 当前学习大单元 / 小单元
- 当前主线书章节
- 当前重点薄弱项
- 当前动态大纲节点

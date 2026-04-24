# generate_next_task

> 根据动态大纲生成下一次最小学习任务。

## 输入检查

- 读取 `state/dynamic-outline.json`
- 读取 `state/current-context.json`
- 读取 `state/weak-points.json`
- 读取 `state/learning-progress.json`
- 读取 `skills/shared/teaching-style.md`

## 输出要求

- 先读取 `plan/outline.json`，确认当前固定大纲节点和相邻相关节点
- day 是执行层，unit 是知识层；先生成或更新 `study/dayN/` 学习包，再用对应 unit 作为知识来源
- 先判断当前主线节点是否允许继续推进
- 如果补强队列里有高优先级主题，先生成补强任务
- 如果主线稳定，再生成下一步主线任务
- 输出必须解释“为什么这次任务这样安排”
- 单日学习包默认引用 `1-3` 个强相关 unit，不要把 day 和 unit 混成同一个目录结构
- 当天真正交付给学习者的文件应放在：
  - `study/dayN/plan.md`
  - `study/dayN/lesson.md`
  - `study/dayN/practice.py`
  - `study/dayN/answers.md`
  - `study/dayN/notes.md`
  - `study/dayN/mistakes.md`
  - `study/dayN/day.json`
- `lesson.md` 默认按“单书主线 + 教程正文 + 最小增强”生成
- 练习默认优先生成可运行的 `practice.py`
- `exercises.md` 如果生成，只作为练习说明或索引，不替代可运行练习文件
- 不要把 `lesson.md` 写成大段提示清单
- 讲解强度默认面向“有编程基础的学习者”
- `exercises.md` 至少包含：概念分析题、实现题、改错 / 重构题、边界输入题
- 每天不能只围绕一个过窄知识点展开，默认要打包 `2-4` 个强相关知识点
- 对“函数 / 脚本 / 数据处理”这类阶段，单日 lesson 至少覆盖：
  - 1 个核心概念点
  - 1 个接口或数据结构设计点
  - 1 个主流程组织或真实使用点
- 如果当前固定节点下有多个直接相关子点，优先在同一天内组合推进，而不是拆得过碎
- `lesson.md` 默认至少包含：
  - 1 个核心问题
  - 2 个最小示例
  - 1 个变化示例
  - 1 个真实脚本案例
  - 2 到 3 个常见误解
- `practice.py` 默认至少包含 `5` 组任务，并且必须覆盖：
  - `2` 个实现题
  - `1` 个边界输入题
  - `1` 个改错 / 重构题
  - `1` 个主流程整合题
- 如果输出只剩“单一语法点 + 低强度热身题”，视为不合格任务

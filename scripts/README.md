# Scripts

本目录存放辅助脚本。

## 当前建议

- 根据 `plan/outline.json` 初始化或同步 `study/units/` 单元骨架
- 校验 `state/` 字段完整性
- 根据 `router/intents.yaml` 做简单路由

## 当前脚本

- `init_day_plan.py`
  - 读取 `state/current-context.json`
  - 生成 `study/dayN/` 学习包
  - 优先从对应 unit 复制 `lesson / practice / answers / notes / mistakes`
  - 只初始化缺失文件，不覆盖已有内容
- `sync_units_from_outline.py`
  - 读取固定大纲
  - 生成 `study/units/<大单元>/<小单元>/`
  - 仅补缺失文件，不覆盖已有学习产出
- `fetch_liaoxuefeng_python_intro.py`
  - 抓取廖雪峰 Python 教程从 `Python基础` 到结尾的章节
  - 将原始结构化内容写入 `source/liaoxuefeng-python-introduction-from-basic/`
  - 将蒸馏结果写入 `tmp/web/`

## 约束

- 脚本优先做小而明确的事情
- 输入输出路径尽量固定
- 不直接覆盖已有学习产出

# Study Units

本目录按固定大纲的“大单元 / 小单元”组织可选知识索引。

## 目录约定

- 一级目录：大单元中文标题
  例如：`Python基础`、`函数`
- 二级目录：`<outline-id>-<中文标题>`
  例如：`5.1-数据类型和变量`、`6.3-函数的参数`

## 每个小单元的标准文件

- `unit.json`
- `refs.md`

## 使用规则

- 固定大纲决定“学到哪里”
- day 计划决定“今天具体学哪些大纲节点”
- 动态大纲决定“在当前单元是正常推进、补强还是回退”
- 当天正式任务统一写到 `study/<day-id>/`
- 本目录不再生成新的 `lesson / practice / answers / notes / mistakes`
- 初次同步目录骨架时，运行 `python3 scripts/sync_units_from_outline.py`

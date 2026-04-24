# Study Units

本目录按固定大纲的“大单元 / 小单元”组织学习内容。

## 目录约定

- 一级目录：大单元中文标题
  例如：`Python基础`、`函数`
- 二级目录：`<outline-id>-<中文标题>`
  例如：`5.1-数据类型和变量`、`6.3-函数的参数`

## 每个小单元的标准文件

- `lesson.md`
- `practice.py`
- `answers.md`
- `notes.md`
- `mistakes.md`
- `unit.json`

## 使用规则

- 固定大纲决定“学到哪里”
- day 计划决定“今天具体学哪些 unit”
- 动态大纲决定“在当前单元是正常推进、补强还是回退”
- 同一个单元补强时，优先更新同目录下的文件，不新建无关目录
- 初次同步目录骨架时，运行 `python3 scripts/sync_units_from_outline.py`

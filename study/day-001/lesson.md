# Day 001：数据类型、变量绑定与最小输出

> 当前 focus：Python基础 / 数据类型和变量
> 固定大纲：`outline-5-1`

## 今天要解决什么问题

你已经有 JS / TS 背景，所以今天不需要花很多时间理解“变量是什么”。  
真正要打稳的是 4 个 Python 入门关卡：

1. Python 里最常见的基础值长什么样  
2. 变量在 Python 里是“绑定名字”，不是 `let` / `const` 的直接翻版  
3. `None`、`False`、`0`、空字符串不是同一个东西  
4. 输出混合类型时，优先用 f-string，而不是直接做字符串拼接

## 今天涉及的知识点

- `int`、`float`、`str`、`bool`、`None`
- 变量绑定与重新赋值
- `type()` 查看运行时类型
- `print()` 和 f-string
- Python 和 JS / TS 在“空值”和变量声明上的差异

## 概念讲解

Python 和 JavaScript 一样，也是动态类型语言。你写代码时通常不需要先声明变量类型，运行时值自己带着类型走。  
比如 `28` 是整数，`19.9` 是浮点数，`"Ada"` 是字符串，`True` 是布尔值，`None` 表示“这里现在没有值”。

今天先记一个够用判断：

- `0` 表示数字零
- `""` 表示空字符串
- `False` 表示布尔假
- `None` 表示“没有值”或“值缺席”

这四个都可能在条件判断里表现为“假”，但语义完全不同。  
以后写脚本、处理接口返回值、清洗数据时，你经常要分清“值是空”还是“根本没有值”。

变量这一块，Python 的重点也不是“声明”，而是“绑定”。  
`name = "Ada"` 的意思不是“定义一个叫 name 的盒子”，而是“让名字 `name` 指向字符串 `"Ada"`”。  
所以 `=` 在 Python 里首先是赋值，不是数学上的相等判断。

## 核心规则

- `True`、`False`、`None` 必须大写开头，写成 `true`、`false`、`none` 会报错
- 变量不需要 `let`、`const`、`var`
- `type(value)` 用来快速确认值的运行时类型
- 混合类型输出时，优先用 f-string：`f"name={name}, age={age}"`
- 重新赋值只会改变当前名字的绑定，不会自动回头修改已经保存下来的旧值

## 最小示例 1：5 个基础值

```python
age = 28
price = 19.9
nickname = "Ada"
is_ready = True
remark = None

print(age, price, nickname, is_ready, remark)
```

这 5 个值基本覆盖了你接下来写小脚本时最常见的基础输入。  
以后你处理配置、命令行参数、接口字段、日志摘要，几乎都会在这几个类型里打转。

## 最小示例 2：运行时类型

```python
age = 28
nickname = "Ada"
is_ready = True
remark = None

print(type(age))
print(type(nickname))
print(type(is_ready))
print(type(remark))
```

如果你刚从 TS 过来，`type()` 可以暂时把它理解成“运行时帮你看值现在到底是什么”。  
它不是类型系统推导，而是直接看当前值的真实类型。

## 变化示例：变量绑定不是声明关键字

```python
a = "ABC"
b = a
a = "XYZ"

print(a)
print(b)
```

运行结果里，`a` 是 `"XYZ"`，但 `b` 仍然是 `"ABC"``。  
这里最容易带入错误直觉：以为“a 变了，b 也会跟着变”。  
Python 这里更像“名字重新指向了别的值”，不是把所有引用位置同时改写。

## JS / TS 对照

- Python 变量没有 `let` / `const`
- f-string 很像 JS 模板字符串：`` `name=${name}` `` 对应 `f"name={name}"`
- `None` 更接近 JS 的 `null`，但 Python 没有一个日常数据层面的 `undefined`
- `True` / `False` 在 Python 里首字母大写，和 JS 不一样

## 真实脚本案例

假设你在写一个 AI 应用的小脚本，准备先把用户输入打印成调试日志：

```python
user_name = "Ada"
retry_count = 2
is_trial = False
note = None

print(
    f"user={user_name}, retries={retry_count}, "
    f"trial={is_trial}, note={note}"
)
```

这个例子没有高级语法，但它已经很像真实脚本里的最小日志输出了。  
它同时用到了字符串、整数、布尔值、`None` 和 f-string。  
今天把这类最小表达写顺了，后面学条件、循环、函数时会轻很多。

## 常见误解

### 1. 把 `true` / `false` / `null` 直接搬进 Python

这是最常见的 JS 迁移错误。Python 里要写：

- `True`
- `False`
- `None`

### 2. 直接做字符串和数字拼接

下面这种写法会报错：

```python
name = "Ada"
age = 28
print(name + " is " + age)
```

因为右边最后一段是整数，不是字符串。  
今天最简单的修法就是改成 f-string。

### 3. 把 `None` 当成 `False`

它们都可能在条件判断里表现为“假”，但语义不同。  
`False` 是一个明确的布尔结果，`None` 是“现在没有值”。

## 今天任务

1. 运行 `study/day-001/practice.py`，先观察当前占位输出
2. 完成 5 组任务，把错误类型改对
3. 用 f-string 修掉“字符串 + 数字”的问题
4. 在 `notes.md` 写下你对 `None`、变量绑定和 f-string 的一句话总结
5. 在 `mistakes.md` 记录至少 2 个今天最容易犯的错误

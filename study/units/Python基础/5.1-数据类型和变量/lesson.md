# Python基础 / 5.1 数据类型和变量

## 本单元解决什么问题

这个单元是 Python 主线的真正起点。你已经有编程基础，所以今天不是“认识变量”这种零基础内容，而是先把 Python 对“值”和“名字”的处理方式建立起来。后面无论写条件、循环、函数，还是做脚本清洗和 Agent 工具调用，底层都离不开这几件事：

- 先知道值是什么：`int`、`float`、`str`、`bool`、`None`
- 再知道名字怎么绑定值
- 最后知道表达式算出来的到底是什么类型

它在固定大纲里的位置是 `Python基础 / 数据类型和变量`，也是后面 `字符串和编码`、`list / tuple`、`函数的参数` 的前置基础。

## 本单元涉及的知识点

- 基础值类型：整数、浮点数、字符串、布尔值、空值
- 变量绑定、重新赋值和运行时类型
- 表达式计算、比较结果、最小输出
- `type()` 的最小使用方式
- f-string 的最小用法

## 概念讲解

Python 和 JS/TS 在“先有值，再把名字指向值”这件事上很像，但写法和约束不同。

在 JS 里你会写：

```ts
let score = 95;
```

在 Python 里你直接写：

```python
score = 95
```

这里没有 `let`、`const`、`var`。`score` 这个名字会被绑定到值 `95`。后面如果你再写：

```python
score = "95"
```

语法仍然是合法的，因为 Python 默认是动态类型语言。名字没有被“声明成 int”，只是当前绑定到了一个 `int` 值，后面又重新绑定到了 `str` 值。对有经验的开发者来说，这既灵活，也意味着你必须更清楚自己现在手里拿到的是什么类型。

今天要先建立 5 个最常见的值类型直觉：

- `int`：整数，例如 `1`、`42`、`-7`
- `float`：浮点数，例如 `3.14`、`0.5`
- `str`：字符串，例如 `"python"`、`'agent'`
- `bool`：布尔值，只有 `True` 和 `False`
- `None`：空值，表示“这里现在没有值”

其中 `None` 很值得单独记。它更接近 JS 里的 `null`，但 Python 没有 `undefined` 这个值。一个变量如果根本没定义，Python 不会给你 `undefined`，而是直接抛 `NameError`。所以：

- `nickname = None` 表示“这个名字存在，但当前没有实际值”
- 直接写 `nickname` 且此前没赋值，表示“这个名字根本不存在”

还有两个容易踩的细节：

1. Python 的布尔字面量首字母大写：`True`、`False`  
   不是 JS 风格的 `true`、`false`
2. Python 不会像 JS 那样把数字和字符串随便拼起来  
   `1 + "2"` 会直接报错，必须显式转换或用 f-string

如果你暂时不确定一个值的类型，可以先用 `type()` 看运行时类型：

```python
user_name = "Mia"
score = 95
print(type(user_name))
print(type(score))
```

今天先把 `type()` 当成“调试观察工具”，不要把重点放在它的函数定义上。函数本身会在后面系统讲。

## JS / TS 对照

- `let score = 95` 对应 `score = 95`
- `null` 更接近 `None`
- Python 没有 `undefined` 值；未定义名字会直接报错
- JS 常见的隐式拼接在 Python 里通常行不通，类型要更明确

## 最小示例 1

```python
age = 18
height = 175.5
language = "Python"
is_ready = True
extra_note = None

print(age, type(age))
print(height, type(height))
print(language, type(language))
print(is_ready, type(is_ready))
print(extra_note, type(extra_note))
```

这个例子只做一件事：把 5 类最常见的值摆在你面前。先不追求花哨，先记住“字面量长什么样”和“类型名是什么”。

## 最小示例 2

```python
score = 95
target = 60
passed = score >= target

print(score + 5)
print(passed)
print(type(passed))
```

这里开始把“值”推进到“表达式”。`score >= target` 的结果不是数字，而是 `bool`。这一步很关键，因为后面的条件判断和过滤逻辑都会依赖这种结果。

## 变化示例

```python
user_name = "Mia"
score = 95
passed = score >= 60

summary = f"{user_name} score={score}, passed={passed}"
print(summary)
```

如果你是前端开发者，可以把这句理解成 Python 版模板字符串。今天不需要引入复杂格式化，只要先用它避免“字符串和数字直接相加”的错误。

## 真实案例

假设你后面要做一个学习记录清洗脚本，处理每个学习者的最小状态。哪怕只是第一步，底层也还是这些值：

```python
learner_name = "Mia"
finished_minutes = 95
target_minutes = 60
need_review = finished_minutes < target_minutes

report_line = (
    f"{learner_name}: "
    f"finished={finished_minutes}, "
    f"target={target_minutes}, "
    f"need_review={need_review}"
)

print(report_line)
```

这里还没有用到列表、字典、函数，但你已经能看到真实脚本的雏形了：先有值，再有变量，再有表达式，最后形成输出。后面的章节只是把这些基础动作组织得更复杂。

## 常见误解

- 把 `true`、`false`、`null` 直接搬进 Python  
  Python 里应写 `True`、`False`、`None`
- 以为变量一旦放了数字，就永远只能是数字  
  Python 语法不会阻止你重新绑定，但这会影响后续表达式和类型判断
- 以为 `"score=" + 95` 会像 JS 一样自动转成字符串  
  Python 默认不会这样做
- 把 `None` 和空字符串 `""`、数字 `0` 当成同一个东西  
  它们语义不同，后面处理边界输入时差别很大

## 本单元任务

1. 运行 `practice.py` 的示例区，确认自己能看懂每一行输出的值和类型
2. 完成 `practice.py` 里的 5 组任务，至少做完其中 4 组
3. 在 `notes.md` 里写下你今天新确认的 3 条规则
4. 在 `mistakes.md` 里记录至少 2 个错误，尤其是大小写、类型拼接、`None` 处理

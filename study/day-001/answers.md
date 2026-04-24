# Day 001 Answers

> 对应 `study/day-001/practice.py`。先自己做，再看这里。

## task_1：把 5 个基础值类型改对

参考答案可以写成这样：

```python
def task_1_age() -> object:
    return 28


def task_1_price() -> object:
    return 19.9


def task_1_name() -> object:
    return "Ada"


def task_1_is_ready() -> object:
    return True


def task_1_note() -> object:
    return None
```

### 这一题在练什么

- `28` 是 `int`
- `19.9` 是 `float`
- `"Ada"` 是 `str`
- `True` 是 `bool`
- `None` 表示“没有值”

重点不是背定义，而是把“值长什么样”练到手感里。

## task_2：用 f-string 输出一条概要信息

参考答案：

```python
def task_2_profile_line(name: str, age: int, city: str) -> str:
    return f"name={name} | age={age} | city={city}"
```

### 为什么推荐这样写

不要用：

```python
name + " | age=" + age
```

因为这里会把字符串和整数硬拼在一起，直接报 `TypeError`。  
f-string 是今天最小、最稳、最像 JS 模板字符串的解法。

## task_3：变量重新绑定

代码：

```python
a = "ABC"
b = a
a = "XYZ"
return b
```

结果是：

```python
"ABC"
```

### 为什么

`b = a` 时，`b` 已经拿到了当时 `a` 对应的值。  
后面 `a = "XYZ"` 是让 `a` 重新绑定到新值，不会回头修改 `b`。

这题是今天最重要的认知点之一。  
如果你把这里想成“声明的盒子被整体改写”，后面学列表、函数参数时会继续混乱。

## task_4：写布尔表达式

参考答案：

```python
def task_4_can_start_trial(balance: int, has_coupon: bool, is_blocked: bool) -> bool:
    return (balance >= 99 or has_coupon) and not is_blocked
```

### 为什么这样写

先判断“是否有资格开始”：

- 余额够
- 或者有 coupon

再加一条硬限制：

- 只要被 block，就不允许开始

这类布尔表达式以后会频繁出现在参数校验、权限判断、配置开关里。

## task_5：区分 `None` 和普通字符串

参考答案：

```python
def task_5_note_label(note: object) -> str:
    if note is None:
        return "note=None"
    return f"note={note}"
```

### 这一题为什么重要

它在练 2 件事：

1. `None` 不是空字符串  
2. 输出前要先分清“没值”和“有值但内容为空”

如果你把 `None` 和 `False`、`0`、`""` 混成一类，后面处理接口字段和脚本参数时会很容易出 bug。

## 自查清单

看完答案后，确认你能自己说出这 5 句：

- Python 基础值里最常用的是 `int / float / str / bool / None`
- Python 变量不需要 `let` / `const`
- `type(value)` 是看运行时类型
- 混合类型输出优先用 f-string
- `None` 和 `False` 不是一回事

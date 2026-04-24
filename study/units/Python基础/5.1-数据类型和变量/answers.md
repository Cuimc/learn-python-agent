# Python基础 / 5.1 参考答案

## 练习 1

### 思路

- 这一题只检查你能不能正确写出 4 类最基本的字面量
- `None` 不是字符串 `"None"`，而是一个特殊值

### 参考实现

```python
age = 18
completion_ratio = 0.75
is_python_ready = True
backup_note = None
```

### 说明

- `18` 是 `int`
- `0.75` 是 `float`
- `True` 是 `bool`
- `None` 表示“没有值”，而不是空字符串

## 练习 2

### 思路

- 目标不是做复杂格式化，而是用 `repr(value)` 和 `type(value).__name__` 把值和类型说清楚
- 用 `repr()` 的好处是字符串会带引号，观察更直接

### 参考实现

```python
def describe_value(value):
    return f"value={value!r}, type={type(value).__name__}"
```

### 说明

- `value!r` 等价于对值做 `repr(value)`
- 这比直接 `str(value)` 更适合拿来观察值本身

## 练习 3

### 思路

- 这一题在练最小输出格式
- 暂时不用列表、字典、函数参数设计，只先把三个变量组织成一行结果

### 参考实现

```python
def build_user_summary(name, score, is_active):
    return f"name={name}, score={score}, active={is_active}"
```

### 说明

- 这里用 f-string 比字符串拼接更直接
- 也是后面做日志、报告、调试输出时最常见的写法

## 练习 4

### 思路

- 这一题的重点不是字符串处理技巧，而是区分“没有值”和“有值但需要修整”
- `None` 和空字符串都应该回退到 `name`

### 参考实现

```python
def pick_display_name(name, nickname=None):
    if nickname is None or nickname == "":
        return name
    return nickname.strip()
```

### 说明

- `nickname is None` 是在判断是否为空值
- `nickname == ""` 是在判断是否为空字符串
- 这是两个不同概念，不能混成一个

## 练习 5

### 思路

- 这里是在修一个 JS 开发者很容易带过来的坏习惯：字符串直接和数字相加
- Python 不帮你做这种隐式拼接，所以要么显式转字符串，要么直接用 f-string

### 参考实现

```python
def build_report_line(name, score, target=60):
    passed = score >= target
    return f"{name} => score={score}, passed={passed}"
```

### 说明

- 先用表达式算出 `passed`
- 再统一交给 f-string 输出
- 这种“先算值，再输出”的写法比边拼字符串边计算更稳

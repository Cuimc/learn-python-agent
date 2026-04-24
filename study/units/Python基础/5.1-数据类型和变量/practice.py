# 运行方式：python3 practice.py

UNFINISHED = object()


def print_header(title):
    print(f"\n=== {title} ===")


def print_result(task_name, ok, detail):
    status = "OK" if ok else "TODO"
    print(f"[{status}] {task_name}: {detail}")


def has_unfinished(*values):
    return any(value is UNFINISHED for value in values)


# ===== 本文件会用到的新内容清单 =====
# 1. int / float / str / bool / None
# 2. 变量绑定与重新赋值
# 3. 表达式、比较和 f-string


# ===== 示例区 =====
def run_examples():
    print_header("示例区")
    user_name = "Mia"
    score = 95
    passed = score >= 60
    extra_note = None

    print(f"user_name={user_name}, type={type(user_name).__name__}")
    print(f"score={score}, type={type(score).__name__}")
    print(f"passed={passed}, type={type(passed).__name__}")
    print(f"extra_note={extra_note}, type={type(extra_note).__name__}")


# ===== 练习 1：补全代码 / 预测输出 =====
def task1_fill_values():
    # TODO: 把下面 4 个 UNFINISHED 改成正确字面量
    age = UNFINISHED
    completion_ratio = UNFINISHED
    is_python_ready = UNFINISHED
    backup_note = UNFINISHED

    if has_unfinished(age, completion_ratio, is_python_ready, backup_note):
        return False, "把 age / completion_ratio / is_python_ready / backup_note 改成 int / float / bool / None"

    checks = [
        isinstance(age, int) and not isinstance(age, bool),
        isinstance(completion_ratio, float),
        isinstance(is_python_ready, bool),
        backup_note is None,
    ]
    detail = (
        f"age={type(age).__name__}, "
        f"completion_ratio={type(completion_ratio).__name__}, "
        f"is_python_ready={type(is_python_ready).__name__}, "
        f"backup_note={backup_note!r}"
    )
    return all(checks), detail


# ===== 练习 2：实现题 =====
def describe_value(value):
    """
    返回格式:
    value='python', type=str
    value=3.5, type=float
    """
    return UNFINISHED


def check_task2():
    result_a = describe_value("python")
    result_b = describe_value(3.5)
    if result_a is UNFINISHED or result_b is UNFINISHED:
        return False, "实现 describe_value(value)"

    ok = (
        result_a == "value='python', type=str"
        and result_b == "value=3.5, type=float"
    )
    detail = f"sample_a={result_a!r}, sample_b={result_b!r}"
    return ok, detail


# ===== 练习 3：实现题 =====
def build_user_summary(name, score, is_active):
    """
    返回格式:
    name=Mia, score=95, active=True
    """
    return UNFINISHED


def check_task3():
    result = build_user_summary("Mia", 95, True)
    if result is UNFINISHED:
        return False, "实现 build_user_summary(name, score, is_active)"

    ok = result == "name=Mia, score=95, active=True"
    return ok, f"result={result!r}"


# ===== 练习 4：边界输入题 =====
def pick_display_name(name, nickname=None):
    """
    规则:
    - nickname 是 None 或空字符串时，返回 name
    - nickname 有值时，返回去掉首尾空格后的 nickname
    """
    return UNFINISHED


def check_task4():
    result_a = pick_display_name("Mia")
    result_b = pick_display_name("Mia", "")
    result_c = pick_display_name("Mia", "  Ace  ")
    if (
        result_a is UNFINISHED
        or result_b is UNFINISHED
        or result_c is UNFINISHED
    ):
        return False, "实现 pick_display_name(name, nickname=None)"

    ok = result_a == "Mia" and result_b == "Mia" and result_c == "Ace"
    detail = f"results=({result_a!r}, {result_b!r}, {result_c!r})"
    return ok, detail


# ===== 练习 5：找 bug / 重构 / 主流程整合题 =====
def build_report_line(name, score, target=60):
    """
    原来的坏写法类似这样:
    name + " => " + score

    目标输出:
    Mia => score=95, passed=True
    """
    return UNFINISHED


def check_task5():
    result = build_report_line("Mia", 95)
    if result is UNFINISHED:
        return False, "实现 build_report_line(name, score, target=60)"

    ok = result == "Mia => score=95, passed=True"
    return ok, f"result={result!r}"


def run_checks():
    print_header("练习检查")
    tasks = [
        ("练习 1", task1_fill_values),
        ("练习 2", check_task2),
        ("练习 3", check_task3),
        ("练习 4", check_task4),
        ("练习 5", check_task5),
    ]

    for task_name, fn in tasks:
        ok, detail = fn()
        print_result(task_name, ok, detail)


if __name__ == "__main__":
    print("day-001 / Python基础 / 5.1 数据类型和变量")
    print("先看示例输出，再修改每道题里的 UNFINISHED 或函数实现。")
    run_examples()
    run_checks()

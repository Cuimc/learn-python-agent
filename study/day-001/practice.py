"""Day 001 practice: 数据类型、变量绑定与最小输出。

用法:
1. 先直接运行:
   python3 study/day-001/practice.py
2. 按 TODO 修改代码
3. 修改完成后运行:
   python3 study/day-001/practice.py --check
"""

from __future__ import annotations

import sys


def task_1_age() -> object:
    # TODO: 改成 int，而不是 str
    return "28"


def task_1_price() -> object:
    # TODO: 改成 float，而不是 str
    return "19.9"


def task_1_name() -> object:
    # TODO: 改成非空 str，而不是 None
    return None


def task_1_is_ready() -> object:
    # TODO: 改成 bool，而不是 str
    return "True"


def task_1_note() -> object:
    # TODO: 改成 None，而不是数字 0
    return 0


def task_2_profile_line(name: str, age: int, city: str) -> str:
    # TODO: 用 f-string 返回:
    # "name=Ada | age=28 | city=Shanghai"
    return "TODO"


def task_3_rebinding_result() -> str:
    a = "ABC"
    b = a
    a = "XYZ"
    return b


def task_4_can_start_trial(balance: int, has_coupon: bool, is_blocked: bool) -> bool:
    # TODO:
    # 规则:
    # - 余额大于等于 99 可以开始试用
    # - 或者有 coupon 也可以开始试用
    # - 但只要 is_blocked 为 True，就必须返回 False
    return False


def task_5_note_label(note: object) -> str:
    # TODO:
    # - 如果 note 是 None，返回 "note=None"
    # - 否则返回 f"note={note}"
    return "TODO"


def show_current_state() -> None:
    print("== Day 001 当前输出 ==")
    age = task_1_age()
    price = task_1_price()
    name = task_1_name()
    is_ready = task_1_is_ready()
    note = task_1_note()

    print("task_1 values:")
    print(" age      ->", age, "| type =", type(age))
    print(" price    ->", price, "| type =", type(price))
    print(" name     ->", name, "| type =", type(name))
    print(" is_ready ->", is_ready, "| type =", type(is_ready))
    print(" note     ->", note, "| type =", type(note))

    print("\ntask_2 profile line:")
    print(task_2_profile_line("Ada", 28, "Shanghai"))

    print("\ntask_3 rebinding result:")
    print(task_3_rebinding_result())

    print("\ntask_4 can start trial:")
    print(task_4_can_start_trial(120, False, False))
    print(task_4_can_start_trial(20, True, False))
    print(task_4_can_start_trial(120, True, True))

    print("\ntask_5 note label:")
    print(task_5_note_label(None))
    print(task_5_note_label("VIP user"))


def run_checks() -> None:
    age = task_1_age()
    price = task_1_price()
    name = task_1_name()
    is_ready = task_1_is_ready()
    note = task_1_note()

    assert type(age) is int, "task_1_age 必须返回 int"
    assert type(price) is float, "task_1_price 必须返回 float"
    assert type(name) is str and name, "task_1_name 必须返回非空 str"
    assert type(is_ready) is bool, "task_1_is_ready 必须返回 bool"
    assert note is None, "task_1_note 必须返回 None"

    assert (
        task_2_profile_line("Ada", 28, "Shanghai")
        == "name=Ada | age=28 | city=Shanghai"
    ), "task_2_profile_line 输出不对"

    assert task_3_rebinding_result() == "ABC", "task_3_rebinding_result 应该返回 ABC"

    assert task_4_can_start_trial(120, False, False) is True
    assert task_4_can_start_trial(20, True, False) is True
    assert task_4_can_start_trial(120, True, True) is False

    assert task_5_note_label(None) == "note=None"
    assert task_5_note_label("VIP user") == "note=VIP user"

    print("All checks passed.")


def main() -> None:
    if "--check" in sys.argv:
        run_checks()
        return
    show_current_state()
    print("\n现在开始改 TODO，改完后再运行: python3 study/day-001/practice.py --check")


if __name__ == "__main__":
    main()

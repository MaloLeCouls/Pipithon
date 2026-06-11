from solution_user import notify_all


def test_calls_each_callback_with_package_id():
    audit = lambda pid: f"audit:{pid}"
    notify = lambda pid: f"notify:{pid}"
    assert notify_all([audit, notify], "X1") == ["audit:X1", "notify:X1"]


def test_order_preserved():
    a = lambda _: "first"
    b = lambda _: "second"
    c = lambda _: "third"
    assert notify_all([a, b, c], "P") == ["first", "second", "third"]


def test_empty_callback_list_returns_empty():
    assert notify_all([], "X") == []


def test_works_with_named_function():
    def log(pid: str) -> str:
        return f"log[{pid}]"
    assert notify_all([log], "Z9") == ["log[Z9]"]


def test_works_with_mixed_callable_types():
    # fn nommée + lambda dans la même liste.
    def upper(pid: str) -> str:
        return pid.upper()
    assert notify_all([upper, lambda p: p.lower()], "Mixed") == ["MIXED", "mixed"]

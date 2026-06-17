from solution_user import TaskRecord, is_urgent, make_task


def test_make_task_basic():
    t = make_task("Ship", 2)
    assert t["title"] == "Ship"
    assert t["priority"] == 2
    assert t["done"] is False


def test_make_task_returns_dict():
    # TypedDict est un dict à runtime.
    assert isinstance(make_task("X", 1), dict)


def test_is_urgent_true():
    assert is_urgent({"title": "X", "priority": 5, "done": False}) is True


def test_is_urgent_false_low_priority():
    assert is_urgent({"title": "X", "priority": 1, "done": False}) is False


def test_is_urgent_false_done():
    assert is_urgent({"title": "X", "priority": 5, "done": True}) is False


def test_typeddict_declares_keys():
    """Les annotations TypedDict sont accessibles via __annotations__."""
    assert set(TaskRecord.__annotations__) == {"title", "priority", "done"}

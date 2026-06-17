from solution_user import Task


def test_repr_format():
    assert repr(Task("Ship MVP", 2)) == "Task(title='Ship MVP', priority=2)"


def test_str_format():
    assert str(Task("Ship MVP", 2)) == "Ship MVP (P2)"


def test_repr_eval_roundtrip():
    t = Task("Refactor", 1)
    rebuilt = eval(repr(t), {"Task": Task})
    assert rebuilt.title == "Refactor"
    assert rebuilt.priority == 1


def test_print_uses_str_not_default():
    """Sans __repr__/__str__, print(t) afficherait '<Task object at 0x...>'."""
    s = str(Task("X", 3))
    assert "object at" not in s


def test_form_defines_both():
    assert Task.__repr__ is not object.__repr__
    assert Task.__str__ is not object.__str__

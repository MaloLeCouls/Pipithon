import ast
import inspect

from solution_user import run_all


def test_behavior_all_success():
    assert run_all(["A", "B", "C"]) == (3, 0)


def test_behavior_mixed():
    success, fail = run_all(["A", "BROKEN", "B"])
    assert success == 2
    assert fail == 1


def test_behavior_all_failures():
    assert run_all(["BROKEN", "BROKEN"]) == (0, 2)


def test_behavior_empty():
    assert run_all([]) == (0, 0)


def test_form_calls_exception():
    src = inspect.getsource(run_all)
    tree = ast.parse(src)
    has = any(
        isinstance(n, ast.Attribute) and n.attr == "exception" for n in ast.walk(tree)
    )
    assert has, "Vérifie `fut.exception()`."

import ast
import inspect

from solution_user import Box


def test_behavior_unwrap_int():
    assert Box(42).unwrap() == 42


def test_behavior_unwrap_str():
    assert Box("hello").unwrap() == "hello"


def test_behavior_unwrap_list():
    assert Box([1, 2, 3]).unwrap() == [1, 2, 3]


def test_form_class_is_generic():
    # Box[int] doit être légal -> indique que c'est paramétrable.
    Box[int]
    Box[str]


def test_form_uses_typevar():
    import solution_user
    tree = ast.parse(inspect.getsource(solution_user))
    has_typevar = any(
        isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "TypeVar"
        for n in ast.walk(tree)
    )
    assert has_typevar, "La solution doit déclarer un TypeVar."

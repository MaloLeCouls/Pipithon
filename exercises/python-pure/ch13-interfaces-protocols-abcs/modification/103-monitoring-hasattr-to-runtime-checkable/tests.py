import ast
import inspect

from solution_user import Pingable, is_pingable


class Server:
    def ping(self) -> bool:
        return True


class Broken:
    pass


def test_pingable_object_accepted():
    assert is_pingable(Server()) is True


def test_non_pingable_rejected():
    assert is_pingable(Broken()) is False


def test_pingable_is_runtime_checkable():
    # Si non décoré @runtime_checkable, isinstance lèverait TypeError.
    isinstance(object(), Pingable)


def test_form_uses_isinstance():
    src = inspect.getsource(is_pingable)
    tree = ast.parse(src)
    found = False
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "isinstance":
            found = True
            break
    assert found, "Utilise `isinstance(obj, Pingable)`."


def test_form_no_hasattr():
    src = inspect.getsource(is_pingable)
    tree = ast.parse(src)
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            assert n.func.id != "hasattr", "Plus de `hasattr` — utilise le Protocol."

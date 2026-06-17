import ast
import collections
import inspect
import types

from solution_user import is_valid_metadata


def test_accepts_plain_dict():
    assert is_valid_metadata({"a": 1}) is True


def test_accepts_ordered_dict():
    assert is_valid_metadata(collections.OrderedDict(a=1)) is True


def test_accepts_mapping_proxy():
    # Le starter REFUSE celui-ci -> c'est le test qui valide le refactor.
    assert is_valid_metadata(types.MappingProxyType({"a": 1})) is True


def test_rejects_list():
    assert is_valid_metadata([("a", 1)]) is False


def test_rejects_str():
    assert is_valid_metadata("a=1") is False


def test_form_uses_mapping():
    src = inspect.getsource(is_valid_metadata)
    tree = ast.parse(src)
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    assert "Mapping" in names, "Utilise `collections.abc.Mapping`."
    # Plus de dict en isinstance (ils ne peuvent pas coexister)
    has_isinstance_dict = False
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "isinstance":
            for arg in n.args:
                if isinstance(arg, ast.Name) and arg.id == "dict":
                    has_isinstance_dict = True
    assert not has_isinstance_dict, "Plus de `isinstance(..., dict)` — `Mapping` couvre tout."

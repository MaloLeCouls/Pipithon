import ast
import collections.abc as abc
import inspect

from solution_user import Package, pending_tracking_ids


def make_pkgs() -> list[Package]:
    return [
        Package("TRK-1", "pending"),
        Package("TRK-2", "delivered"),
        Package("TRK-3", "pending"),
    ]


def test_behavior_filters_pending():
    assert list(pending_tracking_ids(make_pkgs())) == ["TRK-1", "TRK-3"]


def test_behavior_empty():
    assert list(pending_tracking_ids([])) == []


def test_form_returns_iterator_not_list():
    result = pending_tracking_ids(make_pkgs())
    assert isinstance(result, abc.Iterator)
    assert not isinstance(result, list)


def test_form_uses_genexpr_not_listcomp():
    tree = ast.parse(inspect.getsource(pending_tracking_ids))
    has_listcomp = any(isinstance(n, ast.ListComp) for n in ast.walk(tree))
    has_genexpr = any(isinstance(n, ast.GeneratorExp) for n in ast.walk(tree))
    assert has_genexpr, "Utilise une generator expression `(... for ... if ...)`."
    assert not has_listcomp, "Plus de list comprehension `[... for ... if ...]`."

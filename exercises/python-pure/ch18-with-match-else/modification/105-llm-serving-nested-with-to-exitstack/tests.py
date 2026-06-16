import ast
import inspect

import pytest

from solution_user import FakeCache, with_all_caches


def test_behavior_all_open_during_work():
    caches = [FakeCache(f"c{i}") for i in range(3)]
    seen: list[bool] = []

    def work(opened):
        seen.append(all(c.open for c in opened))
        assert [c.name for c in opened] == ["c0", "c1", "c2"]

    with_all_caches(caches, work)
    assert seen == [True]
    assert all(not c.open for c in caches)


def test_behavior_closes_after_exception():
    caches = [FakeCache(f"c{i}") for i in range(4)]

    def boom(opened):
        raise RuntimeError("crash mid-work")

    with pytest.raises(RuntimeError):
        with_all_caches(caches, boom)
    assert all(not c.open for c in caches)


def test_behavior_empty_list():
    seen: list[list] = []
    with_all_caches([], lambda opened: seen.append(opened))
    assert seen == [[]]


def test_form_uses_exitstack():
    src = inspect.getsource(with_all_caches)
    assert "ExitStack" in src, "Utilise `contextlib.ExitStack`."


def test_form_no_recursive_call():
    # Détection robuste : la version refactorée ne s'appelle pas elle-même.
    tree = ast.parse(inspect.getsource(with_all_caches))
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
    self_calls = [
        c for c in calls
        if isinstance(c.func, ast.Name) and c.func.id == "with_all_caches"
    ]
    assert not self_calls, "Supprime l'appel récursif — ExitStack remplace la récursion."

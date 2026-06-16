import ast
import collections.abc as abc
import inspect

from pymistral import Token
from solution_user import gen_until_eos


def make_stream(ids):
    for i in ids:
        yield Token(id=i, text=str(i))


def test_behavior_stops_at_eos():
    out = list(gen_until_eos(make_stream([1, 2, 9, 3]), eos_id=9))
    assert [t.id for t in out] == [1, 2]


def test_behavior_no_eos_yields_all():
    out = list(gen_until_eos(make_stream([1, 2, 3]), eos_id=99))
    assert [t.id for t in out] == [1, 2, 3]


def test_behavior_eos_first_yields_nothing():
    out = list(gen_until_eos(make_stream([9, 1, 2]), eos_id=9))
    assert out == []


def test_form_returns_iterator():
    result = gen_until_eos(make_stream([1]), eos_id=9)
    assert isinstance(result, abc.Iterator)


def test_form_no_yield_in_body():
    tree = ast.parse(inspect.getsource(gen_until_eos))
    has_yield = any(isinstance(n, (ast.Yield, ast.YieldFrom)) for n in ast.walk(tree))
    assert not has_yield, "Plus de yield : retourne directement le `takewhile`."


def test_form_uses_takewhile():
    src = inspect.getsource(gen_until_eos)
    assert "takewhile" in src, "Utilise `itertools.takewhile`."

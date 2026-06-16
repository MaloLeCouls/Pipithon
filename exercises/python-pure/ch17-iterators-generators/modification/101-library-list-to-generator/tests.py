import ast
import collections.abc as abc
import inspect

from solution_user import Loan, overdue_isbns


def make_loans() -> list[Loan]:
    return [
        Loan("978-001", due_date=10),
        Loan("978-002", due_date=25),
        Loan("978-003", due_date=15),
    ]


def test_behavior_filters_overdue():
    assert list(overdue_isbns(make_loans(), today=20)) == ["978-001", "978-003"]


def test_behavior_empty_input():
    assert list(overdue_isbns([], today=100)) == []


def test_behavior_order_preserved():
    assert list(overdue_isbns(make_loans(), today=100)) == ["978-001", "978-002", "978-003"]


def test_form_returns_iterator_not_list():
    result = overdue_isbns(make_loans(), today=20)
    assert isinstance(result, abc.Iterator)
    assert not isinstance(result, list)


def test_form_uses_yield():
    tree = ast.parse(inspect.getsource(overdue_isbns))
    assert any(isinstance(n, (ast.Yield, ast.YieldFrom)) for n in ast.walk(tree)), \
        "Utilise `yield` plutôt qu'un accumulator."

import collections.abc as abc

from solution_user import Loan, iter_overdue


def make_loans() -> list[Loan]:
    return [
        Loan("978-001", due_date=10),
        Loan("978-002", due_date=25),
        Loan("978-003", due_date=15),
        Loan("978-004", due_date=30),
    ]


def test_yields_only_overdue():
    isbns = [loan.isbn for loan in iter_overdue(make_loans(), today=20)]
    assert isbns == ["978-001", "978-003"]


def test_returns_iterator():
    result = iter_overdue(make_loans(), today=20)
    assert isinstance(result, abc.Iterator)


def test_yields_loan_objects_not_isbns():
    first = next(iter_overdue(make_loans(), today=20))
    assert isinstance(first, Loan)
    assert first.isbn == "978-001"
    assert first.due_date == 10


def test_empty_input_yields_nothing():
    assert list(iter_overdue([], today=100)) == []


def test_boundary_strict_less_than():
    loans = [Loan("a", due_date=20), Loan("b", due_date=19)]
    out = [loan.isbn for loan in iter_overdue(loans, today=20)]
    assert out == ["b"]

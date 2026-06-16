from solution_user import Loan, overdue_summary


def make_loans() -> list[Loan]:
    return [
        Loan("978-001", due_date=10),
        Loan("978-002", due_date=25),
        Loan("978-003", due_date=15),
    ]


def test_count_and_isbns_consistent():
    count, isbns = overdue_summary(make_loans(), today=20)
    assert count == 2
    assert isbns == ["978-001", "978-003"]


def test_no_overdue():
    count, isbns = overdue_summary(make_loans(), today=0)
    assert count == 0
    assert isbns == []


def test_all_overdue():
    count, isbns = overdue_summary(make_loans(), today=100)
    assert count == 3
    assert isbns == ["978-001", "978-002", "978-003"]


def test_empty_loans():
    assert overdue_summary([], today=50) == (0, [])


def test_count_matches_len_isbns():
    # Edge case : invariant fondamental — count == len(isbns) toujours.
    count, isbns = overdue_summary(make_loans(), today=20)
    assert count == len(isbns)

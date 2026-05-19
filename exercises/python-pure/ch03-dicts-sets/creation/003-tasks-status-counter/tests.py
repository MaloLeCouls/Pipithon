from collections import Counter

from solution_user import count_status

TASKS = [
    {"id": "1", "status": "todo"},
    {"id": "2", "status": "done"},
    {"id": "3", "status": "todo"},
]


def test_counts():
    c = count_status(TASKS)
    assert c["todo"] == 2
    assert c["done"] == 1


def test_returns_counter():
    assert isinstance(count_status(TASKS), Counter)


def test_empty():
    assert count_status([]) == Counter()


def test_absent_status_is_zero():
    # edge : Counter renvoie 0, pas KeyError
    assert count_status(TASKS)["blocked"] == 0

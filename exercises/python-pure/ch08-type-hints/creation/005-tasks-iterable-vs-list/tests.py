import inspect

from solution_user import count_at_priority


def test_counts_matching_priority_from_list():
    tasks = [{"priority": 1}, {"priority": 2}, {"priority": 1}]
    assert count_at_priority(tasks, 1) == 2


def test_accepts_generator():
    gen = (t for t in [{"priority": 1}, {"priority": 1}])
    assert count_at_priority(gen, 1) == 2


def test_accepts_tuple():
    tasks = ({"priority": 1}, {"priority": 2})
    assert count_at_priority(tasks, 2) == 1


def test_empty_iterable():
    assert count_at_priority([], 1) == 0


def test_param_annotated_with_iterable():
    sig = inspect.signature(count_at_priority)
    ann = str(sig.parameters["tasks"].annotation)
    assert "Iterable" in ann, f"utilise Iterable, pas list ({ann})"

from solution_user import Task, bulk_close


def make_tasks() -> dict[str, Task]:
    return {tid: Task(tid) for tid in ["A", "B", "C", "D"]}


def test_removes_existing():
    tasks = make_tasks()
    bulk_close(tasks, ["A", "C"])
    assert set(tasks) == {"B", "D"}


def test_ignores_missing_silently():
    tasks = make_tasks()
    bulk_close(tasks, ["X", "Y", "Z"])  # aucun existe
    assert set(tasks) == {"A", "B", "C", "D"}


def test_mix_existing_and_missing():
    tasks = make_tasks()
    bulk_close(tasks, ["A", "X", "B", "Z"])
    assert set(tasks) == {"C", "D"}


def test_empty_ids():
    tasks = make_tasks()
    bulk_close(tasks, [])
    assert set(tasks) == {"A", "B", "C", "D"}


def test_other_exception_propagates():
    # Edge : suppress ne doit avaler QUE KeyError. Un mapping qui lève autre
    # chose remonte normalement.
    import pytest

    class Picky(dict):
        def pop(self, key, *args):  # type: ignore[override]
            raise ValueError(f"refuse {key}")

    with pytest.raises(ValueError):
        bulk_close(Picky({"A": Task("A")}), ["A"])

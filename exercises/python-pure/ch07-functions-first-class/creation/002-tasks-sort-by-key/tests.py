from solution_user import Task, by_priority


def test_sorts_ascending_by_priority():
    tasks = [Task("c", 3), Task("a", 1), Task("b", 2)]
    out = by_priority(tasks)
    assert [t.title for t in out] == ["a", "b", "c"]


def test_does_not_mutate_input():
    tasks = [Task("c", 3), Task("a", 1), Task("b", 2)]
    by_priority(tasks)
    assert [t.title for t in tasks] == ["c", "a", "b"]


def test_returns_distinct_list():
    tasks = [Task("a", 1)]
    assert by_priority(tasks) is not tasks


def test_empty_input():
    assert by_priority([]) == []


def test_stable_sort_preserves_relative_order():
    # python's sort est stable : éléments de même priorité gardent leur ordre.
    tasks = [Task("a", 1), Task("b", 1), Task("c", 1)]
    assert [t.title for t in by_priority(tasks)] == ["a", "b", "c"]

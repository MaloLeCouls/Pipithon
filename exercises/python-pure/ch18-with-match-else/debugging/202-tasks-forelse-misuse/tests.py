from solution_user import Task, first_assignee_or_unassigned


def make_tasks() -> list[Task]:
    return [
        Task("T1", "todo", "alice"),
        Task("T2", "doing", "bob"),
        Task("T3", "doing", "carol"),
        Task("T4", "done", "dave"),
    ]


def test_finds_first_matching():
    assert first_assignee_or_unassigned(make_tasks(), "doing") == "bob"


def test_returns_unassigned_when_no_match():
    assert first_assignee_or_unassigned(make_tasks(), "blocked") == "unassigned"


def test_returns_unassigned_for_empty_list():
    assert first_assignee_or_unassigned([], "todo") == "unassigned"


def test_returns_first_not_last():
    tasks = [
        Task("T1", "todo", "alice"),
        Task("T2", "todo", "bob"),
    ]
    assert first_assignee_or_unassigned(tasks, "todo") == "alice"


def test_match_at_end_of_list():
    tasks = [
        Task("T1", "todo", "alice"),
        Task("T2", "done", "bob"),
    ]
    assert first_assignee_or_unassigned(tasks, "done") == "bob"

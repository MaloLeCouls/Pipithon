from solution_user import Sprint


def test_len_counts_tasks():
    assert len(Sprint("S1", ["a", "b", "c"])) == 3


def test_repr_format():
    assert repr(Sprint("S1", ["a", "b", "c"])) == "Sprint('S1', 3 tasks)"


def test_repr_uses_len():
    s = Sprint("S2", ["x"])
    assert f"{len(s)} tasks" in repr(s)


def test_name_is_quoted_in_repr():
    assert repr(Sprint("Backlog", []))[:16] == "Sprint('Backlog'"


def test_empty_sprint_does_not_crash():
    # edge case : sprint vide -> 0 tasks, pas d'exception
    s = Sprint("S0", [])
    assert len(s) == 0
    assert repr(s) == "Sprint('S0', 0 tasks)"

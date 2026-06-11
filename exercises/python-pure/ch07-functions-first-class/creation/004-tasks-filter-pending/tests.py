from solution_user import pending


def test_filters_done_out():
    tasks = [
        {"title": "a", "status": "todo"},
        {"title": "b", "status": "done"},
        {"title": "c", "status": "doing"},
    ]
    assert pending(tasks) == [
        {"title": "a", "status": "todo"},
        {"title": "c", "status": "doing"},
    ]


def test_all_done_returns_empty():
    tasks = [{"title": "x", "status": "done"}]
    assert pending(tasks) == []


def test_none_done_returns_all():
    tasks = [{"title": "x", "status": "todo"}, {"title": "y", "status": "doing"}]
    assert pending(tasks) == tasks


def test_does_not_mutate_input():
    tasks = [{"title": "a", "status": "todo"}, {"title": "b", "status": "done"}]
    pending(tasks)
    assert len(tasks) == 2


def test_returns_a_list_not_iterator():
    # filter() seul renvoie un iterator. On veut une list.
    out = pending([{"title": "x", "status": "todo"}])
    assert isinstance(out, list)

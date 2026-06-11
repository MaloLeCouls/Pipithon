from solution_user import Worker, make_workers


def test_workers_have_distinct_pending_lists():
    workers = make_workers(3)
    assert workers[0].pending is not workers[1].pending
    assert workers[1].pending is not workers[2].pending


def test_enqueue_does_not_leak_between_workers():
    workers = make_workers(3)
    workers[0].enqueue("T1")
    assert workers[1].pending == []
    assert workers[2].pending == []


def test_each_worker_keeps_its_id():
    workers = make_workers(4)
    assert [w.worker_id for w in workers] == [0, 1, 2, 3]


def test_explicit_pending_still_works():
    w = Worker(99, ["seed"])
    w.enqueue("T")
    assert w.pending == ["seed", "T"]


def test_empty_make_workers():
    assert make_workers(0) == []

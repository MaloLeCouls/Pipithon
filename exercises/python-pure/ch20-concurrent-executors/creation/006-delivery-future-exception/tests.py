from solution_user import deliver_all


def test_all_ok():
    ok, failed = deliver_all(["TRK-1", "TRK-2", "TRK-3"])
    assert sorted(ok) == ["TRK-1", "TRK-2", "TRK-3"]
    assert failed == []


def test_all_failed():
    ok, failed = deliver_all(["BAD-1", "BAD-2"])
    assert ok == []
    assert sorted(failed) == ["BAD-1", "BAD-2"]


def test_mixed():
    ok, failed = deliver_all(["TRK-1", "BAD-X", "TRK-2"])
    assert sorted(ok) == ["TRK-1", "TRK-2"]
    assert failed == ["BAD-X"]


def test_empty():
    ok, failed = deliver_all([])
    assert ok == [] and failed == []

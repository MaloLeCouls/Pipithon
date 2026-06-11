from solution_user import log_trip


def test_two_calls_do_not_share_log():
    a = log_trip("X1")
    b = log_trip("X2")
    assert a == ["X1"]
    assert b == ["X2"]


def test_explicit_log_preserved():
    log: list[str] = ["initial"]
    out = log_trip("Y1", log)
    assert out == ["initial", "Y1"]


def test_explicit_log_returned_is_same_object():
    log: list[str] = []
    out = log_trip("Z", log)
    assert out is log


def test_repeated_default_calls_stay_isolated():
    # edge case : 10 appels sans log, chacun doit avoir un seul élément.
    results = [log_trip(f"P{i}") for i in range(10)]
    for i, r in enumerate(results):
        assert r == [f"P{i}"], f"appel {i} a vu d'autres logs : {r}"

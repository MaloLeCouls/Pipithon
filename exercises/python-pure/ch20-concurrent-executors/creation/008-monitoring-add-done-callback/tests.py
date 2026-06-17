from solution_user import count_outcomes


def test_all_ok():
    ok, failed = count_outcomes(["cpu", "mem", "disk"])
    assert ok == 3
    assert failed == 0


def test_all_failed():
    ok, failed = count_outcomes(["bad", "bad", "bad"])
    assert ok == 0
    assert failed == 3


def test_mixed():
    ok, failed = count_outcomes(["cpu", "bad", "mem", "bad"])
    assert ok == 2
    assert failed == 2


def test_empty():
    ok, failed = count_outcomes([])
    assert ok == 0 and failed == 0

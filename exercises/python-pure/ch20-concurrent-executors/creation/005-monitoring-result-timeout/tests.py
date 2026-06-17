from solution_user import sample_with_timeout


def test_fast_probe_succeeds():
    # sleep court < timeout : renvoie la longueur
    assert sample_with_timeout("cpu", 0.001, timeout=0.1) == 3


def test_slow_probe_returns_sentinel():
    # sleep long > timeout : renvoie -1
    assert sample_with_timeout("disk", 0.1, timeout=0.01) == -1


def test_zero_sleep_returns_real():
    assert sample_with_timeout("io", 0.0, timeout=0.5) == 2

from solution_user import Metric, first_critical


def test_finds_first_above_threshold():
    metrics = [Metric("cpu", 0.4), Metric("mem", 0.95), Metric("disk", 0.8)]
    assert first_critical(metrics, threshold=0.9, default="none") == "mem"


def test_returns_default_when_none_above():
    metrics = [Metric("cpu", 0.4), Metric("mem", 0.5)]
    assert first_critical(metrics, threshold=0.9, default="ok") == "ok"


def test_returns_default_for_empty_list():
    assert first_critical([], threshold=0.9, default="empty") == "empty"


def test_strict_inequality():
    # value == threshold -> NON critique (strict >).
    metrics = [Metric("cpu", 0.9), Metric("mem", 0.91)]
    assert first_critical(metrics, threshold=0.9, default="ok") == "mem"


def test_returns_first_not_any():
    metrics = [Metric("a", 1.0), Metric("b", 2.0), Metric("c", 3.0)]
    assert first_critical(metrics, threshold=0.5, default="x") == "a"

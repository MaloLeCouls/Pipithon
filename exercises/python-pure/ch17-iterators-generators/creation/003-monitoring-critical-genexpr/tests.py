import collections.abc as abc

from solution_user import Metric, critical_alerts


def make_metrics() -> list[Metric]:
    return [
        Metric("cpu", 0.4, "info"),
        Metric("mem", 0.9, "critical"),
        Metric("disk", 0.7, "warning"),
        Metric("net", 0.99, "critical"),
    ]


def test_yields_only_critical():
    names = [m.name for m in critical_alerts(make_metrics())]
    assert names == ["mem", "net"]


def test_returns_iterator():
    result = critical_alerts(make_metrics())
    assert isinstance(result, abc.Iterator)


def test_returns_generator_not_list():
    # Une liste serait `list[Metric]` ; ici on attend un iterator paresseux.
    result = critical_alerts(make_metrics())
    assert not isinstance(result, list)


def test_empty_yields_nothing():
    assert list(critical_alerts([])) == []


def test_no_critical_yields_nothing():
    metrics = [Metric("a", 1.0, "info"), Metric("b", 2.0, "warning")]
    assert list(critical_alerts(metrics)) == []

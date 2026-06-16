import ast
import collections.abc as abc
import inspect

import solution_user
from solution_user import Metric, metric_stream


def make_metrics() -> list[Metric]:
    return [
        Metric("cpu", "info"),
        Metric("mem", "critical"),
        Metric("disk", "warning"),
        Metric("net", "critical"),
    ]


def test_behavior_filters_critical():
    names = [m.name for m in metric_stream(make_metrics(), "critical")]
    assert names == ["mem", "net"]


def test_behavior_filters_warning():
    names = [m.name for m in metric_stream(make_metrics(), "warning")]
    assert names == ["disk"]


def test_behavior_empty():
    assert list(metric_stream([], "critical")) == []


def test_form_returns_iterator():
    assert isinstance(metric_stream(make_metrics(), "info"), abc.Iterator)


def test_form_no_metricstream_class():
    # Le coeur du refactor : la classe doit disparaître.
    assert not hasattr(solution_user, "MetricStream"), \
        "Supprime la classe MetricStream — un générateur suffit."


def test_form_uses_yield():
    tree = ast.parse(inspect.getsource(metric_stream))
    assert any(isinstance(n, (ast.Yield, ast.YieldFrom)) for n in ast.walk(tree))

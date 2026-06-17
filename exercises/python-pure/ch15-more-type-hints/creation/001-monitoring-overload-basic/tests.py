from solution_user import format_metric


def test_int_no_unit():
    assert format_metric(42) == "42"


def test_float_with_ms_unit():
    assert format_metric(1.5) == "1.5ms"


def test_int_zero():
    assert format_metric(0) == "0"


def test_float_zero():
    assert format_metric(0.0) == "0.0ms"


def test_overloads_registered():
    """`format_metric` doit avoir au moins 2 stubs @overload enregistrés."""
    from typing import get_overloads
    overloads = get_overloads(format_metric)
    assert len(overloads) >= 2

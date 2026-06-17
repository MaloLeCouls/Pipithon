from collections.abc import Iterable, Sized

from solution_user import MetricWindow


def test_len_works():
    assert len(MetricWindow([1.0, 2.0, 3.0])) == 3


def test_iter_yields_values_in_order():
    w = MetricWindow([0.1, 0.2, 0.3])
    assert list(w) == [0.1, 0.2, 0.3]


def test_isinstance_sized():
    assert isinstance(MetricWindow([]), Sized)


def test_isinstance_iterable():
    assert isinstance(MetricWindow([]), Iterable)


def test_iter_is_independent_per_call():
    """Deux for indépendants ne se gênent pas (MetricWindow est itérable, pas iterator)."""
    w = MetricWindow([1.0, 2.0])
    a = list(w)
    b = list(w)
    assert a == b == [1.0, 2.0]


def test_empty_window():
    w = MetricWindow([])
    assert len(w) == 0
    assert list(w) == []

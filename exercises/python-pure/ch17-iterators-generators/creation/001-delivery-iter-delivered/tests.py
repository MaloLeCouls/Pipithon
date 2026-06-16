import collections.abc as abc

from solution_user import Package, iter_delivered


def make_pkgs() -> list[Package]:
    return [
        Package("TRK-1", "in_transit"),
        Package("TRK-2", "delivered"),
        Package("TRK-3", "pending"),
        Package("TRK-4", "delivered"),
    ]


def test_yields_only_delivered():
    assert list(iter_delivered(make_pkgs())) == ["TRK-2", "TRK-4"]


def test_returns_an_iterator_not_a_list():
    result = iter_delivered(make_pkgs())
    assert isinstance(result, abc.Iterator)
    assert not isinstance(result, list)


def test_is_lazy_does_not_consume_eagerly():
    seen: list[str] = []

    def spy():
        for p in make_pkgs():
            seen.append(p.tracking_id)
            yield p

    gen = iter_delivered(spy())
    assert seen == []
    next(gen)
    assert "TRK-2" in seen


def test_empty_input_yields_nothing():
    assert list(iter_delivered([])) == []


def test_no_delivered_yields_nothing():
    pkgs = [Package("a", "pending"), Package("b", "in_transit")]
    assert list(iter_delivered(pkgs)) == []

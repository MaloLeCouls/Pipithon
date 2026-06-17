import pytest

from solution_user import Metric


def test_default_unit_is_ms():
    assert Metric.UNIT == "ms"
    assert Metric("latency", 1.0).UNIT == "ms"


def test_instance_override_does_not_change_class():
    m = Metric("x", 1.0)
    m.UNIT = "ns"  # type: ignore[misc]
    assert m.UNIT == "ns"
    assert Metric.UNIT == "ms", "L'override par instance ne doit PAS toucher Metric.UNIT."


def test_reset_unit_changes_class_attr():
    # On sauvegarde + restore pour ne pas polluer les autres tests.
    original = Metric.UNIT
    try:
        Metric.reset_unit("us")
        assert Metric.UNIT == "us"
        assert Metric("y", 1.0).UNIT == "us"  # toutes les futures instances voient
    finally:
        Metric.UNIT = original


def test_bump_increments():
    m = Metric("x", 1.0)
    assert m.bump() == 1
    assert m.bump() == 2
    assert m.bump() == 3


def test_name_mangling_hides_count():
    m = Metric("x", 1.0)
    with pytest.raises(AttributeError):
        m.__count  # type: ignore[attr-defined]


def test_mangled_name_exists():
    m = Metric("x", 1.0)
    m.bump()
    # Le name mangling produit `_Metric__count`. C'est documenté, pas un secret.
    assert getattr(m, "_Metric__count") == 1

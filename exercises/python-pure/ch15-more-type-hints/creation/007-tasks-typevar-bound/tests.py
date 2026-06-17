import pytest

from solution_user import Comparable, max_priority


def test_max_ints():
    assert max_priority([1, 3, 2]) == 3


def test_max_strs():
    assert max_priority(["a", "z", "m"]) == "z"


def test_max_floats():
    assert max_priority([0.5, 1.2, -3.0]) == 1.2


def test_max_empty_raises():
    with pytest.raises(ValueError):
        max_priority([])


def test_comparable_has_lt():
    assert hasattr(Comparable, "__lt__")

import math

import pytest

from solution_user import Embedding2d


def test_iter_and_unpack():
    e = Embedding2d(3, 4)
    x, y = e
    assert (x, y) == (3.0, 4.0)


def test_repr_roundtrip():
    e = Embedding2d(1.5, 2.5)
    assert repr(e) == "Embedding2d(1.5, 2.5)"
    reconstructed = eval(repr(e), {"Embedding2d": Embedding2d})
    assert reconstructed == e


def test_str_format():
    assert str(Embedding2d(1, 2)) == "(1.0, 2.0)"


def test_eq_by_value():
    assert Embedding2d(1, 2) == Embedding2d(1, 2)
    assert Embedding2d(1, 2) != Embedding2d(2, 1)


def test_hash_consistent_with_eq():
    assert hash(Embedding2d(3, 4)) == hash(Embedding2d(3, 4))
    s = {Embedding2d(1, 2), Embedding2d(1, 2)}
    assert len(s) == 1


def test_abs_is_euclidean_norm():
    assert abs(Embedding2d(3, 4)) == 5.0


def test_bool_false_for_zero_vector():
    assert bool(Embedding2d(0, 0)) is False
    assert bool(Embedding2d(0, 1)) is True


def test_format_default():
    assert format(Embedding2d(1, 2)) == "(1.0, 2.0)"


def test_format_polar():
    f = format(Embedding2d(1, 0), "p")
    assert f.startswith("<")
    assert "1.0" in f


def test_format_unknown_spec_raises():
    with pytest.raises(ValueError):
        format(Embedding2d(1, 2), "bogus")


def test_attributes_are_readonly():
    e = Embedding2d(1, 2)
    with pytest.raises(AttributeError):
        e.x = 3  # type: ignore[misc]


def test_from_pair_classmethod():
    e = Embedding2d.from_pair((5.0, 6.0))
    assert e.x == 5.0
    assert e.y == 6.0


def test_from_pair_polymorphic():
    class Tagged(Embedding2d):
        pass

    t = Tagged.from_pair((1.0, 2.0))
    assert type(t) is Tagged


def test_slots_no_dict():
    assert not hasattr(Embedding2d(1, 2), "__dict__")

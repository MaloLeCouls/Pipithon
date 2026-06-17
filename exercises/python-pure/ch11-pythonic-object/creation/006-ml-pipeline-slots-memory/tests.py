import pytest

from solution_user import Sample


def test_basic_attributes():
    s = Sample("cat", [0.1, 0.9])
    assert s.label == "cat"
    assert s.features == [0.1, 0.9]


def test_no_dict():
    s = Sample("x", [])
    assert not hasattr(s, "__dict__"), \
        "__slots__ doit supprimer __dict__ — sinon pas d'économie mémoire."


def test_extra_attr_raises():
    s = Sample("x", [])
    with pytest.raises(AttributeError):
        s.metadata = {}  # type: ignore[attr-defined]


def test_typo_in_attr_raises():
    s = Sample("x", [])
    with pytest.raises(AttributeError):
        s.lable = "y"  # type: ignore[attr-defined]


def test_slots_declared():
    assert hasattr(Sample, "__slots__")
    assert "label" in Sample.__slots__
    assert "features" in Sample.__slots__

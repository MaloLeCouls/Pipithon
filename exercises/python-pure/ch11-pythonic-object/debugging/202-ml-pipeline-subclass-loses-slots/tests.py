import pytest

from solution_user import Sample, TaggedSample


def test_tagged_sample_no_dict():
    ts = TaggedSample("cat", [0.1], "train")
    assert not hasattr(ts, "__dict__"), \
        "Sans `__slots__` sur la sous-classe, `__dict__` réapparaît."


def test_tagged_sample_basic_attributes():
    ts = TaggedSample("cat", [0.1, 0.2], "train")
    assert ts.label == "cat"
    assert ts.features == [0.1, 0.2]
    assert ts.split == "train"


def test_extra_attr_raises_on_tagged():
    ts = TaggedSample("cat", [], "train")
    with pytest.raises(AttributeError):
        ts.unexpected = 1  # type: ignore[attr-defined]


def test_parent_still_slotted():
    s = Sample("x", [])
    assert not hasattr(s, "__dict__")


def test_taggedsample_slots_includes_split():
    assert "split" in TaggedSample.__slots__

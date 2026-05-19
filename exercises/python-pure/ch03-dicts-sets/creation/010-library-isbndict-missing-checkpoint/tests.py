import pytest

from solution_user import IsbnDict


def make():
    d = IsbnDict()
    d["978"] = "Dune"
    d["451"] = "Fahrenheit 451"
    return d


def test_str_key_direct():
    assert make()["978"] == "Dune"


def test_int_key_falls_back_to_str():
    assert make()[978] == "Dune"


def test_missing_str_raises_keyerror():
    with pytest.raises(KeyError):
        make()["000"]


def test_missing_int_raises_keyerror_no_infinite_recursion():
    with pytest.raises(KeyError):
        make()[999]


def test_get_is_type_tolerant():
    d = make()
    assert d.get(978) == "Dune"
    assert d.get("978") == "Dune"
    assert d.get(999) is None
    assert d.get(999, "?") == "?"


def test_contains_both_forms():
    d = make()
    assert 978 in d
    assert "978" in d
    assert 999 not in d


def test_contains_consistent_with_getitem():
    # edge/checkpoint : `in` et d[k] ne doivent jamais se contredire
    d = make()
    for key in (978, "978", 451, "451"):
        assert (key in d) is True
        assert d[key] is not None

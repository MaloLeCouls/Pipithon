import pytest

from solution_user import clean_title


def test_str_input():
    assert clean_title("  Dune  ") == "Dune"


def test_bytes_input():
    assert clean_title(b"  Caf\xc3\xa9 ") == "Café"


def test_str_passthrough_unicode():
    assert clean_title("Café") == "Café"


def test_returns_str_for_bytes():
    assert isinstance(clean_title(b"x"), str)


def test_invalid_type_raises():
    with pytest.raises(TypeError, match="str ou bytes"):
        clean_title(42)


def test_empty_and_whitespace_only():
    # edge
    assert clean_title("") == ""
    assert clean_title(b"   ") == ""

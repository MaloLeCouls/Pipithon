import pytest

from solution_user import Table, reservation_window


def test_reserved_inside_block():
    t = Table("T1")
    with reservation_window(t):
        assert t.reserved is True


def test_released_after_block():
    t = Table("T1")
    with reservation_window(t):
        pass
    assert t.reserved is False


def test_yields_table():
    t = Table("T1")
    with reservation_window(t) as got:
        assert got is t


def test_released_after_exception():
    t = Table("T1")
    with pytest.raises(RuntimeError):
        with reservation_window(t):
            raise RuntimeError("kitchen on fire")
    assert t.reserved is False


def test_independent_calls():
    a = Table("A")
    b = Table("B")
    with reservation_window(a):
        with reservation_window(b):
            assert a.reserved is True
            assert b.reserved is True
        assert b.reserved is False
        assert a.reserved is True
    assert a.reserved is False

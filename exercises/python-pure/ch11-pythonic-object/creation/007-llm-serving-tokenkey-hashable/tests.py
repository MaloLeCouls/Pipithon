import pytest

from solution_user import TokenKey


def test_basic_construction():
    k = TokenKey((1, 2, 3), 42)
    assert k._prefix == (1, 2, 3)
    assert k._seq_id == 42


def test_equal_keys_equal_hash():
    a = TokenKey((1, 2), 7)
    b = TokenKey((1, 2), 7)
    assert a == b
    assert hash(a) == hash(b)


def test_different_prefix_not_equal():
    assert TokenKey((1,), 7) != TokenKey((2,), 7)


def test_different_seq_id_not_equal():
    assert TokenKey((1,), 7) != TokenKey((1,), 8)


def test_usable_as_dict_key():
    cache = {TokenKey((1, 2), 0): "block_42"}
    assert cache[TokenKey((1, 2), 0)] == "block_42"


def test_immutable_setattr_after_init():
    k = TokenKey((1,), 0)
    with pytest.raises(AttributeError):
        k._prefix = (2,)  # type: ignore[misc]
    with pytest.raises(AttributeError):
        k._seq_id = 999  # type: ignore[misc]


def test_no_dict_attribute():
    k = TokenKey((1,), 0)
    assert not hasattr(k, "__dict__")


def test_slots_declared():
    assert TokenKey.__slots__ == ("_prefix", "_seq_id")

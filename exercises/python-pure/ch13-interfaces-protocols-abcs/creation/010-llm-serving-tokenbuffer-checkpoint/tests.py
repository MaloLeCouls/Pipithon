import pytest

from solution_user import FIFOBuffer, ListBuffer, RandomBuffer, TokenBuffer


def test_tokenbuffer_is_abstract():
    with pytest.raises(TypeError):
        TokenBuffer()  # type: ignore[abstract]


def test_random_buffer_load_and_pick_drains():
    b = RandomBuffer(seed=42)
    b.load([1, 2, 3])
    out = sorted([b.pick(), b.pick(), b.pick()])
    assert out == [1, 2, 3]
    with pytest.raises(LookupError):
        b.pick()


def test_random_buffer_loaded_inspect_via_default_impl():
    b = RandomBuffer(seed=0)
    assert b.loaded() is False
    b.load([10, 20])
    assert b.loaded() is True
    assert b.inspect() == (10, 20)
    # inspect ne doit pas vider le buffer (il recharge).
    assert b.loaded() is True


def test_fifo_buffer_pop_order():
    f = FIFOBuffer()
    f.load([1, 2, 3])
    assert f.pick() == 1
    assert f.pick() == 2
    assert f.pick() == 3


def test_fifo_buffer_overrides_loaded():
    f = FIFOBuffer()
    assert f.loaded() is False
    f.load([7])
    assert f.loaded() is True


def test_list_buffer_is_virtual_subclass():
    assert isinstance(ListBuffer([1, 2]), TokenBuffer)
    assert issubclass(ListBuffer, TokenBuffer)
    # MAIS : pas dans le MRO, c'est juste un register.
    assert TokenBuffer not in ListBuffer.__mro__


def test_list_buffer_load_and_pick():
    lb = ListBuffer()
    lb.load([5, 10, 15])
    assert lb.pick() == 15  # list.pop pop le dernier
    assert lb.pick() == 10
    assert lb.pick() == 5
    with pytest.raises(LookupError):
        lb.pick()


def test_tokenbuffer_has_load_pick_abstract():
    assert "load" in TokenBuffer.__abstractmethods__
    assert "pick" in TokenBuffer.__abstractmethods__

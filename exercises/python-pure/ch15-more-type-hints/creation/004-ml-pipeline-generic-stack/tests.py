import pytest

from solution_user import Stack


def test_push_then_len():
    s: Stack[int] = Stack()
    s.push(1)
    s.push(2)
    assert len(s) == 2


def test_pop_lifo_order():
    s: Stack[str] = Stack()
    s.push("a")
    s.push("b")
    assert s.pop() == "b"
    assert s.pop() == "a"


def test_peek_does_not_pop():
    s: Stack[int] = Stack()
    s.push(42)
    assert s.peek() == 42
    assert len(s) == 1  # toujours là


def test_pop_empty_raises():
    s: Stack[int] = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_works_with_any_type():
    s: Stack[list[int]] = Stack()
    s.push([1, 2])
    assert s.pop() == [1, 2]


def test_class_is_generic():
    # Stack doit accepter le bracket : Stack[int] est légal.
    Stack[int]  # ne doit pas lever

import pytest

from solution_user import LRUCache


def test_put_then_get():
    c: LRUCache[str, int] = LRUCache(capacity=2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1
    assert c.get("b") == 2


def test_get_missing_returns_none():
    c: LRUCache[str, int] = LRUCache(capacity=2)
    assert c.get("nope") is None


def test_eviction_when_capacity_exceeded():
    c: LRUCache[str, int] = LRUCache(capacity=2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)  # évince "a" (le plus ancien)
    assert c.get("a") is None
    assert c.get("b") == 2
    assert c.get("c") == 3


def test_get_promotes_to_most_recent():
    c: LRUCache[str, int] = LRUCache(capacity=2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")  # promote a
    c.put("c", 3)  # devrait évincer b, pas a
    assert "a" in c
    assert "b" not in c
    assert "c" in c


def test_overwrite_updates_value_and_recency():
    c: LRUCache[str, int] = LRUCache(capacity=2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 10)  # override + promote
    c.put("c", 3)  # évince b
    assert c.get("a") == 10
    assert c.get("b") is None
    assert c.get("c") == 3


def test_capacity_zero_invalid():
    with pytest.raises(ValueError):
        LRUCache(capacity=0)


def test_capacity_negative_invalid():
    with pytest.raises(ValueError):
        LRUCache(capacity=-1)


def test_len():
    c: LRUCache[int, str] = LRUCache(capacity=3)
    assert len(c) == 0
    c.put(1, "a")
    c.put(2, "b")
    assert len(c) == 2


def test_contains():
    c: LRUCache[int, str] = LRUCache(capacity=2)
    c.put(1, "a")
    assert 1 in c
    assert 2 not in c


def test_class_is_generic():
    LRUCache[str, int]  # ne doit pas lever
    LRUCache[tuple[int, ...], list[float]]


def test_works_with_tuple_keys():
    c: LRUCache[tuple[int, int], str] = LRUCache(capacity=2)
    c.put((1, 2), "pair")
    assert c.get((1, 2)) == "pair"

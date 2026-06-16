import pytest

from pymistral import KVCache, Token
from solution_user import inference_context


def test_cache_starts_empty_inside_block():
    cache = KVCache(num_layers=2)
    cache.append(0, Token(id=1, text="x"))  # cache « sale » avant
    with inference_context(cache) as c:
        assert len(c) == 0


def test_cache_empty_after_block():
    cache = KVCache(num_layers=2)
    with inference_context(cache) as c:
        c.append(0, Token(id=0, text="a"))
        c.append(1, Token(id=1, text="b"))
        assert len(c) == 2
    assert len(cache) == 0


def test_yields_the_cache():
    cache = KVCache(num_layers=1)
    with inference_context(cache) as c:
        assert c is cache


def test_cleanup_on_exception():
    cache = KVCache(num_layers=1)
    with pytest.raises(RuntimeError):
        with inference_context(cache) as c:
            c.append(0, Token(id=0, text="x"))
            raise RuntimeError("oom")
    assert len(cache) == 0


def test_exception_not_swallowed():
    cache = KVCache(num_layers=1)
    with pytest.raises(ValueError):
        with inference_context(cache):
            raise ValueError("bad logits")

from solution_user import Cache, DictCache


def test_set_then_get():
    c = DictCache()
    c.set("hello", "world")
    assert c.get("hello") == "world"


def test_get_missing_returns_none():
    c = DictCache()
    assert c.get("missing") is None


def test_set_overwrites():
    c = DictCache()
    c.set("k", 1)
    c.set("k", 2)
    assert c.get("k") == 2


def test_cache_is_generic_protocol():
    """Cache doit être un Protocol générique paramétrable."""
    Cache[int, str]  # ne doit pas lever : Protocol générique paramétrable
    Cache[str, list]  # idem


def test_dictcache_supports_int_keys():
    c = DictCache()
    c.set(42, "answer")
    assert c.get(42) == "answer"


def test_dictcache_supports_tuple_keys():
    c = DictCache()
    c.set((1, 2), "pair")
    assert c.get((1, 2)) == "pair"

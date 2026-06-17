from solution_user import batch_hashes, hash_with_factor


def test_basic():
    result = batch_hashes(["a", "ab"], factor=3)
    expected = [hash_with_factor("a", 3), hash_with_factor("ab", 3)]
    assert result == expected


def test_empty():
    assert batch_hashes([], factor=0) == []


def test_factor_affects_result():
    a = batch_hashes(["x"], factor=1)
    b = batch_hashes(["x"], factor=2)
    assert a != b


def test_no_pickling_error():
    """Le starter lève PicklingError ici."""
    batch_hashes(["a", "b", "c"], factor=7)

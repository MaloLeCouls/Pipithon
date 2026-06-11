from solution_user import CALLS, tokenize_len


def setup_function():
    CALLS[0] = 0
    tokenize_len.cache_clear()


def test_correct_length():
    assert tokenize_len("abc") == 3


def test_same_input_not_recomputed():
    tokenize_len("hello")
    tokenize_len("hello")
    tokenize_len("hello")
    assert CALLS[0] == 1


def test_different_inputs_each_compute_once():
    tokenize_len("a")
    tokenize_len("b")
    tokenize_len("a")
    tokenize_len("b")
    assert CALLS[0] == 2


def test_cache_attribute_present():
    # @functools.cache expose cache_info / cache_clear.
    assert hasattr(tokenize_len, "cache_info")
    assert hasattr(tokenize_len, "cache_clear")

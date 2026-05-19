from solution_user import is_expected


def test_matching():
    assert is_expected(b"OK", "OK") is True


def test_not_matching():
    assert is_expected(b"OK", "KO") is False


def test_accented_token():
    assert is_expected("café".encode("utf-8"), "café") is True


def test_returns_bool():
    assert isinstance(is_expected(b"x", "x"), bool)


def test_empty_token_edge():
    assert is_expected(b"", "") is True

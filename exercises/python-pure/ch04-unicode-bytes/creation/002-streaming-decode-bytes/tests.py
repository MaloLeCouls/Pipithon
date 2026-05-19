from solution_user import decode_title


def test_utf8():
    assert decode_title(b"Caf\xc3\xa9", "utf-8") == "Café"


def test_latin1():
    assert decode_title(b"Caf\xe9", "latin-1") == "Café"


def test_ascii():
    assert decode_title(b"Dune", "ascii") == "Dune"


def test_returns_str():
    assert isinstance(decode_title(b"x", "utf-8"), str)


def test_empty():
    # edge
    assert decode_title(b"", "utf-8") == ""

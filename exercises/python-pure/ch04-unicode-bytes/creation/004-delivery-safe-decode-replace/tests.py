from solution_user import safe_decode


def test_valid_utf8():
    assert safe_decode(b"Caf\xc3\xa9") == "Café"


def test_invalid_bytes_replaced():
    out = safe_decode(b"abc\xff\xfedef")
    assert "abc" in out and "def" in out
    assert "�" in out  # caractère de remplacement


def test_never_raises():
    # edge : suite d'octets totalement invalides -> pas d'exception
    safe_decode(b"\xff\xff\xff")


def test_empty():
    assert safe_decode(b"") == ""


def test_returns_str():
    assert isinstance(safe_decode(b"\xff"), str)

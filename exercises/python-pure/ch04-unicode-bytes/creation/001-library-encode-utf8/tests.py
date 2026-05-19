from solution_user import to_utf8


def test_ascii_title():
    assert to_utf8("Dune") == b"Dune"


def test_returns_bytes():
    assert isinstance(to_utf8("x"), bytes)


def test_accented_title_utf8():
    assert to_utf8("Café") == b"Caf\xc3\xa9"


def test_roundtrip():
    assert to_utf8("L'Étranger").decode("utf-8") == "L'Étranger"


def test_empty():
    # edge : titre vide -> bytes vides
    assert to_utf8("") == b""

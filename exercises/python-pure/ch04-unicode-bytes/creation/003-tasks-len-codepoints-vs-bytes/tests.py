from solution_user import sizes


def test_ascii_equal():
    assert sizes("todo") == (4, 4)


def test_accented_differs():
    # "é" = 1 caractère mais 2 octets en UTF-8
    assert sizes("café") == (4, 5)


def test_symbol_codepoint():
    # "✅" (U+2705) = 1 code point, 3 octets UTF-8 ; "ok" = 2 octets
    assert sizes("ok✅") == (3, 5)


def test_empty():
    assert sizes("") == (0, 0)


def test_returns_tuple_of_ints():
    n, b = sizes("x")
    assert isinstance(n, int) and isinstance(b, int)

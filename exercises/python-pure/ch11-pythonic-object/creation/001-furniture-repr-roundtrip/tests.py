from solution_user import Chair


def test_repr_format():
    assert repr(Chair("A1", 99)) == "Chair(ref='A1', price=99)"


def test_repr_uses_double_quotes_or_single():
    r = repr(Chair("DESK-2", 250))
    assert "DESK-2" in r
    assert "250" in r
    assert r.startswith("Chair(")


def test_repr_eval_roundtrip():
    """eval(repr(c)) reconstruit un Chair équivalent (mêmes champs)."""
    c = Chair("SOFA-7B", 1200)
    reconstructed = eval(repr(c), {"Chair": Chair})
    assert reconstructed.ref == c.ref
    assert reconstructed.price == c.price


def test_repr_special_chars_in_ref():
    # !r protège des caractères spéciaux (apostrophes, etc.)
    c = Chair("CH'AIR", 10)
    r = repr(c)
    # Python utilise des doubles quotes si la str contient une simple, ou échappe.
    assert "CH" in r

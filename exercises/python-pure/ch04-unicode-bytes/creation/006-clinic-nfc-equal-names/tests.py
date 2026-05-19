import unicodedata

from solution_user import same_name

PRECOMPOSED = "Zoé"  # 'é' = U+00E9
DECOMPOSED = unicodedata.normalize("NFD", "Zoé")  # 'e' + U+0301


def test_canonically_equivalent_true():
    assert PRECOMPOSED != DECOMPOSED  # vérifie que le piège existe
    assert same_name(PRECOMPOSED, DECOMPOSED) is True


def test_identical_strings():
    assert same_name("Marie", "Marie") is True


def test_different_names_false():
    assert same_name("Zoé", "Zoe") is False


def test_returns_bool():
    assert isinstance(same_name("a", "a"), bool)


def test_empty_strings():
    # edge
    assert same_name("", "") is True

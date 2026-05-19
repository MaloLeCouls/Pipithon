import unicodedata

from solution_user import canonical_key, dedupe


def test_key_equates_case_and_form():
    a = "Café"
    b = unicodedata.normalize("NFD", "café")
    assert canonical_key(a) == canonical_key(b)


def test_dedupe_keeps_first_spelling():
    titles = ["Café", unicodedata.normalize("NFD", "café"), "CAFÉ"]
    assert dedupe(titles) == ["Café"]


def test_dedupe_distinct_titles_kept():
    assert dedupe(["Dune", "Neuromancer"]) == ["Dune", "Neuromancer"]


def test_order_preserved():
    assert dedupe(["B", "a", "b", "A"]) == ["B", "a"]


def test_empty():
    assert dedupe([]) == []


def test_key_is_str():
    assert isinstance(canonical_key("X"), str)

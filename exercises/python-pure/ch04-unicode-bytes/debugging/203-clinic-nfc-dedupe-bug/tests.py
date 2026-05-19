import unicodedata

from solution_user import count_unique


def test_canonical_dupes_collapse():
    composed = "Zoé"
    decomposed = unicodedata.normalize("NFD", "Zoé")
    assert composed != decomposed
    assert count_unique([composed, decomposed]) == 1


def test_distinct_names_counted():
    assert count_unique(["Marie", "Jean", "Marie"]) == 2


def test_all_distinct():
    assert count_unique(["A", "B", "C"]) == 3


def test_empty():
    assert count_unique([]) == 0


def test_mixed_real_and_form_dupes():
    # edge : mélange de vrais distincts et de doublons de forme
    names = ["Zoé", unicodedata.normalize("NFD", "Zoé"), "Léa", "Léa"]
    assert count_unique(names) == 2

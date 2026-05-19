import unicodedata

from solution_user import search


def test_case_insensitive():
    assert search(["Dune", "Neuromancer"], "dune") == ["Dune"]


def test_casefold_beats_lower():
    # 'ß'.lower() == 'ß' ; il faut casefold pour matcher 'ss'
    assert search(["Straße"], "strasse") == ["Straße"]


def test_substring_match():
    assert search(["The Great Gatsby"], "great") == ["The Great Gatsby"]


def test_nfc_robustness():
    composed = "Café Society"
    decomposed_query = unicodedata.normalize("NFD", "café")
    assert search([composed], decomposed_query) == [composed]


def test_order_preserved_and_multiple():
    titles = ["Alpha", "alphabet", "Beta"]
    assert search(titles, "alpha") == ["Alpha", "alphabet"]


def test_no_match_and_empty():
    # edge
    assert search(["Dune"], "xyz") == []
    assert search([], "q") == []

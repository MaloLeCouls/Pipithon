import ast
import inspect

from solution_user import find, search_key


def test_preserved_accent_insensitive_match():
    # comportement d'origine conservé : 'cafe' trouve 'Café'
    assert find(["Café Society", "Dune"], "cafe") == ["Café Society"]


def test_preserved_case_insensitive():
    assert find(["Dune"], "DUNE") == ["Dune"]


def test_now_handles_accents_outside_old_table():
    # 'ñ' n'était pas dans _ACCENTS : l'ancien code ratait
    assert find(["El Niño"], "nino") == ["El Niño"]


def test_now_handles_hard_fold():
    assert find(["Straße"], "strasse") == ["Straße"]


def test_no_hardcoded_accent_table():
    src = inspect.getsource
    tree = ast.parse(src(search_key) + "\n" + src(find))
    has_norm = any(
        isinstance(n, ast.Attribute) and n.attr == "normalize"
        for n in ast.walk(tree)
    )
    has_casefold = any(
        isinstance(n, ast.Attribute) and n.attr == "casefold"
        for n in ast.walk(tree)
    )
    assert has_norm and has_casefold, "utilise normalize NFKD + casefold"


def test_order_preserved_and_no_match():
    assert find(["Alpha", "Beta"], "xyz") == []
    assert find(["B", "a", "A"], "a") == ["a", "A"]

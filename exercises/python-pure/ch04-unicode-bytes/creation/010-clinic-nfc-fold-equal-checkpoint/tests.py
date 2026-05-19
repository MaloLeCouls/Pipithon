import unicodedata

from solution_user import fold_equal, nfc_equal

CAFE_NFC = "café"
CAFE_NFD = unicodedata.normalize("NFD", "café")


def test_precondition_trap_exists():
    assert CAFE_NFC != CAFE_NFD  # le piège est réel


def test_nfc_equal_canonical():
    assert nfc_equal(CAFE_NFC, CAFE_NFD) is True


def test_nfc_equal_case_sensitive():
    assert nfc_equal("Café", "café") is False


def test_nfc_equal_identical():
    assert nfc_equal("Dune", "Dune") is True


def test_fold_equal_ignores_case():
    assert fold_equal("Café", CAFE_NFD) is True


def test_fold_equal_superset_of_nfc_equal():
    # tout ce que nfc_equal accepte, fold_equal l'accepte aussi
    pairs = [(CAFE_NFC, CAFE_NFD), ("Dune", "Dune")]
    for a, b in pairs:
        if nfc_equal(a, b):
            assert fold_equal(a, b)


def test_fold_equal_casefold_not_lower():
    # 'ß'.lower() == 'ß' ; casefold le plie en 'ss'
    assert fold_equal("Straße", "STRASSE") is True


def test_genuinely_different():
    # edge : noms réellement différents -> False des deux côtés
    assert nfc_equal("Zoé", "Zoe") is False
    assert fold_equal("Zoé", "Zoe") is False

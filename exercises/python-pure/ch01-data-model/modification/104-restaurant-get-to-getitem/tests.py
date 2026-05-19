from solution_user import Menu

DISHES = ["Soupe", "Steak", "Tarte"]


def test_data_preserved():
    assert Menu(DISHES).dishes == DISHES


def test_indexing_replaces_get():
    m = Menu(DISHES)
    assert m[0] == "Soupe"
    assert m[-1] == "Tarte"


def test_len_replaces_nb():
    assert len(Menu(DISHES)) == 3


def test_old_methods_removed():
    assert not hasattr(Menu, "get")
    assert not hasattr(Menu, "nb")


def test_iteration_now_free():
    assert list(Menu(DISHES)) == DISHES


def test_in_operator_free():
    # edge : `in` aussi vient gratuitement du protocole séquence
    m = Menu(DISHES)
    assert "Steak" in m
    assert "Pizza" not in m

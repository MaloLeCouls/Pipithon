import pytest

from solution_user import Menu

DISHES = ["Soupe", "Steak", "Tarte"]


def test_index_zero():
    assert Menu(DISHES)[0] == "Soupe"


def test_positive_index():
    assert Menu(DISHES)[1] == "Steak"


def test_negative_index():
    assert Menu(DISHES)[-1] == "Tarte"


def test_out_of_range_raises_indexerror():
    with pytest.raises(IndexError):
        Menu(DISHES)[99]


def test_not_coupled_to_caller_list():
    # edge case : muter la liste passée ne doit pas changer le menu
    src = ["Soupe", "Steak"]
    m = Menu(src)
    src.append("Intrus")
    assert m[-1] == "Steak"

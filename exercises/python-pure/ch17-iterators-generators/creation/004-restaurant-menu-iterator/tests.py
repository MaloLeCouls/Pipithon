import pytest

from solution_user import Dish, Menu, MenuIterator


def make_menu() -> Menu:
    return Menu([
        Dish("D1", "Soupe", 8.0),
        Dish("D2", "Plat", 14.0),
        Dish("D3", "Dessert", 6.0),
    ])


def test_menu_iterates_in_order():
    names = [d.name for d in make_menu()]
    assert names == ["Soupe", "Plat", "Dessert"]


def test_menu_is_reusable():
    menu = make_menu()
    once = [d.dish_id for d in menu]
    twice = [d.dish_id for d in menu]
    assert once == twice == ["D1", "D2", "D3"]


def test_iterator_is_its_own_iter():
    it = iter(make_menu())
    assert iter(it) is it
    assert isinstance(it, MenuIterator)


def test_iterator_raises_stopiteration_when_exhausted():
    it = iter(make_menu())
    for _ in range(3):
        next(it)
    with pytest.raises(StopIteration):
        next(it)


def test_empty_menu():
    menu = Menu([])
    assert list(menu) == []
    with pytest.raises(StopIteration):
        next(iter(menu))

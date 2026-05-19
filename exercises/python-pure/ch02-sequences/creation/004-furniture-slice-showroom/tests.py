from solution_user import every_other, reversed_showroom

CAT = ["chair", "table", "desk", "sofa", "shelf"]


def test_every_other():
    assert every_other(CAT) == ["chair", "desk", "shelf"]


def test_reversed():
    assert reversed_showroom(CAT) == ["shelf", "sofa", "desk", "table", "chair"]


def test_every_other_even_length():
    assert every_other(["a", "b", "c", "d"]) == ["a", "c"]


def test_does_not_mutate_input():
    src = ["a", "b", "c"]
    every_other(src)
    reversed_showroom(src)
    assert src == ["a", "b", "c"]


def test_empty_lists():
    # edge : aucune erreur sur l'entrée vide
    assert every_other([]) == []
    assert reversed_showroom([]) == []


def test_single_element():
    # edge : un seul meuble
    assert every_other(["solo"]) == ["solo"]
    assert reversed_showroom(["solo"]) == ["solo"]

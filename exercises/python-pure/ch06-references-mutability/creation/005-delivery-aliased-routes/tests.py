from solution_user import aliased_pairs


def test_no_aliases_returns_empty():
    routes = [["A", "B"], ["A", "B"], ["C"]]
    # Deux premières sont == mais pas is.
    assert aliased_pairs(routes) == []


def test_single_aliasing():
    r = ["A", "B"]
    routes = [r, ["C"], r]
    assert aliased_pairs(routes) == [(0, 2)]


def test_multiple_aliasing_chain():
    r = ["A"]
    routes = [r, r, r]
    assert aliased_pairs(routes) == [(0, 1), (0, 2), (1, 2)]


def test_empty_list_safe():
    assert aliased_pairs([]) == []


def test_uses_is_not_equality():
    # edge case : deux listes égales mais distinctes ne doivent PAS apparaître.
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert aliased_pairs([a, b]) == []

from solution_user import common_allergens, only_in_first


def test_common():
    assert common_allergens(["gluten", "egg"], ["egg", "soy"]) == {"egg"}


def test_only_in_first():
    assert only_in_first(["gluten", "egg"], ["egg", "soy"]) == {"gluten"}


def test_no_common():
    assert common_allergens(["gluten"], ["soy"]) == set()


def test_returns_sets():
    assert isinstance(common_allergens(["x"], ["x"]), set)
    assert isinstance(only_in_first(["x"], []), set)


def test_duplicates_collapse():
    # edge : doublons dans l'entrée -> set dédupe naturellement
    assert only_in_first(["egg", "egg", "soy"], ["soy"]) == {"egg"}


def test_empty_dish():
    # edge : un plat sans allergène
    assert common_allergens([], ["egg"]) == set()
    assert only_in_first([], ["egg"]) == set()

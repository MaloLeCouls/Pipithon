from solution_user import clone_catalog


def test_clone_is_distinct_dict():
    cat = {"CHAIRS": ["A1"]}
    assert clone_catalog(cat) is not cat


def test_clone_isolates_inner_lists():
    cat = {"CHAIRS": ["A1"]}
    clone = clone_catalog(cat)
    clone["CHAIRS"].append("EXTRA")
    assert cat == {"CHAIRS": ["A1"]}


def test_clone_equals_original_initially():
    cat = {"CHAIRS": ["A1"], "DESKS": ["D1"]}
    assert clone_catalog(cat) == cat


def test_mutating_clone_section_does_not_leak():
    cat = {"DESKS": ["D1", "D2"]}
    clone = clone_catalog(cat)
    clone["DESKS"][0] = "MUTATED"
    assert cat["DESKS"] == ["D1", "D2"]


def test_empty_catalog():
    assert clone_catalog({}) == {}

from solution_user import clone_catalog


def test_clone_equals_original():
    cat = {"CHAIRS": ["A1"]}
    assert clone_catalog(cat) == cat


def test_clone_is_distinct():
    cat = {"CHAIRS": ["A1"]}
    assert clone_catalog(cat) is not cat


def test_clone_isolates_inner_lists():
    # le cœur du refactor : les listes internes doivent être DISTINCTES.
    cat = {"CHAIRS": ["A1"]}
    clone = clone_catalog(cat)
    clone["CHAIRS"].append("EXTRA")
    assert cat == {"CHAIRS": ["A1"]}


def test_clone_empty():
    assert clone_catalog({}) == {}


def test_clone_handles_multiple_sections():
    cat = {"CHAIRS": ["A1"], "DESKS": ["D1"]}
    clone = clone_catalog(cat)
    clone["DESKS"].append("D2")
    assert cat["DESKS"] == ["D1"]

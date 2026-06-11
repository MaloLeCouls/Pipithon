from solution_user import clone_catalog


def test_clone_is_equal():
    cat = {"CHAIRS": ["A1"], "DESKS": ["DESK-204"]}
    assert clone_catalog(cat) == cat


def test_top_level_dict_is_distinct():
    cat = {"CHAIRS": ["A1"]}
    assert clone_catalog(cat) is not cat


def test_inner_lists_are_distinct():
    cat = {"CHAIRS": ["A1"]}
    clone = clone_catalog(cat)
    assert clone["CHAIRS"] is not cat["CHAIRS"]


def test_mutating_clone_section_isolates_original():
    cat = {"CHAIRS": ["A1"]}
    clone = clone_catalog(cat)
    clone["CHAIRS"].append("EXTRA")
    assert cat == {"CHAIRS": ["A1"]}


def test_clone_empty():
    assert clone_catalog({}) == {}


def test_clone_adds_new_section_in_clone_only():
    # edge case : ajouter une nouvelle section au clone ne doit pas affecter l'original.
    cat = {"CHAIRS": ["A1"]}
    clone = clone_catalog(cat)
    clone["DESKS"] = ["DESK-1"]
    assert "DESKS" not in cat

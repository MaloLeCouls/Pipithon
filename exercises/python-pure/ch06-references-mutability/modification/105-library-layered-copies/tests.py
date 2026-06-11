from solution_user import clone_catalog


def _make() -> dict[str, list[dict]]:
    return {
        "Hugo": [
            {"title": "Les Misérables", "reviews": ["A+"]},
            {"title": "Notre-Dame", "reviews": []},
        ],
    }


def test_clone_equals_original():
    cat = _make()
    assert clone_catalog(cat) == cat


def test_top_level_distinct():
    cat = _make()
    assert clone_catalog(cat) is not cat


def test_book_list_distinct():
    cat = _make()
    clone = clone_catalog(cat)
    assert clone["Hugo"] is not cat["Hugo"]


def test_book_dict_distinct():
    cat = _make()
    clone = clone_catalog(cat)
    assert clone["Hugo"][0] is not cat["Hugo"][0]


def test_reviews_distinct():
    cat = _make()
    clone = clone_catalog(cat)
    assert clone["Hugo"][0]["reviews"] is not cat["Hugo"][0]["reviews"]


def test_mutating_clone_reviews_isolates_original():
    cat = _make()
    clone = clone_catalog(cat)
    clone["Hugo"][0]["reviews"].append("MUTATED")
    assert "MUTATED" not in cat["Hugo"][0]["reviews"]


def test_mutating_clone_book_list_isolates_original():
    cat = _make()
    clone = clone_catalog(cat)
    clone["Hugo"].append({"title": "Ninety-Three", "reviews": []})
    assert len(cat["Hugo"]) == 2

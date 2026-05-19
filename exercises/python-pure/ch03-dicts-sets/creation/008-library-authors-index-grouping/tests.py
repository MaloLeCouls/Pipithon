from solution_user import index_by_author

BOOKS = [
    {"author": "Herbert", "title": "Dune"},
    {"author": "Herbert", "title": "Dune Messiah"},
    {"author": "Gibson", "title": "Neuromancer"},
]


def test_groups_by_author():
    idx = index_by_author(BOOKS)
    assert idx["Herbert"] == {"Dune", "Dune Messiah"}
    assert idx["Gibson"] == {"Neuromancer"}


def test_dedup_titles():
    dup = [
        {"author": "H", "title": "Dune"},
        {"author": "H", "title": "Dune"},
    ]
    assert index_by_author(dup) == {"H": {"Dune"}}


def test_empty():
    assert index_by_author([]) == {}


def test_values_are_sets():
    assert isinstance(index_by_author(BOOKS)["Gibson"], set)


def test_no_phantom_author_keys():
    # edge : interroger un auteur absent ne doit pas le créer
    idx = index_by_author(BOOKS)
    _ = idx.get("Asimov")
    assert "Asimov" not in idx

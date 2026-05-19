import pytest

from solution_user import Resource


def test_minimal_construction():
    r = Resource("oai:1", "Dune")
    assert r.identifier == "oai:1"
    assert r.title == "Dune"
    assert r.authors == []
    assert r.subjects == []
    assert r.description is None


def test_default_lists_independent():
    a = Resource("id1", "A")
    b = Resource("id2", "B")
    a.authors.append("X")
    assert b.authors == []
    assert a.authors is not b.authors


def test_post_init_normalized():
    r = Resource("id", "  Le Petit Prince  ")
    assert r._normalized == "le petit prince"


def test_empty_identifier_rejected():
    with pytest.raises(ValueError, match="identifier"):
        Resource("  ", "Titre")


def test_normalized_excluded_from_repr():
    r = Resource("id", "Dune")
    assert "_normalized" not in repr(r)
    assert "Resource(" in repr(r)


def test_normalized_not_init_arg():
    with pytest.raises(TypeError):
        Resource("id", "T", [], [], None, "already")


def test_full_construction():
    r = Resource("id", "T", ["A"], ["sci-fi"], "desc")
    assert r.authors == ["A"]
    assert r.subjects == ["sci-fi"]
    assert r.description == "desc"


def test_equality_ignores_internal_consistently():
    # edge : deux records mêmes champs publics -> égaux (eq généré)
    assert Resource("id", "T") == Resource("id", "T")

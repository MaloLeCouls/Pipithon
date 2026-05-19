from solution_user import Movie


def test_repr_with_rating():
    assert repr(Movie("Dune", 8.5)) == "Movie(title='Dune', rating=8.5)"


def test_repr_without_rating_defaults_to_none():
    assert repr(Movie("Tenet")) == "Movie(title='Tenet', rating=unrated)"


def test_repr_explicit_none():
    assert repr(Movie("Tenet", None)) == "Movie(title='Tenet', rating=unrated)"


def test_rating_attribute_preserved_as_none():
    assert Movie("Tenet").rating is None


def test_zero_rating_is_not_treated_as_unrated():
    # edge case : 0.0 est une vraie note, pas une absence de note
    assert repr(Movie("Flop", 0.0)) == "Movie(title='Flop', rating=0.0)"

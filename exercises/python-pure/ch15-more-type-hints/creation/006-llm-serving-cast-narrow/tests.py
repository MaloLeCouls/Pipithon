from solution_user import parse_count


def test_returns_int_value():
    assert parse_count({"count": 42}) == 42


def test_passes_through_at_runtime():
    """cast n'a pas d'effet runtime ; il renvoie la valeur telle quelle."""
    assert parse_count({"count": 0}) == 0
    assert parse_count({"count": 1_000_000}) == 1_000_000


def test_cast_does_not_check_type():
    """Si on viole le contrat (passer une str), cast laisse passer.
    C'est pour ça qu'on dit "cast est un aveu, pas une preuve"."""
    result = parse_count({"count": "fake_int"})  # type: ignore[dict-item]
    assert result == "fake_int"  # eh oui, cast ne convertit pas

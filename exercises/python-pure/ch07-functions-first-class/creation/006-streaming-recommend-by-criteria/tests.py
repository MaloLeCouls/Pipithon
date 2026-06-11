from solution_user import Movie, recommend


def _catalog() -> list[Movie]:
    return [
        Movie("Le Cercle", 90, "horror"),
        Movie("Inception", 148, "scifi"),
        Movie("OSS117", 99, "comedy"),
    ]


def test_filter_by_duration():
    out = recommend(_catalog(), lambda m: m.duration_min < 120)
    assert [m.title for m in out] == ["Le Cercle", "OSS117"]


def test_filter_by_genre():
    out = recommend(_catalog(), lambda m: m.genre == "scifi")
    assert [m.title for m in out] == ["Inception"]


def test_composite_criteria():
    out = recommend(_catalog(), lambda m: m.genre == "comedy" and m.duration_min < 100)
    assert [m.title for m in out] == ["OSS117"]


def test_no_match_returns_empty():
    out = recommend(_catalog(), lambda m: False)
    assert out == []


def test_preserves_input_order():
    out = recommend(_catalog(), lambda m: True)
    assert out == _catalog()

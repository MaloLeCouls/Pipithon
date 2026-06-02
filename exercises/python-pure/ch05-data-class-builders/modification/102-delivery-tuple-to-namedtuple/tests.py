from solution_user import Leg, make_leg


def test_named_access():
    leg = make_leg("Paris", "Lyon", 465.0)
    assert leg.origin == "Paris"
    assert leg.dest == "Lyon"
    assert leg.km == 465.0


def test_still_tuple_indexable():
    leg = make_leg("A", "B", 10.0)
    assert leg[0] == "A"
    assert leg[2] == 10.0


def test_unpacking_still_works():
    origin, dest, km = make_leg("A", "B", 10.0)
    assert (origin, dest, km) == ("A", "B", 10.0)


def test_is_named_tuple_type():
    assert isinstance(make_leg("A", "B", 1.0), Leg)
    assert issubclass(Leg, tuple)


def test_equality_edge():
    assert make_leg("A", "B", 1.0) == Leg("A", "B", 1.0)

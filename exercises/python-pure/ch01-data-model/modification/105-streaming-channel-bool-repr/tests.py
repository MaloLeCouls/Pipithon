from solution_user import Channel


def test_attributes_preserved():
    c = Channel("News", 42)
    assert c.name == "News"
    assert c.viewers == 42


def test_truthy_when_viewers():
    assert bool(Channel("News", 42)) is True
    assert ("live" if Channel("News", 1) else "off") == "live"


def test_falsy_when_no_viewers():
    assert bool(Channel("News", 0)) is False


def test_repr_live_and_offline():
    assert repr(Channel("News", 42)) == "Channel(name='News', viewers=42)"
    assert repr(Channel("News", 0)) == "Channel(name='News', offline)"


def test_old_methods_removed():
    assert not hasattr(Channel, "is_live")
    assert not hasattr(Channel, "describe")


def test_bool_returns_real_bool():
    # edge : pas un int implicite
    assert type(bool(Channel("X", 3))) is bool

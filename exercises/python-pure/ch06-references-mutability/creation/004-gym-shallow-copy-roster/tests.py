from solution_user import Member, snapshot


def test_snapshot_is_distinct_list():
    a = Member(1, "Alice")
    roster = [a]
    snap = snapshot(roster)
    assert snap is not roster


def test_snapshot_shares_members():
    a = Member(1, "Alice")
    snap = snapshot([a])
    assert snap[0] is a  # même Member, pas une copie


def test_snapshot_isolates_container_growth():
    roster = [Member(1, "A")]
    snap = snapshot(roster)
    roster.append(Member(2, "B"))
    assert len(snap) == 1


def test_snapshot_empty_returns_empty_distinct():
    roster: list[Member] = []
    snap = snapshot(roster)
    assert snap == []
    assert snap is not roster


def test_snapshot_preserves_order():
    members = [Member(i, f"M{i}") for i in range(4)]
    assert snapshot(members) == members

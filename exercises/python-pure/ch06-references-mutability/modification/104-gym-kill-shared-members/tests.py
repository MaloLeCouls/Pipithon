from solution_user import Member, Session, schedule


def test_returns_one_session_per_slot():
    sessions = schedule(["10:00", "11:00", "12:00"], [Member(1, "Alice")])
    assert len(sessions) == 3
    assert [s.slot for s in sessions] == ["10:00", "11:00", "12:00"]


def test_rosters_are_distinct_lists():
    sessions = schedule(["10:00", "11:00"], [Member(1, "Alice")])
    assert sessions[0].roster is not sessions[1].roster


def test_appending_to_one_session_does_not_leak():
    # le cœur du refactor : muter une session ne touche pas les autres.
    sessions = schedule(["10:00", "11:00"], [Member(1, "Alice")])
    sessions[0].roster.append(Member(2, "Bob"))
    assert len(sessions[1].roster) == 1


def test_shared_member_objects_is_acceptable():
    # On veut juste isoler les listes, pas dupliquer les Member.
    roster = [Member(1, "Alice")]
    sessions = schedule(["10:00", "11:00"], roster)
    assert sessions[0].roster[0] is sessions[1].roster[0]


def test_empty_slots_returns_empty():
    assert schedule([], [Member(1, "X")]) == []

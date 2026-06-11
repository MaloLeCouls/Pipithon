from solution_user import Member, Session, Trainer, fork_session


def _make_session() -> Session:
    return Session(
        slot="2026-06-12T10:00",
        trainer=Trainer("Coach Mo"),
        members=[Member(1, "Alice"), Member(2, "Bob")],
    )


def test_fork_returns_distinct_session():
    orig = _make_session()
    fork = fork_session(orig)
    assert fork is not orig


def test_fork_shares_trainer():
    orig = _make_session()
    fork = fork_session(orig)
    assert fork.trainer is orig.trainer


def test_fork_isolates_members_list():
    orig = _make_session()
    fork = fork_session(orig)
    assert fork.members is not orig.members


def test_fork_deep_copies_members():
    orig = _make_session()
    fork = fork_session(orig)
    # Les Member eux-mêmes sont dupliqués (deepcopy).
    assert fork.members[0] is not orig.members[0]
    assert fork.members[0] == orig.members[0]


def test_mutating_fork_members_does_not_touch_orig():
    orig = _make_session()
    fork = fork_session(orig)
    fork.members.append(Member(3, "Carol"))
    assert len(orig.members) == 2


def test_mutating_member_attr_in_fork_isolated():
    # edge case : changer le nom d'un membre du fork ne doit pas changer l'orig.
    orig = _make_session()
    fork = fork_session(orig)
    fork.members[0].name = "Renamed"
    assert orig.members[0].name == "Alice"

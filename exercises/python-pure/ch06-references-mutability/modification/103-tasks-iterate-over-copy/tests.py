from solution_user import double_urgent


def test_one_relance_per_original_urgent():
    tasks = [
        {"title": "A", "priority": "urgent"},
        {"title": "B", "priority": "urgent"},
    ]
    out = double_urgent(tasks)
    assert len(out) == 4
    relances = [t for t in out if t["title"].endswith("(relance)")]
    assert {t["title"] for t in relances} == {"A (relance)", "B (relance)"}


def test_relance_keeps_urgent_priority():
    tasks = [{"title": "X", "priority": "urgent"}]
    out = double_urgent(tasks)
    relance = [t for t in out if t["title"].endswith("(relance)")][0]
    assert relance["priority"] == "urgent"


def test_no_urgent_no_relance():
    tasks = [{"title": "tidy", "priority": "low"}]
    out = double_urgent(tasks)
    assert out == [{"title": "tidy", "priority": "low"}]


def test_no_relance_of_relance():
    # le coeur du refactor : la relance ne doit pas re-déclencher une relance.
    tasks = [{"title": "A", "priority": "urgent"}]
    out = double_urgent(tasks)
    # exactement 2 éléments : original + 1 relance.
    assert len(out) == 2
    # surtout pas "A (relance) (relance)".
    assert not any(t["title"].count("(relance)") > 1 for t in out)


def test_returns_same_list_mutated():
    tasks = [{"title": "X", "priority": "urgent"}]
    out = double_urgent(tasks)
    assert out is tasks


def test_empty_input():
    assert double_urgent([]) == []

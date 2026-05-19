from solution_user import triage

ORDERS = [
    {"id": "A", "priority": 1, "total": 50.0},
    {"id": "B", "priority": 0, "total": 20.0},
    {"id": "C", "priority": 0, "total": 99.0},
    {"id": "D", "priority": 2, "total": 10.0},
]


def test_priority_then_total_desc():
    assert [o["id"] for o in triage(ORDERS)] == ["C", "B", "A", "D"]


def test_returns_new_list_not_none():
    result = triage(ORDERS)
    assert result is not None
    assert isinstance(result, list)


def test_input_not_mutated():
    snapshot = [dict(o) for o in ORDERS]
    triage(ORDERS)
    assert ORDERS == snapshot


def test_empty():
    assert triage([]) == []


def test_stable_within_same_key():
    # edge : à (priority, total) identiques, l'ordre d'origine est conservé
    same = [
        {"id": "X", "priority": 0, "total": 10.0},
        {"id": "Y", "priority": 0, "total": 10.0},
    ]
    assert [o["id"] for o in triage(same)] == ["X", "Y"]

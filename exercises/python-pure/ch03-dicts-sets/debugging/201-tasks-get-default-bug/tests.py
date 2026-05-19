from solution_user import group_by_assignee

TASKS = [
    {"id": "T1", "assignee": "Sam"},
    {"id": "T2", "assignee": "Lee"},
    {"id": "T3", "assignee": "Sam"},
]


def test_groups_populated():
    assert group_by_assignee(TASKS) == {"Sam": ["T1", "T3"], "Lee": ["T2"]}


def test_not_empty():
    assert group_by_assignee(TASKS) != {}


def test_single():
    assert group_by_assignee([{"id": "X", "assignee": "Z"}]) == {"Z": ["X"]}


def test_empty_input():
    assert group_by_assignee([]) == {}


def test_order_within_group():
    # edge : ordre d'arrivée préservé dans chaque groupe
    assert group_by_assignee(TASKS)["Sam"] == ["T1", "T3"]

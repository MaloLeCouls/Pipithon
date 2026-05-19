from solution_user import group_by_zone

PKGS = [
    {"tracking": "A", "zone": "Z1"},
    {"tracking": "B", "zone": "Z2"},
    {"tracking": "C", "zone": "Z1"},
]


def test_groups():
    assert group_by_zone(PKGS) == {"Z1": ["A", "C"], "Z2": ["B"]}


def test_order_preserved():
    assert list(group_by_zone(PKGS).keys()) == ["Z1", "Z2"]
    assert group_by_zone(PKGS)["Z1"] == ["A", "C"]


def test_empty():
    assert group_by_zone([]) == {}


def test_single_zone():
    one = [{"tracking": "X", "zone": "Z9"}]
    assert group_by_zone(one) == {"Z9": ["X"]}


def test_no_phantom_keys():
    # edge : lire une zone inexistante ne doit pas la créer
    result = group_by_zone(PKGS)
    _ = result.get("Z404")
    assert "Z404" not in result

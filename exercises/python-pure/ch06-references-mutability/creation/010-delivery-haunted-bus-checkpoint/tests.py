from solution_user import Bus, HauntedBus, make_fleet


# ----------------------------------- HauntedBus : le piège doit être présent.
def test_haunted_bus_shares_default_passengers_across_instances():
    a = HauntedBus()
    b = HauntedBus()
    a.pick("Alice")
    # Le bug iconique : Alice apparaît dans le bus B parce qu'ils partagent
    # le même `[]` par défaut.
    assert "Alice" in b.passengers


def test_haunted_bus_with_explicit_list_is_isolated():
    a = HauntedBus(["Alice"])
    b = HauntedBus(["Bob"])
    a.pick("Carol")
    assert "Carol" not in b.passengers


# ----------------------------------- Bus : le None-guard doit éviter le piège.
def test_bus_default_passengers_are_isolated():
    a = Bus()
    b = Bus()
    a.pick("Alice")
    assert "Alice" not in b.passengers


def test_bus_isolates_caller_list():
    src = ["Alice"]
    a = Bus(src)
    src.append("Bob")
    assert "Bob" not in a.passengers


# ----------------------------------- make_fleet : shallow vs deep.
def test_shallow_clone_shares_passengers_list():
    proto = Bus(["Alice"])
    shallow, _ = make_fleet(proto)
    shallow.pick("Bob")
    assert "Bob" in proto.passengers  # liste partagée


def test_deep_clone_isolates_passengers_list():
    proto = Bus(["Alice"])
    _, deep = make_fleet(proto)
    deep.pick("Bob")
    assert "Bob" not in proto.passengers  # liste isolée


def test_shallow_and_deep_are_distinct_instances():
    proto = Bus(["X"])
    s, d = make_fleet(proto)
    assert s is not proto
    assert d is not proto
    assert s is not d

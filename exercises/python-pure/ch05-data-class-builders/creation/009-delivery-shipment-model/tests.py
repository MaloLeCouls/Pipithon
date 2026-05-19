from solution_user import Shipment


def test_zone_normalized():
    assert Shipment("  eu-west ").zone == "EU-WEST"


def test_default_parcels_empty_and_independent():
    a, b = Shipment("Z1"), Shipment("Z2")
    a.add(1.0)
    assert b.parcels == []
    assert a.parcels is not b.parcels


def test_total_weight_from_initial_parcels():
    s = Shipment("Z1", [2.0, 3.0])
    assert s.total_weight == 5.0


def test_add_updates_total():
    s = Shipment("Z1")
    s.add(1.5)
    s.add(2.5)
    assert s.parcels == [1.5, 2.5]
    assert s.total_weight == 4.0


def test_total_weight_not_constructor_arg():
    import pytest

    with pytest.raises(TypeError):
        Shipment("Z1", [1.0], 999.0)


def test_empty_shipment_edge():
    s = Shipment("Z9")
    assert s.total_weight == 0.0
    assert s.parcels == []

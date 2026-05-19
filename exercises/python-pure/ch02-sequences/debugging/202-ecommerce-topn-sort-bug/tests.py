from solution_user import best_sellers


def make():
    return [
        {"sku": "A", "sales": 10},
        {"sku": "B", "sales": 90},
        {"sku": "C", "sales": 50},
        {"sku": "D", "sales": 70},
    ]


def test_returns_highest_first():
    top = best_sellers(make(), 2)
    assert [p["sku"] for p in top] == ["B", "D"]


def test_full_ranking():
    ranked = best_sellers(make(), 4)
    assert [p["sku"] for p in ranked] == ["B", "D", "C", "A"]


def test_input_not_mutated():
    products = make()
    snapshot = [dict(p) for p in products]
    best_sellers(products, 2)
    assert products == snapshot


def test_n_larger_than_list():
    assert len(best_sellers(make(), 99)) == 4


def test_n_zero_edge():
    # edge : top 0 = liste vide, et l'entrée reste intacte
    products = make()
    assert best_sellers(products, 0) == []
    assert len(products) == 4

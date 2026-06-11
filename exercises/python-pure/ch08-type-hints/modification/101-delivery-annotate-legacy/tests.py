import inspect

from solution_user import average_per_stop, total_distance


def test_total_distance_sum():
    stops = [{"km": 10}, {"km": 20}, {"km": 5}]
    assert total_distance(stops) == 35


def test_total_distance_empty():
    assert total_distance([]) == 0


def test_average_per_stop():
    stops = [{"km": 10}, {"km": 20}, {"km": 30}]
    assert average_per_stop(stops) == 20.0


def test_average_per_stop_empty():
    assert average_per_stop([]) == 0.0


def test_both_functions_fully_annotated():
    for fn in (total_distance, average_per_stop):
        sig = inspect.signature(fn)
        for name, p in sig.parameters.items():
            assert p.annotation is not inspect.Parameter.empty, \
                f"annotate `{name}` dans {fn.__name__}"
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"annotate le retour de {fn.__name__}"

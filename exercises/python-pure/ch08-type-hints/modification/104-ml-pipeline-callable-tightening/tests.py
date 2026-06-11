import inspect

from solution_user import Sample, process


def test_calls_callback_for_each_sample():
    seen: list[float] = []
    samples = [Sample(1.0), Sample(2.0), Sample(3.0)]
    process(samples, lambda s: seen.append(s.feature))
    assert seen == [1.0, 2.0, 3.0]


def test_empty_iterable_no_call():
    seen: list[float] = []
    process([], lambda s: seen.append(s.feature))
    assert seen == []


def test_callable_annotation_has_brackets():
    sig = inspect.signature(process)
    ann = str(sig.parameters["callback"].annotation)
    assert "[" in ann and "Sample" in ann, \
        f"Callable doit être paramétré : {ann}"

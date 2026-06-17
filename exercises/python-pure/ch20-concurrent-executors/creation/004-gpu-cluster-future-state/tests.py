from concurrent.futures import ThreadPoolExecutor

from solution_user import compute, submit_job, wait_done


def test_submit_returns_future():
    with ThreadPoolExecutor(max_workers=1) as ex:
        fut = submit_job(5, ex)
        assert hasattr(fut, "result")
        wait_done(fut)


def test_wait_done_is_true_after_wait():
    with ThreadPoolExecutor(max_workers=1) as ex:
        fut = submit_job(10, ex)
        assert wait_done(fut) is True


def test_future_carries_result():
    with ThreadPoolExecutor(max_workers=1) as ex:
        fut = submit_job(7, ex)
        wait_done(fut)
        assert fut.result() == 14


def test_multiple_futures_independent():
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [submit_job(i, ex) for i in range(4)]
        for fut in futs:
            wait_done(fut)
        results = [f.result() for f in futs]
    assert results == [0, 2, 4, 6]

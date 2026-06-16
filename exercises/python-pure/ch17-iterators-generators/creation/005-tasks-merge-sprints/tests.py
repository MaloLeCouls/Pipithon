import collections.abc as abc

from solution_user import Task, merge_sprints


def test_concatenates_in_order():
    s1 = [Task("A1"), Task("A2")]
    s2 = [Task("B1")]
    s3 = [Task("C1"), Task("C2"), Task("C3")]
    ids = [t.task_id for t in merge_sprints(s1, s2, s3)]
    assert ids == ["A1", "A2", "B1", "C1", "C2", "C3"]


def test_returns_iterator():
    result = merge_sprints([Task("X")])
    assert isinstance(result, abc.Iterator)


def test_no_args_yields_nothing():
    assert list(merge_sprints()) == []


def test_accepts_generators_as_input():
    def gen_sprint(prefix: str, n: int):
        for i in range(n):
            yield Task(f"{prefix}{i}")

    ids = [t.task_id for t in merge_sprints(gen_sprint("X", 2), gen_sprint("Y", 1))]
    assert ids == ["X0", "X1", "Y0"]


def test_one_sprint_pass_through():
    s = [Task("S1"), Task("S2")]
    assert [t.task_id for t in merge_sprints(s)] == ["S1", "S2"]

import pytest

from solution_user import Pipeline, UpperPipeline


def test_pipeline_is_abstract():
    with pytest.raises(TypeError):
        Pipeline()  # type: ignore[abstract]


def test_upper_pipeline_runs():
    out = UpperPipeline().run("hello")
    assert out == "dumped:LOADED:HELLO"


def test_template_method_calls_load_transform_dump_in_order():
    calls: list[str] = []

    class TraceUpper(UpperPipeline):
        def _load(self, p: str) -> str:
            calls.append("load")
            return super()._load(p)

        def _transform(self, p: str) -> str:
            calls.append("transform")
            return super()._transform(p)

        def _dump(self, p: str) -> str:
            calls.append("dump")
            return super()._dump(p)

    TraceUpper().run("x")
    assert calls == ["load", "transform", "dump"]


def test_subclass_can_override_only_transform():
    class TitlePipeline(Pipeline):
        def _transform(self, p: str) -> str:
            return p.title()

    assert TitlePipeline().run("hello world") == "dumped:Loaded:Hello World"


def test_transform_is_abstract():
    assert "_transform" in Pipeline.__abstractmethods__

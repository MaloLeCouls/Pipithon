from solution_user import FinishReason, Heartbeat, StreamToken, route_event


def test_stream_token():
    assert route_event(StreamToken(token_id=42, text="he")) == "stream:42:he"


def test_finish_stop():
    assert route_event(FinishReason(reason="stop")) == "done:ok"


def test_finish_length():
    assert route_event(FinishReason(reason="length")) == "done:max-tokens"


def test_finish_other_captured():
    assert route_event(FinishReason(reason="error")) == "done:error"
    assert route_event(FinishReason(reason="cancelled")) == "done:cancelled"


def test_heartbeat():
    assert route_event(Heartbeat()) == "alive"


def test_unknown_default():
    assert route_event("garbage") == "unknown"
    assert route_event(42) == "unknown"
    assert route_event(None) == "unknown"

"""Tests de fumée du framework pymistral.

Non exhaustifs : on vérifie que les classes s'importent, satisfont leurs
invariants de base, et que le contrat round-trip tokenize/decode tient.
La couverture pédagogique est l'affaire des exercices.
"""
from __future__ import annotations

import random

import pytest

from pymistral import (
    BPETokenizer,
    BatchedRequests,
    ConversationHistory,
    GenerationConfig,
    KVCache,
    Logits,
    Request,
    Scheduler,
    Token,
    Turn,
    Vocabulary,
    greedy_sampler,
    top_k_sampler,
    top_p_sampler,
)


# ---------------------------------------------------------------- Token (ch1)
def test_token_repr_and_eq():
    t = Token(id=5, text="hi")
    assert repr(t) == "Token(id=5, text='hi')"
    assert t == Token(id=5, text="hi")
    assert hash(t) == hash(Token(id=5, text="hi"))


def test_token_is_frozen():
    t = Token(id=1, text="x")
    with pytest.raises(Exception):  # FrozenInstanceError
        t.id = 2  # type: ignore[misc]


# ---------------------------------------------------------- Vocabulary (ch3)
def test_vocabulary_roundtrip():
    v = Vocabulary(["a", "b", "c"])
    assert len(v) == 3
    assert v.id_of("b") == 1
    assert v.text_of(1) == "b"
    assert v.add("a") == 0  # idempotent
    assert v.add("d") == 3
    assert "d" in v
    assert 3 in v
    assert "zz" not in v


# --------------------------------------------------- ConversationHistory (ch2)
def test_history_bounded_and_slice():
    h = ConversationHistory(max_turns=3)
    for i in range(5):
        h.append(Turn(role="user", content=str(i)))
    assert len(h) == 3
    assert [t.content for t in h] == ["2", "3", "4"]
    assert h[-1].content == "4"
    assert [t.content for t in h[:2]] == ["2", "3"]


def test_history_add():
    a = ConversationHistory(max_turns=10, initial=[Turn("user", "hi")])
    b = ConversationHistory(max_turns=10, initial=[Turn("assistant", "yo")])
    c = a + b
    assert len(c) == 2
    assert c[0].role == "user"
    assert c[1].role == "assistant"


# ----------------------------------------------------- BPETokenizer (ch4)
def test_tokenizer_roundtrip():
    tk = BPETokenizer()
    tokens = tk.encode("Étoile")
    assert tk.decode(tokens) == "Étoile"
    assert all(isinstance(t, Token) for t in tokens)


def test_tokenizer_encode_bytes():
    tk = BPETokenizer()
    assert tk.decode(tk.encode_bytes("hé".encode("utf-8"))) == "hé"


# ------------------------------------------------ GenerationConfig (ch5)
def test_config_defaults_and_validation():
    c = GenerationConfig()
    assert c.temperature == 1.0
    with pytest.raises(ValueError):
        GenerationConfig(temperature=-1.0)
    with pytest.raises(ValueError):
        GenerationConfig(top_p=1.5)
    with pytest.raises(ValueError):
        GenerationConfig(max_tokens=0)


def test_config_is_frozen_and_hashable():
    c = GenerationConfig(temperature=0.5)
    {c}  # smoke : doit être hashable
    with pytest.raises(Exception):
        c.temperature = 0.7  # type: ignore[misc]


# ----------------------------------------------------------- Logits (ch11)
def test_logits_add_and_argmax():
    a = Logits([1.0, 2.0, 3.0])
    b = Logits([0.5, 0.5, 0.5])
    s = a + b
    assert list(s) == [1.5, 2.5, 3.5]
    assert s.argmax() == 2


def test_logits_softmax_sums_to_one():
    probs = Logits([1.0, 2.0, 3.0]).softmax()
    assert abs(sum(probs) - 1.0) < 1e-9


def test_logits_dim_mismatch():
    with pytest.raises(ValueError):
        Logits([1.0, 2.0]) + Logits([1.0])


# --------------------------------------------------------- Sampling (ch7/13)
def test_greedy_is_deterministic_argmax():
    cfg = GenerationConfig()
    assert greedy_sampler(Logits([0.1, 0.9, 0.5]), cfg) == 1


def test_top_k_respects_k_and_rng():
    cfg = GenerationConfig(top_k=2, seed=42)
    rng = random.Random(42)
    pick = top_k_sampler(Logits([5.0, 4.0, -10.0]), cfg, rng=rng)
    assert pick in (0, 1)  # le -10 doit être exclu


def test_top_p_respects_threshold():
    cfg = GenerationConfig(top_p=0.6, seed=7)
    rng = random.Random(7)
    pick = top_p_sampler(Logits([5.0, 1.0, 1.0, 1.0]), cfg, rng=rng)
    assert pick in (0, 1, 2, 3)


def test_sampler_protocol_satisfied():
    from pymistral.sampling import Sampler

    assert isinstance(greedy_sampler, Sampler)
    assert isinstance(top_k_sampler, Sampler)


# ---------------------------------------------------------- KVCache (ch11)
def test_kv_cache_per_layer():
    c = KVCache(num_layers=2)
    c.append(0, Token(1, "a"))
    c.append(1, Token(2, "b"))
    c.append(0, Token(3, "c"))
    assert c.get(0) == [Token(1, "a"), Token(3, "c")]
    assert c.get(1) == [Token(2, "b")]
    assert len(c) == 3
    c.clear(0)
    assert len(c) == 1
    c.clear()
    assert len(c) == 0


def test_kv_cache_get_returns_copy():
    c = KVCache(num_layers=1)
    c.append(0, Token(1, "a"))
    snap = c.get(0)
    snap.append(Token(99, "x"))
    assert len(c) == 1  # mutation externe n'affecte pas le cache


def test_kv_cache_layer_bounds():
    c = KVCache(num_layers=2)
    with pytest.raises(IndexError):
        c.append(2, Token(1, "x"))


# --------------------------------------------------- Batching + Scheduler (ch12)
def test_batched_requests_slicing():
    reqs = [Request(id=f"r{i}", prompt=[Token(i, "x")]) for i in range(4)]
    b = BatchedRequests(reqs)
    assert len(b) == 4
    sub = b[1:3]
    assert isinstance(sub, BatchedRequests)
    assert [r.id for r in sub] == ["r1", "r2"]


def test_scheduler_fifo():
    s = Scheduler()
    for i in range(5):
        s.submit(Request(id=f"r{i}", prompt=[]))
    batch = s.next_batch(max_batch_size=3)
    assert [r.id for r in batch] == ["r0", "r1", "r2"]
    assert s.pending() == 2
    rest = s.next_batch(max_batch_size=10)
    assert len(rest) == 2

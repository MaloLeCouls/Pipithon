"""pymistral — mini-framework d'inférence LLM jouet, fil rouge du dojo.

Ne fait *aucun* vrai modèle : tout est simulation déterministe en Python pur,
stdlib uniquement. But pédagogique : donner aux exercices ch >= 8 une narrative
bout-en-bout — Token (ch1) -> Vocabulary (ch3) -> Tokenizer (ch4) ->
GenerationConfig (ch5) -> Sampler (ch7/ch13) -> Logits (ch11) -> KVCache (ch11)
-> Batch/Scheduler (ch12/ch19-21).

Conventions :
- Pas de dépendance externe (Pyodide-friendly).
- `mypy --strict` doit passer.
- Chaque module expose un docstring qui pointe le chapitre Fluent Python.
- API publique re-exportée ici ; détails internes restent dans leur module.
"""
from __future__ import annotations

from pymistral.batching import BatchedRequests, Request
from pymistral.cache import KVCache
from pymistral.config import GenerationConfig
from pymistral.history import ConversationHistory, Turn
from pymistral.logits import Logits
from pymistral.sampling import (
    Sampler,
    greedy_sampler,
    top_k_sampler,
    top_p_sampler,
)
from pymistral.scheduler import Scheduler
from pymistral.tokenizer import BPETokenizer
from pymistral.tokens import Token
from pymistral.vocabulary import Vocabulary

__all__ = [
    "BPETokenizer",
    "BatchedRequests",
    "ConversationHistory",
    "GenerationConfig",
    "KVCache",
    "Logits",
    "Request",
    "Sampler",
    "Scheduler",
    "Token",
    "Turn",
    "Vocabulary",
    "greedy_sampler",
    "top_k_sampler",
    "top_p_sampler",
]

__version__ = "0.1.0"

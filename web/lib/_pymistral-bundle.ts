// AUTO-GÉNÉRÉ par scripts/build-pymistral.mjs — NE PAS ÉDITER À LA MAIN.
// Source : exercises/_pymistral/pymistral/  (généré le 2026-06-11T17:25:56.762Z)
// Embarqué côté client pour que Pyodide importe `pymistral` sans réseau.

export const PYMISTRAL_BUNDLE: Record<string, string> = {
  "__init__.py": `"""pymistral — mini-framework d'inférence LLM jouet, fil rouge du dojo.

Ne fait *aucun* vrai modèle : tout est simulation déterministe en Python pur,
stdlib uniquement. But pédagogique : donner aux exercices ch >= 8 une narrative
bout-en-bout — Token (ch1) -> Vocabulary (ch3) -> Tokenizer (ch4) ->
GenerationConfig (ch5) -> Sampler (ch7/ch13) -> Logits (ch11) -> KVCache (ch11)
-> Batch/Scheduler (ch12/ch19-21).

Conventions :
- Pas de dépendance externe (Pyodide-friendly).
- \`mypy --strict\` doit passer.
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
`,
  "batching.py": `"""Request + BatchedRequests — groupement de requêtes. Chapitre 12 (sequences).

\`BatchedRequests\` est une séquence indexable/sliceable de \`Request\`. Sert de
base au \`Scheduler\` (ch12/ch19-21).
"""
from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from typing import overload

from pymistral.config import GenerationConfig
from pymistral.tokens import Token


@dataclass(slots=True)
class Request:
    """Une requête de génération : un prompt tokenisé + sa config."""

    id: str
    prompt: list[Token]
    config: GenerationConfig = field(default_factory=GenerationConfig)


class BatchedRequests:
    """Vue séquence sur un lot de Requests, immutable."""

    __slots__ = ("_requests",)

    def __init__(self, requests: Sequence[Request]) -> None:
        self._requests: tuple[Request, ...] = tuple(requests)

    @property
    def requests(self) -> tuple[Request, ...]:
        return self._requests

    def __len__(self) -> int:
        return len(self._requests)

    def __iter__(self) -> Iterator[Request]:
        return iter(self._requests)

    @overload
    def __getitem__(self, index: int) -> Request: ...
    @overload
    def __getitem__(self, index: slice) -> BatchedRequests: ...
    def __getitem__(self, index: int | slice) -> Request | BatchedRequests:
        if isinstance(index, slice):
            return BatchedRequests(self._requests[index])
        return self._requests[index]

    def __repr__(self) -> str:
        return f"BatchedRequests(size={len(self)})"
`,
  "cache.py": `"""KVCache — cache par couche, jouet. Chapitres 11 (Pythonic object) & 15 (generics).

Pas de vraie attention : on stocke des séquences de tokens par couche, pour
simuler le coût mémoire et l'éviction. Le mapping \`layer -> list[Token]\` est
exposé via \`get\` / \`append\` / \`clear\` ; jamais d'accès direct au dict interne.
"""
from __future__ import annotations

from pymistral.tokens import Token


class KVCache:
    """Cache par couche, indexé \`0..num_layers-1\`."""

    def __init__(self, num_layers: int) -> None:
        if num_layers <= 0:
            raise ValueError(f"num_layers must be > 0, got {num_layers}")
        self._num_layers = num_layers
        self._cache: dict[int, list[Token]] = {i: [] for i in range(num_layers)}

    @property
    def num_layers(self) -> int:
        return self._num_layers

    def _check_layer(self, layer: int) -> None:
        if not 0 <= layer < self._num_layers:
            raise IndexError(
                f"layer {layer} out of range [0, {self._num_layers})"
            )

    def get(self, layer: int) -> list[Token]:
        """Renvoie une *copie* — l'appelant ne peut pas muter le cache."""
        self._check_layer(layer)
        return list(self._cache[layer])

    def append(self, layer: int, token: Token) -> None:
        self._check_layer(layer)
        self._cache[layer].append(token)

    def clear(self, layer: int | None = None) -> None:
        """Vide une couche (ou tout si \`layer is None\`)."""
        if layer is None:
            for lst in self._cache.values():
                lst.clear()
        else:
            self._check_layer(layer)
            self._cache[layer].clear()

    def __len__(self) -> int:
        """Nombre total de tokens stockés, toutes couches confondues."""
        return sum(len(lst) for lst in self._cache.values())

    def __repr__(self) -> str:
        return f"KVCache(num_layers={self._num_layers}, total_tokens={len(self)})"
`,
  "config.py": `"""GenerationConfig — paramètres de génération. Chapitre 5 (data class builders).

\`frozen=True\` -> hashable, partageable entre requêtes, immutabilité forcée.
Les valeurs par défaut suivent la convention Mistral (Couche 5 du mapping).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GenerationConfig:
    """Paramètres d'une session de génération.

    Attributs:
        temperature: > 0 contrôle l'aplatissement de la softmax (1.0 neutre).
        top_k: garde les k logits les plus hauts (None = pas de filtre).
        top_p: nucleus sampling : garde le plus petit ensemble de probabilité
            cumulée >= p (None = pas de filtre).
        max_tokens: budget de tokens à générer.
        seed: graine RNG (None = non déterministe).
    """

    temperature: float = 1.0
    top_k: int | None = None
    top_p: float | None = None
    max_tokens: int = 64
    seed: int | None = None

    def __post_init__(self) -> None:
        if self.temperature <= 0:
            raise ValueError(f"temperature must be > 0, got {self.temperature}")
        if self.top_k is not None and self.top_k <= 0:
            raise ValueError(f"top_k must be > 0 if set, got {self.top_k}")
        if self.top_p is not None and not 0 < self.top_p <= 1.0:
            raise ValueError(f"top_p must be in (0, 1], got {self.top_p}")
        if self.max_tokens <= 0:
            raise ValueError(f"max_tokens must be > 0, got {self.max_tokens}")
`,
  "history.py": `"""ConversationHistory — buffer circulaire de tours. Chapitres 2 (sequences) & 16 (overload).

Utilise un \`collections.deque\` borné par \`max_turns\`. Supporte iteration,
indexation, slicing, et concaténation (\`+\`).
"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import overload


@dataclass(frozen=True, slots=True)
class Turn:
    """Un tour de conversation (role + contenu)."""

    role: str  # "user" | "assistant" | "system"
    content: str

    def __repr__(self) -> str:
        return f"Turn(role={self.role!r}, content={self.content!r})"


class ConversationHistory:
    """Buffer borné de Turns. Les plus anciens tombent quand on dépasse."""

    def __init__(
        self,
        max_turns: int = 128,
        initial: Iterable[Turn] | None = None,
    ) -> None:
        self._max_turns = max_turns
        self._turns: deque[Turn] = deque(initial or [], maxlen=max_turns)

    @property
    def max_turns(self) -> int:
        return self._max_turns

    def append(self, turn: Turn) -> None:
        self._turns.append(turn)

    def extend(self, turns: Iterable[Turn]) -> None:
        self._turns.extend(turns)

    def clear(self) -> None:
        self._turns.clear()

    def __len__(self) -> int:
        return len(self._turns)

    def __iter__(self) -> Iterator[Turn]:
        return iter(self._turns)

    @overload
    def __getitem__(self, index: int) -> Turn: ...
    @overload
    def __getitem__(self, index: slice) -> list[Turn]: ...
    def __getitem__(self, index: int | slice) -> Turn | list[Turn]:
        if isinstance(index, slice):
            return list(self._turns)[index]
        return self._turns[index]

    def __add__(self, other: ConversationHistory) -> ConversationHistory:
        """Concaténation non destructive ; max_turns hérité du membre gauche."""
        merged = ConversationHistory(max_turns=self._max_turns)
        merged.extend(self._turns)
        merged.extend(other._turns)
        return merged

    def __repr__(self) -> str:
        return f"ConversationHistory(len={len(self)}, max_turns={self._max_turns})"
`,
  "logits.py": `"""Logits — vecteur de scores. Chapitre 11 (Pythonic object, analogue Vector2d).

Implémentation Python pure (pas de numpy). Supporte \`+\`, indexation, slicing,
softmax stable (subtract max), argmax.
"""
from __future__ import annotations

import math
from collections.abc import Iterator, Sequence
from typing import overload


class Logits:
    """Vecteur immuable de scores réels (logits)."""

    __slots__ = ("_scores",)

    def __init__(self, scores: Sequence[float]) -> None:
        self._scores: tuple[float, ...] = tuple(scores)

    @property
    def scores(self) -> tuple[float, ...]:
        return self._scores

    def __len__(self) -> int:
        return len(self._scores)

    def __iter__(self) -> Iterator[float]:
        return iter(self._scores)

    @overload
    def __getitem__(self, index: int) -> float: ...
    @overload
    def __getitem__(self, index: slice) -> Logits: ...
    def __getitem__(self, index: int | slice) -> float | Logits:
        if isinstance(index, slice):
            return Logits(self._scores[index])
        return self._scores[index]

    def __add__(self, other: Logits) -> Logits:
        if len(self) != len(other):
            raise ValueError(
                f"Logits dimensions mismatch: {len(self)} vs {len(other)}"
            )
        return Logits(tuple(a + b for a, b in zip(self._scores, other._scores)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Logits):
            return NotImplemented
        return self._scores == other._scores

    def __hash__(self) -> int:
        return hash(self._scores)

    def __repr__(self) -> str:
        return f"Logits(n={len(self)})"

    def argmax(self) -> int:
        if not self._scores:
            raise ValueError("argmax of empty Logits")
        best_idx = 0
        best_val = self._scores[0]
        for i, v in enumerate(self._scores[1:], start=1):
            if v > best_val:
                best_val = v
                best_idx = i
        return best_idx

    def softmax(self, temperature: float = 1.0) -> list[float]:
        """Softmax numériquement stable. \`temperature > 0\`."""
        if temperature <= 0:
            raise ValueError(f"temperature must be > 0, got {temperature}")
        if not self._scores:
            return []
        scaled = [s / temperature for s in self._scores]
        m = max(scaled)
        exps = [math.exp(s - m) for s in scaled]
        total = sum(exps)
        return [e / total for e in exps]
`,
  "sampling.py": `"""Sampler — Protocol + stratégies. Chapitres 7 (HOF), 10 (patterns), 13 (Protocol).

Un \`Sampler\` est une callable \`(Logits, GenerationConfig, Random | None) -> int\`.
Trois stratégies fournies : greedy (argmax), top-k, top-p (nucleus).

\`Protocol\` permet à des fonctions et à des classes call-ables de satisfaire le
même type sans héritage explicite (duck typing statique).
"""
from __future__ import annotations

import random
from typing import Protocol, runtime_checkable

from pymistral.config import GenerationConfig
from pymistral.logits import Logits


@runtime_checkable
class Sampler(Protocol):
    """Stratégie de sampling : prend un Logits + config, renvoie un id."""

    def __call__(
        self,
        logits: Logits,
        config: GenerationConfig,
        rng: random.Random | None = None,
    ) -> int: ...


def greedy_sampler(
    logits: Logits,
    config: GenerationConfig,  # noqa: ARG001
    rng: random.Random | None = None,  # noqa: ARG001
) -> int:
    """Toujours l'argmax — déterministe, rng ignoré."""
    return logits.argmax()


def top_k_sampler(
    logits: Logits,
    config: GenerationConfig,
    rng: random.Random | None = None,
) -> int:
    """Échantillonne parmi les \`top_k\` logits les plus hauts.

    \`rng\` requis pour la reproductibilité ; à défaut un Random nouveau est créé
    (avec la \`config.seed\` si fournie).
    """
    if config.top_k is None:
        raise ValueError("top_k_sampler requires config.top_k to be set")
    if rng is None:
        rng = random.Random(config.seed)
    probs = logits.softmax(temperature=config.temperature)
    indexed = sorted(enumerate(probs), key=lambda kv: kv[1], reverse=True)
    kept = indexed[: config.top_k]
    total = sum(p for _, p in kept)
    weights = [p / total for _, p in kept]
    choice_idx = _weighted_choice(weights, rng)
    return kept[choice_idx][0]


def top_p_sampler(
    logits: Logits,
    config: GenerationConfig,
    rng: random.Random | None = None,
) -> int:
    """Nucleus sampling : garde le plus petit ensemble dont la proba cumulée >= top_p."""
    if config.top_p is None:
        raise ValueError("top_p_sampler requires config.top_p to be set")
    if rng is None:
        rng = random.Random(config.seed)
    probs = logits.softmax(temperature=config.temperature)
    indexed = sorted(enumerate(probs), key=lambda kv: kv[1], reverse=True)
    kept: list[tuple[int, float]] = []
    cum = 0.0
    for i, p in indexed:
        kept.append((i, p))
        cum += p
        if cum >= config.top_p:
            break
    total = sum(p for _, p in kept)
    weights = [p / total for _, p in kept]
    choice_idx = _weighted_choice(weights, rng)
    return kept[choice_idx][0]


def _weighted_choice(weights: list[float], rng: random.Random) -> int:
    """Tirage pondéré déterministe — utilise rng.random() pour la reproductibilité."""
    r = rng.random()
    cum = 0.0
    for i, w in enumerate(weights):
        cum += w
        if r < cum:
            return i
    return len(weights) - 1
`,
  "scheduler.py": `"""Scheduler — FIFO trivial. Chapitres 12 (sequences) & 19-21 (concurrence).

Une file de Requests en attente, \`next_batch\` pop le préfixe. Pas de priorité,
pas de continuous batching « pour de vrai » — l'exo continuous-batching du
ch19+ enrichira ça.
"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterable

from pymistral.batching import BatchedRequests, Request


class Scheduler:
    """File FIFO de Requests, batch poppé par \`next_batch\`."""

    def __init__(self, initial: Iterable[Request] | None = None) -> None:
        self._queue: deque[Request] = deque(initial or [])

    def submit(self, request: Request) -> None:
        self._queue.append(request)

    def pending(self) -> int:
        return len(self._queue)

    def next_batch(self, max_batch_size: int = 8) -> BatchedRequests:
        if max_batch_size <= 0:
            raise ValueError(f"max_batch_size must be > 0, got {max_batch_size}")
        taken: list[Request] = []
        for _ in range(min(max_batch_size, len(self._queue))):
            taken.append(self._queue.popleft())
        return BatchedRequests(taken)

    def __len__(self) -> int:
        return len(self._queue)

    def __repr__(self) -> str:
        return f"Scheduler(pending={len(self)})"
`,
  "tokenizer.py": `"""BPETokenizer — tokenizer caractère-par-caractère jouet. Chapitre 4 (unicode/bytes).

C'est *pas* du vrai BPE (pas de merges) : un caractère = un token. Le but
est de drilller la frontière \`str\`/\`bytes\`, l'encodage UTF-8 et le round-trip
encode/decode, pas de battre tiktoken.
"""
from __future__ import annotations

from collections.abc import Iterable

from pymistral.tokens import Token
from pymistral.vocabulary import Vocabulary


class BPETokenizer:
    """Tokenizer trivial : 1 code point = 1 token. Vocab auto-construit.

    Le contrat round-trip est garanti : \`decode(encode(s)) == s\`.
    """

    def __init__(self, vocab: Vocabulary | None = None) -> None:
        self._vocab = vocab if vocab is not None else Vocabulary()

    @property
    def vocab(self) -> Vocabulary:
        return self._vocab

    def encode(self, text: str) -> list[Token]:
        out: list[Token] = []
        for ch in text:
            tid = self._vocab.add(ch)
            out.append(Token(id=tid, text=ch))
        return out

    def decode(self, tokens: Iterable[Token]) -> str:
        return "".join(t.text for t in tokens)

    def encode_bytes(self, data: bytes, encoding: str = "utf-8") -> list[Token]:
        """Pratique pour les exos chapitre 4 : décode bytes puis tokenize."""
        return self.encode(data.decode(encoding))

    def __repr__(self) -> str:
        return f"BPETokenizer(vocab_size={len(self._vocab)})"
`,
  "tokens.py": `"""Token — unité atomique de texte. Introduit au chapitre 1 (data model).

\`Token\` est *frozen* (immutable) et hashable : utilisable comme clé de dict ou
membre de set. Le \`__repr__\` est sans ambiguïté, conforme au protocole Fluent
Python ch.1.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Token:
    """Une unité de texte avec son identifiant dans un vocabulaire.

    Attributs:
        id: index dans le \`Vocabulary\` (entier positif).
        text: forme imprimable du token (peut être un caractère, une pièce BPE).
    """

    id: int
    text: str

    def __repr__(self) -> str:
        return f"Token(id={self.id}, text={self.text!r})"
`,
  "vocabulary.py": `"""Vocabulary — mapping bidirectionnel id<->text en O(1). Chapitre 3 (dicts).

Pas de tri, pas de fréquences : c'est un *index*. Pour étendre il faut passer
par \`add\` (qui dédoublonne) ; les lookups sont O(1) dans les deux sens grâce
à deux dicts maintenus en miroir.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Vocabulary:
    """Index bidirectionnel id<->text avec dédoublonnage."""

    def __init__(self, initial: Iterable[str] | None = None) -> None:
        self._text_to_id: dict[str, int] = {}
        self._id_to_text: dict[int, str] = {}
        if initial is not None:
            for text in initial:
                self.add(text)

    def add(self, text: str) -> int:
        """Ajoute \`text\` s'il n'existe pas, renvoie son id."""
        if text in self._text_to_id:
            return self._text_to_id[text]
        new_id = len(self._text_to_id)
        self._text_to_id[text] = new_id
        self._id_to_text[new_id] = text
        return new_id

    def text_of(self, id_: int) -> str:
        return self._id_to_text[id_]

    def id_of(self, text: str) -> int:
        return self._text_to_id[text]

    def __len__(self) -> int:
        return len(self._text_to_id)

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return item in self._text_to_id
        if isinstance(item, int):
            return item in self._id_to_text
        return False

    def __iter__(self) -> Iterator[str]:
        return iter(self._text_to_id)

    def __repr__(self) -> str:
        return f"Vocabulary(size={len(self)})"
`,
};

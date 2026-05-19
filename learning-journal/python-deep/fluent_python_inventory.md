# Fluent Python 2e — Inventaire de référence

> Source : table des matières officielle *Fluent Python* 2e (Luciano Ramalho,
> O'Reilly 2022, Python 3.10+). 24 chapitres, 5 parties.
> Coche au fur et à mesure. C'est la **vérité de calibration** des
> `docs/curriculum/python-pure/chapter-XX.md`.
>
> Légende tier (cf. `docs/context/mapping-mistral.md` Couche 1 + angle ML
> inference) : **S** socle réflexe · **A** très différenciant · **B** culture/lecture.

## Partie I — Data Structures

- [ ] **Ch 1 — The Python Data Model** · tier S
  - Dunder : `__init__`, `__len__`, `__getitem__`, `__repr__`, `__str__`, `__bool__`, `__abs__`
  - "Pythonic" : `len(x)` vs `x.len()` ; émulation des types built-in
  - Vue d'ensemble des dunders par catégorie
- [ ] **Ch 2 — An Array of Sequences** · tier S
  - mutables (`list`, `bytearray`, `array`, `deque`) vs immutables (`tuple`, `str`, `bytes`)
  - container vs flat sequences ; list/generator comprehensions
  - tuples records & listes immutables ; unpacking, `*args`, capture `*`
  - `match`/`case` sur séquences ; slicing avancé (`slice`, multidim, assignment, pas négatif)
  - `+`/`*` (pièges copie superficielle) ; `+=`/`*=` mutable vs immutable
  - `list.sort()` vs `sorted()`, `key` ; `bisect` ; `array`/`memoryview`/`deque`
- [ ] **Ch 3 — Dictionaries and Sets** · tier S
  - dict comprehensions ; unpacking mappings ; fusion `|`/`|=` ; `match` sur mappings
  - `defaultdict`, `__missing__` ; `OrderedDict`, `ChainMap`, `Counter`, `UserDict`
  - `MappingProxyType` ; vues dict ; hash tables / dicts compacts (3.7+)
  - `set`/`frozenset`, opérations ensemblistes, set comprehensions ; hashabilité (`__hash__`/`__eq__`)
- [ ] **Ch 4 — Unicode Text versus Bytes** · tier A
  - `str`/`bytes`/`bytearray` ; encode/decode UTF-8/16, latin-1, ASCII
  - `UnicodeEncodeError`/`DecodeError` ; BOM ; `unicodedata` NFC/NFD/NFKC/NFKD, case folding
  - égalité canonique ; `re` vs `regex` ; tri `locale`/`pyuca` ; dual-mode `str`/`bytes`
- [ ] **Ch 5 — Data Class Builders** · tier S
  - `namedtuple`, `typing.NamedTuple`, `@dataclass` (`field`, `default_factory`, `__post_init__`, `frozen=True`)
  - quand utiliser quoi ; data class comme code smell ; représentation, mutabilité par défaut
- [ ] **Ch 6 — Object References, Mutability, and Recycling** · tier S
  - variables = labels ; `is` vs `==` ; `id()` ; tuples relativement immutables
  - `copy.copy` vs `copy.deepcopy` ; aliasing ; passage par référence
  - mutable default arg ; GC (refcount, cycles) ; `weakref` ; interning ints/strings

## Partie II — Functions as Objects

- [ ] **Ch 7 — Functions as First-Class Objects** · tier S
  - fonctions = objets ; higher-order (`map`/`filter`/`reduce`) ; `lambda` et limites
  - 9 flavors de callables ; `__call__` ; introspection (`__name__`, `__code__`, `__defaults__`…)
  - positionnels / keyword-only (`*`) / positional-only (`/`) ; `inspect.Signature`
  - `operator` (`itemgetter`, `attrgetter`, `methodcaller`) ; `functools.partial`
- [ ] **Ch 8 — Type Hints in Functions** · tier S
  - gradual typing ; duck vs nominal vs structural ; `Any`, `Union`, `Optional`, `X | Y`
  - generics (`list[int]`, `dict[str, list[int]]`) ; `tuple[int, ...]` vs `tuple[int, str]`
  - `Iterable`/`Sequence`/`Mapping` (Liskov) ; `Callable[[...], R]` ; `TypeVar`
  - protocols static vs runtime ; `NoReturn` ; mypy
- [ ] **Ch 9 — Decorators and Closures** · tier S
  - syntaxe `@`, quand Python exécute les décorateurs ; LEGB ; closures, variables libres ; `nonlocal`
  - `lru_cache`/`cache`, `singledispatch` ; décorateurs paramétrés ; `functools.wraps` ; empilés ; classe vs fonction
- [ ] **Ch 10 — Design Patterns with First-Class Functions** · tier B
  - Strategy fonctions vs classes ; refactor patterns OO ; Command simplifié ; Pythonic vs GoF ; `globals()`

## Partie III — Object-Oriented Idioms

- [ ] **Ch 11 — A Pythonic Object** · tier S
  - `__repr__` vs `__str__` ; `classmethod` vs `staticmethod` ; `__format__` + mini-langage
  - hashabilité (`__hash__`+`__eq__`) ; attributs privés, name mangling ; `__slots__` ; class vs instance attrs
- [ ] **Ch 12 — Special Methods for Sequences** · tier A
  - séquence custom complète ; protocol vs interface ; `__getitem__` int+slice
  - `__len__`/`__iter__`/`__contains__` ; `functools.reduce` ; hashabilité ; `__getattr__` ; classe Vector
- [ ] **Ch 13 — Interfaces, Protocols, and ABCs** · tier A
  - duck typing ; goose typing ABC (`abc`, `abstractmethod`, `register`) ; `collections.abc`
  - virtual subclasses ; `typing.Protocol` (PEP 544), `runtime_checkable` ; ABC vs Protocol ; `numbers` ; `isinstance` controversé
- [ ] **Ch 14 — Inheritance: For Better or For Worse** · tier B
  - `super()` subtil ; MRO/C3 ; multiple inheritance, diamond ; mixins ; subclasser built-ins
  - `__init_subclass__` ; ABC vs mixin vs Protocol ; composition vs héritage
- [ ] **Ch 15 — More About Type Hints** · tier A
  - `@overload` ; `TypedDict` ; `cast` ; hints au runtime (`get_type_hints`)
  - generic classes user-defined ; variance (co/contra/invariance) ; generic protocols
- [ ] **Ch 16 — Operator Overloading** · tier B
  - règles & limites ; unaires (`__neg__`/`__pos__`/`__abs__`/`__invert__`)
  - binaires + reflected (`__add__`/`__radd__`) ; `NotImplemented` vs `NotImplementedError`
  - augmented (`__iadd__`) ; comparaisons riches + `functools.total_ordering`

## Partie IV — Control Flow

- [ ] **Ch 17 — Iterators, Generators, and Classic Coroutines** · tier S
  - protocole itération (`__iter__`/`__next__`/`StopIteration`) ; iterator vs iterable
  - `yield` ; generator expressions ; `itertools` (count/cycle/chain/groupby/tee/accumulate/…)
  - `yield from`, sub-generators ; iterator = son propre iterable ; coroutines classiques (`send`/`throw`/`close`) ; pipelines, lazy eval
- [ ] **Ch 18 — with, match, and else Blocks** · tier S
  - context managers (`__enter__`/`__exit__`) ; `contextlib` (`@contextmanager`, `closing`, `suppress`, `redirect_stdout`, `nullcontext`, `ExitStack`)
  - `try/else`, `for/else`, `while/else` ; `match`/`case` en profondeur (littéraux, capture, classes, séquences, mappings, `|`, guards, `_`)
- [ ] **Ch 19 — Concurrency Models in Python** · tier S
  - concurrency vs parallelism ; GIL ; threads/processes/coroutines ; I/O-bound vs CPU-bound
  - modèles séquentiel/thread/process/async ; spinner comparatif ; free-threading 3.13+
- [ ] **Ch 20 — Concurrent Executors** · tier A
  - `ThreadPoolExecutor`/`ProcessPoolExecutor` ; `Future`, `as_completed`, `map`
  - vs threads/processes à la main ; download parallèle ; progress bars, error handling ; thread vs process pool
- [ ] **Ch 21 — Asynchronous Programming** · tier S
  - `async def`/`await` ; event loop ; native vs classic coroutines vs generators
  - `asyncio` (`run`/`create_task`/`gather`/`wait`/`to_thread`) ; async iter/gen/`async for`
  - async context managers/`async with` ; 3 awaitables ; pièges (`await` oublié, blocking, mixing)

## Partie V — Metaprogramming

- [ ] **Ch 22 — Dynamic Attributes and Properties** · tier S · *optional*
  - data attrs vs properties ; `@property`/`@x.setter` ; `__getattr__`/`__setattr__`/`__delattr__`/`__getattribute__`
  - `__dir__`, `vars()`, `__dict__` ; validation ; computed/`cached_property`
- [ ] **Ch 23 — Attribute Descriptors** · tier B · *optional*
  - protocol descriptor (`__get__`/`__set__`/`__delete__`) ; data vs non-data
  - implémentation `property`/`classmethod`/`staticmethod`/méthodes ; storage ; `__set_name__` ; lookup order ; validation/ORM
- [ ] **Ch 24 — Class Metaprogramming** · tier B · *optional*
  - classes first-class ; `type(name, bases, dict)` ; class decorators ; `__init_subclass__`
  - metaclasses ; quand indispensable vs over-engineering ; registration/validation/frameworks

---

## Priorisation ML inference (angle Mistral, priorité décroissante)

- **Critique** : ch 1, 5, 7, 8, 17, 19, 20, 21, 22 — data model, dataclasses,
  fonctions, type hints, générateurs (fondation streaming), concurrency/asyncio
  (base FastAPI/inference servers), properties.
- **Très utile** : ch 2, 3, 9, 11, 12, 13, 15, 18 — collections optimales,
  décorateurs (PyTorch/vLLM/FastAPI), objets Pythonic, ABCs/Protocols (lecture
  codebases vLLM/Transformers), type hints avancés, context managers.
- **Culture / lecture** : ch 4 (Unicode → tokenisation), 6, 10, 14, 16, 23, 24.
- **Le plus dispensable si pressé** : ch 24 (metaclasses) — code metaclass-heavy
  rare en ML systems.

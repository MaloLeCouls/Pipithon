# Mapping exhaustif des compétences — ML Inference Engineer (catégorie 5) — visibilité Mistral, décembre 2027

**Date de cadrage** : 17 mai 2026
**Horizon de calibration** : décembre 2027 (sortie MS Télécom Paris IA)
**Cible primaire** : Mistral AI (Paris) — postes *Inference / Serving Engineer*, *ML Engineer Open-Source*, *SWE New Grad → Inference team*
**Cibles secondaires alignées** : NVIDIA Paris/Zurich (AI Inference Performance New Grad), Hugging Face, Together AI, Modal, Baseten, Cohere

---

## 0. Comment lire ce document

### 0.1 La philosophie de calibration

Tu candidates en décembre 2027 mais tu construis le profil **maintenant**, mai 2026. Le piège classique : viser le marché d'aujourd'hui. Or les compétences décisives en décembre 2027 sont celles qui sont **émergentes mai 2026** et **mainstream mi-2027**. Trois exemples concrets de ce décalage temporel :

1. La **désagrégation prefill/decode** était un sujet de papier en 2024, expérimental dans vLLM mi-2025, est devenue mainstream chez Meta/LinkedIn/Mistral/HuggingFace en production début 2026 (`vLLM`, `SGLang`, `NVIDIA Dynamo` GA, `llm-d` Red Hat/AWS). En décembre 2027 ce sera *table stakes*, pas un différenciateur.
2. **NVFP4 quantization** (Blackwell B200/GB200) — Mistral publie déjà ses checkpoints Large 3 en NVFP4 via `llm-compressor` (Red Hat). FP8 sera *baseline*, NVFP4 sera *standard production*.
3. **MoE expert parallelism** — Large 3 (675B/41B actifs), Small 4 (119B/6B actifs), DeepSeek, Kimi, Qwen — c'est devenu l'architecture dominante des frontier models open-weights. Tu dois maîtriser DeepEP, expert parallelism dans vLLM/SGLang, all-to-all NCCL.

→ La table ci-dessous calibre **niveau attendu mai 2026** (où tu dois être maintenant pour rester en piste) et **niveau attendu déc 2027** (ce qui sera testé en entretien).

### 0.2 Les 5 tiers de priorité

| Tier | Signification | Conséquence opérationnelle |
|---|---|---|
| **S** | Socle absolu. Impossible de passer un entretien Mistral cat 5 sans. | Drill quotidien jusqu'à maîtrise réflexe. |
| **A** | Très différenciant. Distingue le candidat "lu sur Twitter" du "vraiment fait". | 200-400h de pratique réelle, projets concrets. |
| **B** | Utile, solidifie le profil. | Couverture en lecture + 1 projet d'illustration. |
| **C** | Bonus, ouvre des portes adjacentes. | Connaître l'existence, savoir en parler 5 minutes. |
| **D** | Distraction. Ne pas y aller. | Ignorer activement, dire non. |

### 0.3 Sources d'autorité utilisées

- Prises de parole **Arthur Mensch** : audition Assemblée nationale 12 mai 2026, conférence Polytechnique 19 janvier 2026, Big Technology Podcast 16 janvier 2026, India AI Impact Summit février 2026, posts LinkedIn 2025-2026
- Prises de parole **Guillaume Lample** : VentureBeat décembre 2025
- **Release notes Mistral** : Large 3 (déc 2025), Ministral 3 (déc 2025), Small 4 (mars 2026), Medium 3.5 (avril 2026), Vibe CLI (déc 2025), EAGLE draft (avril 2026)
- **Job postings actuels Mistral** (lever.co/mistral, careers.mistral.ai, mai 2026)
- **Job postings NVIDIA** : AI Inference Performance Engineer New College Grad 2026
- État de l'art technique : papers vLLM, SGLang, FlashAttention 3, EAGLE-3, blogs Red Hat AI, Baseten, BentoML, NVIDIA Dynamo

---

## 1. Synthèse stratégique avant la table — ce que Mensch te dit en filigrane

Avant la cartographie technique, **cinq messages directs de Mensch** que tu dois internaliser parce qu'ils décident à quoi ressemble un bon profil à ses yeux :

1. **« Inference efficiency comme moat »** (cohérent avec ses critiques de la stratégie OpenAI/Anthropic au Big Technology Podcast et avec l'investissement Mistral dans vLLM/SGLang/EAGLE/NVFP4). Mistral ne veut pas dépenser des dizaines de milliards en compute, donc chaque token serveur coûte. Tu dois penser **€/token** avant **points de benchmark**.

2. **« Les ingénieurs n'écrivent plus de code »** (audition AN, mai 2026). Contradiction apparente avec « apprenez à coder sans IA » (Polytechnique, janvier 2026). Résolution : l'ingénieur cat 5 chez Mistral a *appris* à coder manuellement, *travaille* en supervisant des agents, et possède le mental model fin pour **débugger** ce que les agents ne savent pas faire — soit précisément les kernels CUDA/Triton, les schedulers GPU, le NCCL/InfiniBand.

3. **« Faire une thèse »** (Polytechnique). Recommandation explicite. À profil égal en décembre 2027, le candidat avec un PhD CIFRE pertinent passe avant. Si tu peux faire CIFRE Mistral × Veolia × Télécom Paris (énergie/eau × IA), c'est la trajectoire optimale.

4. **« Contribuer en open-source »** : non négociable côté Mistral. Le poste *ML Engineer Open-Source Software* exige explicitement : `Experience contributing to popular open-source libraries such as PyTorch, Tensorflow, JAX, vLLM, Transformers, Llama.cpp`. C'est *la* preuve sociale recevable.

5. **« Travailler à l'intersection des disciplines »** (Polytechnique). Ton profil ICAM + Télécom Paris + Veolia te place naturellement à l'intersection IA × industrie lourde. C'est ton angle unique — ne le sous-estime pas, **n'essaie pas de devenir un pur ML systems engineer générique** parce que tu seras un de 1 000.

---

## 2. Vue d'ensemble — tableau de bord des couches

| # | Couche | Tier dominant | Niveau mai 2026 attendu | Niveau déc 2027 attendu |
|---|---|---|---|---|
| 1 | Langages & systèmes (Python, C++, shell, Git) | S | Python solide ; C++ pas commencé | Python expert ; C++ lisible/débuggable |
| 2 | Maths & fondamentaux ML | S | Algèbre lin/calcul/probas en cours | Maîtrisé au niveau interview |
| 3 | Deep learning + Transformers internals | S | En apprentissage | Maîtrise active (savoir réimplémenter from scratch) |
| 4 | PyTorch hands-on | S | Solide | Expert, custom ops, profiler |
| 5 | LLM inference internals | **A → S** | À commencer sérieusement | Cœur du métier, maîtrise totale |
| 6 | GPU programming (Triton + CUDA lecture) | **A** | À démarrer T2 2027 | Triton actif, CUDA lecture experte |
| 7 | Quantization & compression | **A** | Compréhension conceptuelle | Pratique active FP8/NVFP4/GGUF |
| 8 | Distributed training & MoE | A | Notions FSDP/DeepSpeed | DP/TP/PP/EP + MoE expert parallelism |
| 9 | Inference frameworks (vLLM, SGLang, Dynamo, llm-d) | **A → S** | Lecture passive | Contributeur actif vLLM + SGLang |
| 10 | Speculative decoding & decoding advanced | A | Connaître les noms | EAGLE-2/3, Medusa pratique |
| 11 | Long-context & KV cache management | A | Conceptuel | Paged Attention, prefix caching, disagg |
| 12 | Profiling & benchmarking | A | À démarrer | Nsight, PyTorch Profiler, roofline |
| 13 | GPU cluster ops & infra | B → A | Découverte | SLURM, K8s+Volcano, InfiniBand, NCCL debug |
| 14 | MLOps production | B | Découverte FastAPI/Docker | Production-grade serving |
| 15 | Agents, MCP, sandboxing | **A** (signal Mensch fort) | Notions | MCP serveur custom, sandboxing |
| 16 | Open-source contribution (PRs réelles) | **S** | 0 PR mergée | 10-20 PRs mergées repos stratégiques |
| 17 | Soft skills cat 5 | S | Variable | Mature et démontrables |
| 18 | Vertical domain (Veolia / énergie / industrie) | A (unique différenciateur) | À construire | 1-2 projets publiés |
| 19 | Évaluation & evals (SWE-Bench, τ-bench, etc.) | A | Notions | Harness public sous ton nom |
| 20 | Veille & écosystème (papers, OSS, conf) | A | Émergent | Actif, visible, reconnu |

---

## 3. Couche par couche — tables exhaustives

### Couche 1 — Langages & systèmes

| Compétence | Tier | Niveau mai 2026 | Niveau déc 2027 | Pourquoi Mistral | Ressource clé |
|---|---|---|---|---|---|
| Python idiomatique : list/dict/set, complexités, mutabilité, copies | S | Solide | Expert réflexe | Toutes fiches Mistral exigent "Expert Python" | Fluent Python (Ramalho) ch 2-7 |
| Comprehensions (list, dict, set, generator) | S | Acquis | Réflexe | Idem | Fluent Python ch 17 |
| Decorators (with/without args, factories, classmethod, property) | S | Niveau intermédiaire | Expert | Standard codebases Mistral | Fluent Python ch 9 |
| Context managers (`__enter__/__exit__`, contextlib) | S | Basique | Expert | Gestion ressources GPU/files | Fluent Python ch 18 |
| Generators, iterators, lazy eval | S | Acquis | Réflexe | Streaming tokens, data pipelines | Fluent Python ch 17 |
| Dunder methods complètes (`__init__`, `__repr__`, `__eq__`, `__hash__`, `__iter__`, `__getitem__`, `__call__`) | S | Partiel | Maîtrisé | Code review de PRs vLLM/transformers | Fluent Python ch 1, 11 |
| Type hints, mypy, protocols | S | Notions | Expert | Codebases modernes Mistral typées | Fluent Python ch 8 |
| asyncio (event loops, async/await, asyncio.gather, asyncio.Queue) | S | Basique | Solide | Serveurs inference asynchrones | Fluent Python ch 21 |
| Performance Python : `cProfile`, `line_profiler`, `memory_profiler`, `py-spy` | A | À démarrer | Solide | Profiler vLLM workers | High Performance Python (Gorelick) |
| Cython/CFFI/pybind11/nanobind (lecture) | B | Découverte | Lecture confortable | Lire les bindings PyTorch ATen | docs nanobind |
| **C++ moderne (C++17/20)** : syntaxe, classes, templates simples | **A** | **Pas commencé** | Lecture + écriture basique | Lire/déboguer kernels vLLM C++, llama.cpp, PyTorch ATen | A Tour of C++ (Stroustrup) |
| C++ memory : stack/heap, pointers, references, smart pointers | A | Pas commencé | Solide | Idem | A Tour of C++ |
| C++ STL : vector, map, unordered_map, algorithms | A | Pas commencé | Solide | Idem | A Tour of C++ |
| C++ RAII, move semantics, perfect forwarding | A | Pas commencé | Compréhension | Lire codebase ATen | A Tour of C++ |
| CMake basique | B | Pas commencé | Lire un CMakeLists.txt | Compilation extensions PyTorch | CMake docs officiels |
| Linux command line (find, grep, sed, awk, pipes) | S | Variable | Expert | Indispensable cluster GPU | Linux Bible |
| Bash scripting (loops, conditions, traps) | S | Solide | Solide | Scripts de benchmarks | bashguide.org |
| Processus, signaux, htop, `nvidia-smi`, `nvtop`, `perf` | A | Découverte | Maîtrise | Debug OOM GPU, deadlocks NCCL | Linux Performance (Brendan Gregg) |
| Git avancé : rebase, cherry-pick, bisect, hooks | S | Intermédiaire | Expert | PRs vLLM, code review fluide | Pro Git (Chacon) |
| GitHub workflow : forks, draft PRs, code review, CI | S | Intermédiaire | Expert | Workflow OSS Mistral | docs GitHub |
| Docker : multi-stage builds, image optimization, layer caching | A | Découverte | Solide | NIM containers, déploiements | Docker Deep Dive (Poulton) |
| tmux/screen, vim/neovim de survie | B | Variable | Confortable | Sessions cluster persistantes | OMSCS guides |
| SSH, port forwarding, jump hosts | B | Solide | Confortable | Accès cluster Bruyères-le-Châtel | docs OpenSSH |
| Rust (lecture) | C | Pas commencé | Lecture confortable | Vibe CLI est Rust, optionnel | The Rust Book |
| Go (notions) | C | Pas commencé | Notions | K8s ecosystem | A Tour of Go |

**Signaux Mensch** : Mensch insiste à Polytechnique sur le fait de savoir coder **sans** IA pour comprendre le système. Concrètement : tape les exemples Fluent Python à la main, refais les exos C++ à la main, ne vibe-code pas tes premiers Triton. Le moment où l'agent te débloque doit être *choisi*, pas par défaut.

---

### Couche 2 — Maths & fondamentaux ML

| Compétence | Tier | Niveau mai 2026 | Niveau déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| Algèbre linéaire : vecteurs, matrices, produits, inverses, déterminants | S | En cours | Maîtrisé | Base absolue ML, questions interview | Mathematics for ML (Deisenroth) |
| Décompositions : SVD, QR, Cholesky, eigen | S | À acquérir | Confortable | Compréhension LoRA, attention low-rank | MathML |
| Norms (L1/L2/Frobenius), inégalité de Cauchy-Schwarz | A | À acquérir | Acquis | Régularisation, optimisation | MathML |
| Calcul : dérivées partielles, gradient, Jacobien, Hessienne | S | À acquérir | Confortable | Backprop, optimization | MathML |
| Règle de la chaîne multivariable | S | Notions | Maîtrisé | Backprop manuel | Karpathy micrograd |
| Probas : variables aléatoires, distributions usuelles, espérance, variance | S | À acquérir | Confortable | Sampling, dropout, RLHF | MathML |
| Estimation : MLE, MAP, KL divergence, entropie croisée | S | À acquérir | Confortable | Loss functions, alignment | MathML |
| Statistiques : tests d'hypothèse, intervalles de confiance | B | À acquérir | Notions | Benchmark variance, A/B | Statistics for ML |
| Optimisation : convexité, descente de gradient, momentum, Adam | S | En cours | Maîtrisé | Comprendre training dynamics | MathML + Hands-On ML |
| Information theory : entropie, perplexity, mutual information | A | À acquérir | Confortable | Perplexity-based evals | MathML |

**Note** : les maths ne se révisent pas en mode "lecture passive". Tu dois pouvoir au tableau dériver la backprop d'un MLP à 2 couches en 10 minutes, dériver l'attention et son gradient, et expliquer pourquoi `softmax(QK^T/√d)V` divise par √d.

---

### Couche 3 — Deep learning + Transformers internals

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| MLP : forward, backward, init (Xavier, He), activations | S | En cours | Réflexe | Base | Karpathy micrograd + makemore |
| Backprop manuelle (à la main, sans framework) | S | À démarrer | Réflexe | Filtre interview obligatoire | Karpathy "Spelled-out intro" |
| Batch normalization, LayerNorm, RMSNorm | S | Conceptuel | Maîtrisé | Mistral utilise RMSNorm dans ses LLMs | Lilian Weng blog |
| Mixed precision (FP16/BF16, AMP, master weights, gradient scaling) | S | À acquérir | Maîtrisé | Training et inference | PyTorch AMP docs |
| Optimizers (SGD, Adam, AdamW, Lion) | S | Notions | Confortable | Choisir un optimizer | Hands-On ML ch 11 |
| LR schedulers (cosine, warmup, linear) | S | Notions | Confortable | Training LLMs | Karpathy nanoGPT |
| Transformer architecture complète (encoder/decoder/enc-dec) | S | À acquérir solidement | **Réimplémentation from scratch** | Filtre interview obligatoire | Karpathy "Let's build GPT" |
| Self-attention scaled dot-product, multi-head | S | Notions | Réimplémentable | Idem | Attention Is All You Need |
| Cross-attention | A | Notions | Confortable | VLMs Mistral, multimodal | Papers |
| Positional encoding : sinusoidal, learned, **RoPE**, ALiBi | S | À acquérir | RoPE en particulier maîtrisé | Mistral utilise RoPE | RoFormer paper |
| **Sliding Window Attention (SWA)** | A | À acquérir | Maîtrisé | **Architecture Mistral 7B/Mixtral** | Mistral 7B paper |
| **Grouped Query Attention (GQA)** | S | À acquérir | Maîtrisé | Mistral 7B, Large, Medium | Mistral 7B paper |
| Multi-Query Attention (MQA) | A | Notions | Confortable | Inference efficiency | PaLM paper |
| **Mixture of Experts (MoE) — routing, capacity, gating** | **S** | À acquérir prio | Maîtrisé | **Large 3 (675B/41B), Small 4 (119B/6B), Mixtral** | Mixtral paper + Mistral Large 3 blog |
| Tokenization : BPE, SentencePiece, tiktoken, **Tekken (Mistral)** | S | Conceptuel | Maîtrisé | Tokenizer Mistral spécifique | mistral-common repo |
| Pretraining (next token prediction) | A | Conceptuel | Confortable | Comprendre pipeline complète | Karpathy |
| Fine-tuning : full FT, LoRA, QLoRA, adapters, prefix tuning | A | À acquérir | Pratique réelle | mistral-finetune | LoRA paper + PEFT docs |
| RLHF, DPO, PPO concepts | A | Conceptuel | Confortable | Alignment Mistral models | InstructGPT + DPO papers |
| Instruction tuning, chat templates Mistral | A | À acquérir | Maîtrisé | mistral-common, tool calling | mistral-common repo |
| Vision Transformers (ViT), CLIP-style encoders | A | Conceptuel | Confortable | Medium 3.5 vision encoder from scratch | ViT paper |

---

### Couche 4 — PyTorch hands-on

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| Tensors : ops, broadcasting, indexing avancé, contiguous | S | Solide | Réflexe | Code review fluide | PyTorch tutorials |
| Autograd, computation graph | S | Notions | Maîtrisé | Debug grad issues | PyTorch docs |
| `nn.Module`, custom layers, parameter management | S | Solide | Expert | Implémenter blocks custom | PyTorch tutorials |
| Datasets et DataLoaders, samplers, collate fns | S | Notions | Solide | Training pipelines | PyTorch tutorials |
| Training loop (manual, sans Lightning) | S | À pratiquer | Réflexe | Mistral teams custom loops | Karpathy |
| `torch.cuda.amp` mixed precision | A | À acquérir | Solide | Production training | PyTorch AMP |
| **DDP (DistributedDataParallel)** | A | À acquérir | Solide | Multi-GPU | PyTorch DDP tutorial |
| **FSDP (Fully Sharded Data Parallel)** | **A** | À acquérir prio | Maîtrisé | Training LLMs sur clusters | PyTorch FSDP tutorial |
| `torch.compile` (TorchDynamo, TorchInductor) | A | Notions | Solide | Speed-ups 2.x | PyTorch 2.x blog |
| `torch.fx` symbolic tracing (lecture) | B | Aucun | Lecture | Graph transformations | docs fx |
| Custom CUDA ops integration | B | Aucun | Lecture | Comprendre kernels custom dans vLLM | PyTorch C++ ext |
| TorchScript (culture) | C | Aucun | Notions | Deprecated, just know it exists | docs |
| PyTorch Profiler (trace events, kernels, memory timeline) | **A** | À acquérir | Expert | Profiler avant d'optimiser | PyTorch Profiler tutorial |
| Hooks (forward/backward) | B | Notions | Confortable | Debug, instrumentation | docs |
| State dict manipulation, checkpointing | B | Notions | Solide | Loading Mistral weights | docs |
| Quantization API (torch.ao.quantization) | A | Aucun | Confortable | Comprendre pipeline quantization | docs |

---

### Couche 5 — LLM inference internals (CŒUR DU MÉTIER)

C'est ici que se joue ta crédibilité cat 5. Chaque ligne de cette table doit être un sujet sur lequel tu peux parler **20 minutes au tableau** en décembre 2027.

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| **Prefill vs Decode** : nature compute-bound vs memory-bound | **S** | Conceptuel | Maîtrise totale | Distinction fondamentale de tout le métier | vLLM paper + Spheron blog disagg 2026 |
| **KV cache** : pourquoi, structure, coût mémoire par token | **S** | À acquérir | Réflexe | Question d'entretien certaine | vLLM paper |
| **Paged Attention** : block-based memory, fragmentation interne | **S** | À acquérir | Maîtrisé | Fondateur vLLM | vLLM paper (Kwon et al. 2023) |
| **Continuous batching** vs static batching | **S** | À acquérir | Maîtrisé | Throughput moderne | Orca paper |
| **Prefix caching** (vLLM APC, SGLang RadixAttention) | **A** | À acquérir | Maîtrisé | Multi-turn chat, system prompts | RadixAttention paper |
| **Chunked prefill** | A | À acquérir | Solide | Latence TTFT/ITL | vLLM docs |
| **Disaggregated prefill/decode** (NIXL, LMCache, PyNcclConnector) | **A** | Conceptuel | Maîtrisé | **Mainstream production 2026, Mistral en prod** | Spheron blog avril 2026 + vLLM docs disagg |
| **Speculative decoding** : draft + target model, acceptance ratio | **A** | Conceptuel | Maîtrisé | **Mistral publie EAGLE drafts** | Chen et al. 2023 |
| **EAGLE-2, EAGLE-3** | **A** | À acquérir | Pratique | **Mistral publie ses recipes EAGLE** | EAGLE papers + Mistral release notes Medium 3.5 |
| Lookahead decoding, Medusa | B | Notions | Confortable | Familles modernes | papers |
| Sampling : greedy, top-k, top-p, temperature, repetition penalty, min_p | S | Conceptuel | Maîtrisé | Tuning serveurs | HF generation docs |
| Beam search | C | Notions | Notions | Culture, peu utilisé en LLM modern | survol |
| Tensor parallelism (TP) | A | À acquérir | Maîtrisé | Serving sur 8 GPUs | Megatron-LM paper |
| Pipeline parallelism (PP) | A | À acquérir | Confortable | Modèles très gros | Megatron-LM paper |
| **Expert parallelism (EP)** pour MoE | **A** | À acquérir prio | Maîtrisé | **Large 3, Small 4 MoE** | DeepEP, vLLM expert_parallel |
| Sequence parallelism (SP) pour long context | A | À acquérir | Confortable | Contexte 256k Mistral | Ring Attention, USP |
| Constrained / structured decoding (JSON, guided) | A | Conceptuel | Solide | Tool calling Mistral, function calling | SGLang FSM, Outlines |
| Tool calling / function calling implementation | A | Conceptuel | Maîtrisé | Mistral tool-call-parser dans vLLM | vLLM docs Mistral |
| Streaming / SSE responses | A | Notions | Solide | API serving | FastAPI streaming |
| Backpressure, queueing, scheduling | A | Notions | Solide | Scheduler vLLM | vLLM scheduler code |

---

### Couche 6 — GPU programming (Triton + CUDA lecture)

**Stratégie** : Triton = arme principale (écrire), CUDA = lecture obligatoire. Démarrage T2 2027 selon plan d'apprentissage actuel.

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| **Triton** : modèle d'exécution (program_id, grids, blocks) | A | Aucun | Maîtrisé | OpenAI Triton est utilisé dans vLLM, FlashAttention 2/3 | triton-lang.org tutorials |
| Triton pointers, `tl.load`, `tl.store`, masking | A | Aucun | Maîtrisé | Idem | tutorials officiels |
| Triton memory hierarchy (registers, shared, global) | A | Aucun | Maîtrisé | Optimisation | tutorials |
| Triton tiling, broadcasting, auto-tuning (BLOCK_SIZE, num_warps) | A | Aucun | Maîtrisé | Tuning kernels | tutorials + GPU Puzzles |
| **Écrire matmul Triton from scratch** | A | Aucun | Réalisé | Le "hello world" | Sasha Rush GPU Puzzles |
| Écrire fused softmax Triton | A | Aucun | Réalisé | Pattern fondamental | tutorials |
| Écrire attention simplifiée Triton | A | Aucun | Réalisé | Comprendre FlashAttention | papers + tutorials |
| **Lire kernels Triton dans vLLM** (paged attention kernels) | A | Aucun | Confortable | Code review réelle | vLLM kernels/ |
| CUDA execution model : grid, block, thread, warp | A (lecture) | Aucun | Compris | Lire code source vLLM C++ | PMPP ch 1-7 |
| CUDA memory hierarchy : registers, shared, L1/L2, HBM | A | Aucun | Compris | Idem | PMPP |
| Coalescing, bank conflicts, occupancy | A | Aucun | Compris | Idem | PMPP |
| Tensor cores (concept) | A | Aucun | Compris | NVFP4, FP8 utilisation | NVIDIA docs |
| Lire matmul CUDA naïve puis tiled | A | Aucun | Confortable | Comprendre les fondamentaux | Simon Boehm blog |
| `nvcc`, compilation basique | B | Aucun | Notions | Build extensions | docs CUDA |
| **Nsight Compute** (analyse kernel) | A | Aucun | Solide | Profiler les kernels critiques | NVIDIA docs |
| **Nsight Systems** (system-wide traces) | A | Aucun | Solide | Profiler une inference complète | NVIDIA docs |
| FlashAttention 1/2/3 — savoir lire et expliquer | A | Aucun | Lecture experte | **State of the art attention** | Tri Dao papers |

**Compétence "écriture from scratch"** : à décembre 2027, tu dois pouvoir asseoir un recruteur Mistral et expliquer en 30 minutes ton implémentation Triton d'une attention fused, avec les choix de tiling et les courbes de speed-up sur ton DGX. C'est ton projet flagship cat 5.

---

### Couche 7 — Quantization & compression

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| Précisions : FP32, FP16, BF16 | S | Conceptuel | Maîtrisé | Base | docs PyTorch AMP |
| **FP8** (E4M3, E5M2) | A | Conceptuel | Maîtrisé | Hopper H100/H200, Blackwell | NVIDIA Transformer Engine |
| **NVFP4** | **A** | Connaître le nom | Maîtrisé | **Mistral Large 3 publié en NVFP4 via llm-compressor** | NVIDIA NVFP4 docs + Red Hat blog |
| INT8, INT4 | A | Conceptuel | Confortable | Edge | docs |
| FP4 / W4A16 | A | Conceptuel | Confortable | Frontier quantization | papers |
| **PTQ (Post-Training Quantization)** vs **QAT (Quantization-Aware Training)** | A | Conceptuel | Maîtrisé | Choix méthode selon use case | papers |
| **GPTQ** | A | Conceptuel | Pratique | Méthode standard | GPTQ paper |
| **AWQ** | A | Conceptuel | Pratique | Méthode standard | AWQ paper |
| **SmoothQuant** | B | Notions | Confortable | Activation quantization | paper |
| **GGUF (llama.cpp)** | A | Conceptuel | Pratique | Edge deployments, Ministral 3 | llama.cpp docs |
| **bitsandbytes** | B | Notions | Confortable | QLoRA, 8bit Adam | docs |
| **llm-compressor (Red Hat)** | A | Connaître | Pratique | **Mistral l'utilise officiellement** | docs vllm-project/llm-compressor |
| **Unsloth GGUF** | B | Notions | Pratique | Edge Ministral | Unsloth docs |
| Calibration datasets, layer-wise sensitivity | A | À acquérir | Solide | Quantization sérieuse | papers |
| Mesure dégradation : MMLU, HumanEval, perplexity | A | À acquérir | Solide | Quantization sérieuse | benchmarks |
| Pruning, distillation, sparsity | B | Notions | Confortable | Compression alternative | papers |

---

### Couche 8 — Distributed training & MoE

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| Data Parallelism (DP) | S | À acquérir | Maîtrisé | Base | PyTorch DDP tutorial |
| Tensor Parallelism (TP) | A | À acquérir | Maîtrisé | Serving + training | Megatron-LM |
| Pipeline Parallelism (PP) | A | À acquérir | Confortable | Très gros modèles | Megatron-LM |
| Sequence Parallelism (SP) | A | À acquérir | Confortable | Long context | Ring Attention, USP |
| **Expert Parallelism (EP)** pour MoE | **A** | À acquérir prio | Maîtrisé | **Large 3, Small 4** | DeepSpeed-MoE, DeepEP |
| **3D parallel hybrid** (DP+TP+PP) | A | À acquérir | Confortable | Training à 10k+ GPUs | Megatron-LM blog |
| **ZeRO stages 1, 2, 3** (DeepSpeed) | A | À acquérir | Maîtrisé | Memory optimization | DeepSpeed docs |
| **FSDP** comparaison ZeRO-3 | A | À acquérir | Maîtrisé | Standard PyTorch | docs |
| **NCCL primitives** : all-reduce, all-gather, reduce-scatter, broadcast | A | À acquérir | Maîtrisé | Debug réseau cluster | NCCL docs |
| **All-to-all** pour MoE | A | À acquérir | Maîtrisé | Routing MoE | NCCL + DeepEP |
| Communication overlap with compute | A | Notions | Solide | Performance critique | papers |
| Activation checkpointing | A | Notions | Solide | Memory optimization | PyTorch docs |
| Gradient accumulation | S | À acquérir | Réflexe | Base | PyTorch |
| **DeepSpeed-MoE, Megatron-Core MoE** | A | Aucun | Pratique | **Stack training MoE Mistral probable** | docs |
| Routing strategies : top-1, top-k, sinkhorn, expert choice | A | Notions | Maîtrisé | MoE design | papers |
| Load balancing, capacity factors | A | Notions | Maîtrisé | MoE production | papers |
| Curriculum learning, data scheduling | B | Notions | Confortable | Pretraining tricks | papers |

---

### Couche 9 — Inference frameworks (le combat principal)

**Stratégie de priorisation post-mai 2026** : `vLLM > SGLang > NVIDIA Dynamo > llm-d > llama.cpp > TGI`. TGI sort de la short-list, comme indiqué dans le rapport Mensch.

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| **vLLM** : architecture, scheduler, paged attention, comment ça fonctionne en interne | **S** | Lecture passive | Contributeur actif | **Documenté officiellement par Mistral pour chaque release** | vLLM docs + code source |
| vLLM : `tensor-parallel-size`, `--tool-call-parser mistral`, `--reasoning-parser mistral` | S | À acquérir | Réflexe | Run Mistral models officiellement | docs Mistral HF |
| **vLLM PRs mergées (objectif 3-5 minimum)** | **S** | 0 | 3-5 | **La preuve sociale Mistral #1** | vLLM issues |
| **SGLang** : architecture, RadixAttention, RadixAttention vs vLLM APC | **A** | Lecture | Contributeur | **Documenté officiellement par Mistral (cookbooks)** | SGLang docs + papers |
| SGLang : disaggregated prefill/decode (DeepEP normal vs low-latency mode) | A | Aucun | Solide | Production scale | SGLang docs |
| SGLang : constrained decoding (compressed FSM) | A | Aucun | Solide | Tool calling | SGLang docs |
| **NVIDIA Dynamo** (GTC 2025, GA 1.0) | A | Découverte | Pratique | Orchestration au-dessus de vLLM/SGLang/TRT-LLM | NVIDIA Dynamo docs |
| **llm-d** (Red Hat + AWS, K8s-native) | A | Découverte | Confortable | Sur AWS managed maintenant | llm-d docs |
| **TensorRT-LLM** | A | Lecture | Confortable | NVIDIA partnership Mistral | NVIDIA docs |
| **llama.cpp / GGUF** | A | Conceptuel | Pratique | Edge Ministral 3 | llama.cpp wiki |
| **NVIDIA NIM containers** | B | Découverte | Pratique | Mistral models en NIM officiellement | build.nvidia.com |
| Ollama | C | Connaître | Notions | Dev experience | docs |
| TGI (HuggingFace) | C | Notions | Notions | **Désinvestir** — sortie de la short-list Mistral | docs |
| Triton Inference Server (NVIDIA, pas le langage) | C | Notions | Notions | Couplé à TensorRT-LLM | docs |

**Action concrète mai 2026** : commence dès **juin 2026** à lire le code vLLM, ouvrir des issues, prendre des "good first issue". Tu n'as pas besoin d'avoir terminé le programme d'apprentissage pour ça. Une PR mergée fin 2026, c'est 5 PRs mergées fin 2027.

---

### Couche 10 — Speculative decoding & decoding avancé

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| Concept spec decoding : draft + target | A | Connaître | Maîtrisé | Sujet de pointe Mistral | Chen et al. 2023 |
| Acceptance ratio, expected speedup | A | Aucun | Compris | Métriques clés | papers |
| **EAGLE-1, EAGLE-2, EAGLE-3** | **A** | Connaître les noms | Pratique réelle | **Mistral publie EAGLE draft pour Medium 3.5** | EAGLE papers + cookbook |
| Medusa (multiple decoding heads) | B | Connaître | Confortable | Famille de techniques | paper |
| Lookahead decoding | B | Connaître | Notions | Alternative spec | paper |
| Self-speculative decoding | B | Connaître | Notions | Sans draft model séparé | papers |
| Tree-based draft (EAGLE-2 spécifique) | A | Aucun | Confortable | EAGLE state of the art | EAGLE-2 paper |
| Training un draft model | B | Aucun | Notions | Recipe Mistral | EAGLE training scripts |

---

### Couche 11 — Long-context & KV cache management

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| KV cache : taille = N_layers × N_heads × N_tokens × N_dim × 2 × bytes | S | À acquérir | Réflexe calcul mental | Comprendre coût mémoire | vLLM paper |
| Paged Attention | S | À acquérir | Maîtrisé | vLLM cœur | paper |
| Prefix caching (APC, RadixAttention) | A | À acquérir | Maîtrisé | Multi-turn, system prompts | papers |
| KV cache quantization (FP8/INT8 KV) | A | Conceptuel | Confortable | Long context cost | docs vLLM |
| Sliding window attention (KV éviction) | A | Conceptuel | Maîtrisé | **Mistral 7B/Mixtral** | Mistral 7B paper |
| Ring Attention | B | Connaître | Confortable | Long context training | paper |
| Tree Attention | B | Connaître | Notions | Alternative | paper |
| **Unified Sequence Parallelism (USP)** | B | Connaître | Notions | 256k Mistral | paper |
| RoPE scaling (NTK, YaRN, dynamic NTK) | A | Conceptuel | Confortable | Étendre contexte | papers |
| Disaggregated prefill (NIXL transport, LMCache) | A | Conceptuel | Maîtrisé | Production scale | Spheron blog 2026 |

---

### Couche 12 — Profiling & benchmarking

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| **Métriques** : tokens/sec, TTFT, ITL, MFU, HFU, memory bandwidth | A | À acquérir | Réflexe | Vocabulaire d'entretien | docs vLLM |
| **PyTorch Profiler** trace events, kernels, memory timeline | A | Découverte | Expert | Outil principal | PyTorch Profiler tutorial |
| **Nsight Systems** (system-wide) | A | Aucun | Solide | Profiler runs complets | NVIDIA docs |
| **Nsight Compute** (kernel-level) | A | Aucun | Solide | Optimisation kernel | NVIDIA docs |
| py-spy, scalene (Python pur) | B | Découverte | Confortable | Python bottlenecks | docs |
| Identifier compute-bound vs memory-bound vs comm-bound | A | Aucun | Réflexe | Choix d'optimisation | Roofline model |
| Roofline model | A | Aucun | Maîtrisé | Reasoning bottlenecks | NERSC tutorials |
| Benchmarks rigoureux : warmup, runs multiples, mediane vs moyenne | A | Aucun | Solide | Crédibilité résultats | best practices |
| Reproductibilité benchmarks (seeds, fixed input lengths) | A | Aucun | Solide | Publier des résultats utilisables | community standards |
| Lecture de papers de benchmark inference | A | Émergent | Actif | Veille Mistral | Together AI blog, etc. |

---

### Couche 13 — GPU cluster ops & infra

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| Linux server admin basique | B | Solide | Solide | Cluster Bruyères | docs |
| **SLURM** : sbatch, srun, squeue, partitions, srun debugging | A | Aucun | Solide | **Cluster Bruyères-le-Châtel + tout cluster HPC** | SLURM docs |
| **Kubernetes** : pods, services, deployments, GPU plugin | A | Découverte | Solide | NIM, Mistral Compute | K8s docs |
| **Volcano / KubeRay** | B | Aucun | Notions | GPU scheduling K8s | docs |
| **Helm charts** basique | B | Aucun | Lire/modifier | Déploiements | docs |
| **InfiniBand / NVLink / NVSwitch** | B | Aucun | Compris conceptuellement | Network fabric H100/H200 | NVIDIA docs |
| GPU health monitoring, MIG, MPS | B | Aucun | Notions | Cluster ops | NVIDIA docs |
| `nvidia-smi`, `nvtop`, `dcgmi` | A | Découverte | Réflexe | Outils quotidiens | docs |
| NCCL debugging (NCCL_DEBUG=INFO, env vars) | A | Aucun | Solide | Hangs/timeouts cluster | NCCL docs |
| Container GPU runtime (nvidia-container-toolkit) | B | Notions | Solide | NIM | docs |
| Bare-metal / air-gapped deployment | B | Aucun | Notions | Clients sovereign (HTX Singapour, Défense FR, ESA) | docs |
| Terraform / IaC (basique) | C | Aucun | Notions | DevOps | docs |
| Prometheus / Grafana monitoring | B | Notions | Solide | Observability serving | docs |

---

### Couche 14 — MLOps production & serving

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| **FastAPI** pour APIs ML | A | Notions | Solide | Standard serving Python | docs FastAPI |
| Pydantic validation | A | Notions | Solide | API design | docs |
| OpenAI-compatible API spec | A | Aucun | Maîtrisé | Standard inference servers | OpenAI API docs |
| Streaming SSE responses | A | Aucun | Solide | Tokens streaming | FastAPI |
| Rate limiting, queueing, backpressure | A | Aucun | Solide | Production serving | best practices |
| Caching strategies | B | Notions | Solide | Cost optimization | docs |
| Load balancing inference workers | A | Aucun | Solide | Scale-out | docs |
| Observability LLM : traces, metrics, logs | B | Notions | Solide | Production | OpenTelemetry, Datadog |
| Canary / shadow traffic | B | Notions | Notions | Deploy new versions | docs |
| A/B testing inference engines | B | Notions | Solide | Comparer vLLM vs SGLang | docs |
| Multi-LoRA serving | B | Aucun | Confortable | vLLM, SGLang | docs |

---

### Couche 15 — Agents, MCP & sandboxing (signal Mensch FORT)

**Pourquoi cette couche est critique** : Mistral mise lourdement sur Vibe (CLI + Remote Agents), Le Chat Work Mode, agents asynchrones cloud. Mensch parle de « delegate a ticket to a junior ». MCP est passé sous Linux Foundation Agentic AI Foundation en décembre 2025. C'est un signal Mensch direct.

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral | Ressource |
|---|---|---|---|---|---|
| **MCP (Model Context Protocol)** : concepts, stdio vs SSE | A | Notions | Maîtrisé | Standard ouvert, Mistral adopte | spec MCP |
| Écrire un serveur MCP custom (stdio + SSE) | A | Aucun | Réalisé | Différenciateur fort | docs MCP |
| Consommer des MCP connectors | A | Notions | Solide | Vibe ecosystem | docs |
| OAuth, token refresh dans contextes MCP | B | Aucun | Notions | Production MCP | docs |
| **Mistral Vibe CLI** (Apache 2.0) | A | Aucun | Pratique active | Coding agent Mistral officiel | github mistralai/vibe |
| Agent Communication Protocol (ACP) | B | Aucun | Notions | Vibe support | docs |
| Sandboxing : gVisor, Firecracker microVMs, isolated containers | A | Aucun | Solide | Vibe Remote, Code Interpreter Mistral | docs |
| Seccomp, capabilities | B | Aucun | Notions | Isolation | docs |
| Human-in-the-loop approval patterns | A | Aucun | Solide | Agents safety | papers |
| Tool-calling reliability (eval) | A | Aucun | Solide | Eval primary métrique agentique | τ-bench, τ³-Telecom |
| Multi-step success metrics | A | Aucun | Solide | Eval agents | SWE-Bench Verified |

---

### Couche 16 — Open-source contribution (la PREUVE SOCIALE non négociable)

Cette couche n'est pas optionnelle. La fiche officielle *Machine Learning Engineer, Open-Source Software* de Mistral exige : `Experience contributing to popular open-source libraries such as PyTorch, Tensorflow, JAX, vLLM, Transformers, Llama.cpp`.

| Repo cible | Priorité | Objectif déc 2027 | Raison |
|---|---|---|---|
| **vLLM** | **#1** | **3-5 PRs mergées** | Cité dans chaque release Mistral, plus large communauté inference |
| **SGLang** | **#2** | 1-3 PRs mergées | Cookbooks officiels Mistral |
| **Mistral Vibe CLI** | **#3** | 1-3 PRs mergées | Repo Mistral direct, visibilité maximale |
| **mistral-common** | #4 | 1-2 PRs mergées | Repo Mistral direct (tokenizer Tekken) |
| **mistral-inference** | #4 | 1-2 PRs mergées | Repo Mistral direct |
| **llama.cpp** | #5 | 1 PR mergée | Edge ecosystem |
| **llm-compressor** | #5 | 1 PR mergée | Stack Mistral × Red Hat NVFP4 |
| **transformers (HF)** | #6 | 1-2 PRs mergées | Communauté massive, moins prioritaire Mistral spécifique |
| **PyTorch core** | #7 | Optionnel | Très compétitif, ROI faible pour Mistral |
| **TensorRT-LLM** | #8 | Optionnel | NVIDIA, moins direct |

**Compétences transverses** :

| Compétence | Tier | mai 2026 | déc 2027 |
|---|---|---|---|
| Lire un codebase OSS complexe et naviguer | S | Émergent | Réflexe |
| Écrire un bon issue avec repro | S | Émergent | Réflexe |
| Écrire une PR claire, scopée, testée | S | Aucun | Maîtrisé |
| Code review constructive | A | Aucun | Solide |
| Discussion sur Discord vLLM / GPU Mode | A | Aucun | Visible |
| Documenter (docstrings, READMEs, changelogs) | A | Variable | Solide |
| Triager des issues sur un repo | B | Aucun | Notions |

---

### Couche 17 — Soft skills cat 5

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral |
|---|---|---|---|---|
| Communication écrite claire en anglais | S | Variable | Excellent | Tout le travail technique est en anglais |
| Capacité à expliquer un concept complexe simplement | S | Variable | Solide | Fiches Mistral le mentionnent partout |
| Ownership end-to-end (« ship features with minimal oversight ») | S | À démontrer | Démontrable via projets | Formule récurrente fiches Mistral |
| Self-starter / autonomy / fast-paced | S | À démontrer | Démontré | Culture Mistral codée |
| Curiosité technique active (papers, OSS, conf) | S | Émergent | Réflexe | Distingue les obsédés des candidats |
| Capacité à reviewer du code généré par IA (Mensch dixit) | A | À développer | Solide | Compétence émergente clé 2026-2027 |
| Tenir un journal de bugs IA, anti-patterns observés | A | Pas commencé | Tenu | Asset d'entretien différenciant |
| Réception du feedback technique sans ego | A | Variable | Solide | Code review culture |
| Travail en équipe distribuée (FR/UK/US/Singapore/Germany) | A | Variable | Confortable | Équipes Mistral réparties |
| Capacité à prioriser face à l'ambiguïté | A | Variable | Solide | Startup mindset |
| Anglais technique parlé (interviews, daily stand-ups) | S | Variable | Fluent | Indispensable |
| Capacité à dire « je ne sais pas » sans paniquer | A | Variable | Solide | Honnêteté technique |
| Vente / forward-deployment soft skills (reformuler problème métier en spec ML) | A | Émergent | Solide | Modèle embedded engineer Mistral |

---

### Couche 18 — Vertical domain (ton angle UNIQUE)

**C'est ici que tu peux casser le moule du candidat générique ML systems.** Mensch dit à Polytechnique : « travailler à l'intersection des disciplines ». Ton intersection : **IA × énergie/eau/industrie lourde via Veolia + Télécom Paris**.

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral |
|---|---|---|---|---|
| Connaissance domaine Veolia (digestion anaérobie, traitement eau, déchets) | A | En cours alternance | Maîtrisé | Domain expertise différenciante |
| Projet 1 : RL/IA pour optimisation procédé Veolia réel | A | À démarrer | Publié blog + repo | Démonstration vertical |
| Projet 2 : prédiction qualité eau ou maintenance prédictive | A | À démarrer | Publié | Idem |
| Simulateurs physiques + ML (sujet émergent Mensch) | B | Aucun | Notions | Sujet de pointe |
| Connaissance secteur défense / dual-use (partenariat Helsing, Armée FR) | B | Aucun | Notions | Mistral assume défense maintenant |
| Connaissance énergie / nucléaire (lié à Bruyères-le-Châtel + BNP nucléaire) | B | Aucun | Notions | Contexte stratégique |
| Lecture papers Mistral sur verticalisation (Forge) | A | Aucun | Actif | Veille |
| Capacité à reformuler un cas client en spec ML | A | Émergent | Solide | Modèle Forward Deployed |

---

### Couche 19 — Évaluation & evals

| Compétence | Tier | mai 2026 | déc 2027 | Pourquoi Mistral |
|---|---|---|---|---|
| Benchmarks classiques : MMLU, MMLU-Pro, HumanEval, GSM8K | S | Notions | Maîtrisé | Vocabulaire commun |
| **SWE-Bench Verified** | A | Connaître | Maîtrisé | Mistral score 77.6% sur Medium 3.5 |
| **τ-bench, τ³-Telecom** | A | Connaître | Maîtrisé | Mistral score 91.4% sur Medium 3.5 |
| LMArena / Arena Hard | A | Connaître | Maîtrisé | Référence chat |
| Construction de eval harness custom | A | Aucun | Réalisé | **Différenciateur entretien** |
| Reference tests, model-graded checks, heuristics | A | Notions | Solide | Eval moderne |
| Multilingual benchmarks (Mistral focus EU langues) | A | Aucun | Confortable | Différenciateur Mistral |
| Eval de tool-calling reliability | A | Aucun | Solide | Agents primary metric |
| LLM-as-judge biases, mitigations | A | Notions | Solide | Eval modernes |
| Publier un benchmark public sous ton nom | A | Aucun | Réalisé | Signal fort |

---

### Couche 20 — Veille & écosystème

| Activité | Tier | mai 2026 | déc 2027 |
|---|---|---|---|
| Suivre Twitter/X technique (Tri Dao, Lilian Weng, Horace He, Tim Dettmers, Sasha Rush, Soumith Chintala, Stas Bekman) | A | À démarrer | Actif quotidien |
| Lire 2-3 papers/semaine inference | A | Émergent | Routine |
| Lire papers Mistral (Mixtral, Mistral 7B, Codestral, Magistral, Medium 3.5 release notes) | S | À démarrer | Couvert |
| Discord GPU Mode | A | Pas encore | Présent actif |
| HuggingFace blog | A | Découverte | Suivi |
| NVIDIA developer blog | A | Découverte | Suivi |
| Together AI engineering blog | A | Découverte | Suivi |
| Conférences : MLSys, NeurIPS, ICML (au moins en watch-only) | B | Aucun | 1 conf live |
| Présence GitHub publique avec contributions visibles | S | Émergent | Forte |
| Blog technique personnel | A | Émergent | Établi (10+ posts) |
| LinkedIn aligné technique (pas générique) | A | À ajuster | Aligné |

---

## 4. Le DELTA mai 2026 → décembre 2027 — où tu dois progresser le plus vite

Si tu devais résumer ce mapping en 7 chantiers prioritaires pour les 18 prochains mois, dans l'ordre de ROI :

### Chantier 1 — Démarrer vLLM contribution dès juin 2026
**Pas besoin d'attendre d'être prêt.** Ouvre le repo, prends 2 "good first issues", commente, fais une première PR (probablement refusée, c'est OK). À fin 2026 tu vises **1 PR mergée**, à fin 2027 tu vises **3-5 PRs mergées**. C'est *le* signal social qui fait passer ton CV de "candidat possible" à "à shortlister".

### Chantier 2 — MoE expert parallelism (non négociable)
Pas mentionné dans ton plan d'apprentissage initial. À ajouter explicitement T3-T4 2026 : DeepSpeed-MoE, Megatron-Core MoE, expert parallelism vLLM/SGLang, routing & load balancing. Sans ça, tu ne peux pas tenir une conversation Mistral sérieuse sur leur architecture.

### Chantier 3 — Triton sérieux à partir de mai 2027
Calendrier respecté : tutorials officiels (semaine 1), Sasha Rush GPU Puzzles (semaines 2-3), Simon Boehm matmul translation (semaine 4), puis projets continus. Objectif décembre 2027 : **un fused attention Triton custom benchmarké sur ton DGX**, publié sur blog.

### Chantier 4 — Projet flagship inference benchmark suite
Démarrage T2 2027. Tu prends 3-5 modèles open-source (Mistral 7B, Ministral 3, Mistral Small 4, Llama, Qwen), tu les sers sur 3 engines (vLLM, SGLang, llama.cpp), tu mesures rigoureusement, tu publies sous ton nom. C'est *le* projet qu'un recruteur Mistral va regarder en premier.

### Chantier 5 — Compétences Mensch émergentes (MCP, agents, sandboxing)
Aspect le plus sous-estimé du plan initial. Mistral mise massivement sur Vibe + MCP + agents asynchrones. À ajouter : serveur MCP custom (1 projet T3 2026), contribution Vibe CLI (T1 2027), compréhension sandboxing (T2 2027 avec un projet de Code Interpreter mini).

### Chantier 6 — Quantization NVFP4/FP8 hands-on
Pas suffisamment couvert dans le plan initial. À ajouter T4 2026 - T1 2027 : pratiquer GPTQ/AWQ sur Mistral models, lire llm-compressor source, publier 1-2 benchmarks de quantization sur ton blog.

### Chantier 7 — Vertical Veolia comme angle propre
Probablement ton **meilleur ROI marginal**. Tu disposes d'un accès rare : données industrielles d'un grand groupe de services environnementaux. **1-2 projets IA × énergie/eau publiés** te placeront dans une catégorie distincte des 95% de candidats "ML systems génériques". À mener sur toute la durée 2026-2027.

---

## 5. Anti-patterns spécifiques cat 5 (à éviter activement)

1. **Le piège "j'ai compris en lisant"** : HPI + absorbtion rapide théorique = illusion de compétence. Si tu ne peux pas coder de mémoire l'exemple principal d'un chapitre Fluent Python, tu ne l'as pas appris. Test obligatoire : ferme le livre, code de mémoire.

2. **Le piège du framework-hopping** : ne te disperse pas sur 12 inference engines. Concentre-toi sur vLLM + SGLang principalement. NVIDIA Dynamo et llm-d en culture, pas en pratique deep.

3. **Le piège des LeetCode hard** : Mistral ne demande pas LeetCode hard exotique. Live coding 45 min standard, system design 45 min standard. Drill NeetCode Easy/Medium à 150 problèmes, mock interviews — pas plus.

4. **Le piège "1000 stars GitHub vs 5 PRs mergées"** : 5 PRs mergées dans vLLM/SGLang/Vibe valent infiniment plus que 1000 stars sur ton repo perso. Mesure la bonne métrique.

5. **Le piège "j'apprends C++ from scratch comme pour un job C++"** : non. Tu apprends C++ pour **lire** et **modifier marginalement** des codebases ML (vLLM C++ kernels, llama.cpp, PyTorch ATen). 100h de C++ ciblé suffisent — pas 500h de C++ avancé.

6. **Le piège du blog post générique** : éviter les "Introduction to LLM inference" qui existent à 1000 exemplaires. Vise des sujets différenciants : "I translated Simon Boehm's CUDA matmul to Triton, here's what I learned", "Benchmarking Mistral Ministral 3 on consumer hardware: 4 quantizations compared", "Why disaggregated prefill helps RAG workloads more than batch generation".

7. **Le piège "je vise uniquement Mistral"** : ton plan d'éventail (NVIDIA, HF, Together AI, Modal, Baseten, Cohere, Doctolib infra) est la bonne stratégie. Le profil que tu construis te rend candidat à 5 portes, pas 1. Ne sur-spécifie pas Mistral au point de devenir illisible pour les autres.

8. **Le piège du « je commencerai vLLM quand je serai prêt »** : tu ne seras jamais prêt. Commence en juin 2026 avec une PR ratée. C'est le seul moyen.

---

## 6. Trame de validation continue — comment savoir si tu restes en piste

Tous les 3 mois, audit personnel sur ces 12 indicateurs :

| Indicateur | Cible déc 2026 | Cible juin 2027 | Cible déc 2027 |
|---|---|---|---|
| PRs mergées vLLM/SGLang | 0-1 | 1-3 | 3-5 |
| Blog posts techniques publiés | 5 | 10 | 15-20 |
| Followers Twitter ML technique | 50-100 | 200-500 | 500-1000 |
| Projets flagship public | 0-1 (mini-GPT) | 1 V0 (benchmark suite) | 1-2 publiés solides |
| NeetCode problems résolus | 80 | 130 | 150+ |
| Mock interviews techniques | 0 | 3-5 | 10-15 |
| Présence Discord GPU Mode (messages contribuants) | Occasionnel | Régulier | Reconnaissable |
| Papers lus + résumés écrits | 20 | 50 | 80-100 |
| Réseau alumni / référents Mistral | 0 | 1-2 contacts | 3-5 |
| Stack technique pratique (sait faire) | Python + DL bases | Python + DL + Triton émergent + vLLM lecture | Tout le tier S + A en pratique |
| Vertical projet Veolia publié | 0 | V0 prototype | 1 publié solide |
| Anglais technique parlé (mock 30 min en EN) | Faisable mais hésitant | Confortable | Fluide |

Si à juin 2027 tu es sous **2/3 des cibles juin 2027**, alarme : il faut soit recalibrer le plan, soit envisager **CIFRE** (recommandation directe Mensch) qui te donne 3 ans supplémentaires plutôt qu'un saut new grad incertain.

---

## 7. Synthèse en une phrase

> **Pour être visible chez Mistral en décembre 2027, tu dois être à mi-2027 un Python+PyTorch expert qui contribue activement à vLLM/SGLang, comprend MoE expert parallelism et speculative decoding au point d'en parler 30 minutes, sait lire (pas forcément écrire) du C++/CUDA, a publié 1-2 projets différenciants (benchmark suite + vertical Veolia), et démontre via son GitHub/blog/Discord qu'il est un membre actif de la communauté open-source d'inférence européenne.**

Le reste est de l'exécution.

---

*Document évolutif. À relire et amender tous les 3 mois. Date de prochaine révision recommandée : 17 août 2026.*
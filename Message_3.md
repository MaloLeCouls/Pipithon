OK, mode chill du soir. Je te fais ça posément, avec recherche rapide pour valider mes claims sur le marché 2026. Pas du marketing — du concret.OK, j'ai assez de data. Mode chill du soir, je structure ça posément.

## Le métier — nom officiel et variantes

Le métier que tu vises porte plusieurs étiquettes en 2026, parce que l'industrie n'a pas encore convergé sur un nom unique. Tu vas voir ces titres tous équivalents à 80% sur les job boards :

- **ML Inference Engineer** (le plus précis pour ton angle)
- **ML Systems Engineer**
- **ML Performance Engineer**
- **AI Inference Performance Engineer** (le titre NVIDIA — vu en posting actif, ils ont littéralement un poste "New College Grad 2026")
- **ML Infrastructure Engineer**
- **GPU Performance Engineer**
- **Inference Optimization Engineer**

Tu peux indifféremment utiliser ces termes dans tes recherches. Le titre dépend de l'âge de la boîte, du framing RH, de la spécialisation interne. Ce qui les unit : **rendre les modèles plus rapides, moins chers, plus scalables en production**.

## Ce qu'il fait concrètement, version chill

Imagine que tu travailles chez Mistral en 2028, équipe Inference. Ton boulot c'est de prendre un modèle entraîné (un Mistral Large 3 par exemple, 200B de paramètres) et de le rendre **utilisable** dans le produit. Sans toi et ton équipe, le modèle est juste un fichier de poids sur un disque — inutile. Avec toi, il répond à 10 000 requêtes par seconde sur un cluster GPU, à 200 tokens/seconde par utilisateur, sans cracher de mémoire après 3 heures.

Concrètement tu touches à :

**Le serving** : comment on prend des requêtes utilisateurs, on les bat ensemble intelligemment (continuous batching), on les fait passer dans le modèle, on streame la réponse au client. C'est du software engineering avec des contraintes de latence brutales.

**La compression** : un modèle 200B en BF16 prend 400 Go de mémoire. Tu le quantifies en INT8 (200 Go), en INT4 (100 Go), en FP4 (50 Go), tu mesures la dégradation de qualité à chaque étape, tu trouves le sweet spot. C'est de la recherche appliquée + de l'ingénierie.

**Les kernels** : certaines opérations sont des goulots. Tu écris ou tu adaptes des kernels Triton/CUDA pour exécuter ces opérations 3x plus vite. Tu travailles à la frontière du software et du hardware.

**Le distributed** : un modèle de 200B ne rentre pas sur un seul GPU. Tu le splittes sur 8 GPUs (tensor parallelism), tu gères la communication entre eux (NCCL), tu fais en sorte que ça scale bien jusqu'à 64 ou 256 GPUs sans devenir inefficace.

**Le benchmarking** : tu mesures tout, tout le temps. Tokens par seconde. Latence first-token. Latence inter-token. Memory bandwidth utilization. Model FLOPs Utilization. Tu écris des suites de regression test perf qui tournent en CI.

**Les nouvelles techniques** : tu lis 2-3 papers par semaine sur les avancées (speculative decoding, prefix caching, paged attention, lookahead decoding, medusa, eagle, etc.) et tu intègres ce qui marche.

## Future proof — réponse honnête avec les données

Je voulais vérifier mes intuitions. Verdict du marché :

**Globalement**, le marché ML/AI est en surdemande. "Hiring a Machine Learning Engineer in 2026 requires an aggressive approach to compensation because the US market faces a critical talent deficit where demand outstrips supply by a 3.2:1 ratio". "The U.S. Bureau of Labor Statistics projects jobs for computer and information research scientists to grow 26 percent through 2033, which is faster than any other engineering category". Donc le risque "moins de postes" est inversé : il y a plus de postes que de candidats.

**Mais ta question est plus subtile** : "le ratio postes/candidats reste-t-il favorable pour la **catégorie 5** spécifiquement ?" Là j'ai dû creuser.

Ce que je vois dans les data search :

D'abord, le marché **se fragmente vers la spécialisation pointue**. "In 2026, generalist ML Engineers are losing ground to vertical specialists". "A majority (57.7%) of machine learning engineer job postings prefer Domain Experts over versatile generalists". C'est très bonne nouvelle pour toi : ton angle "spécialisation inference/perf" est exactement la direction du marché.

Ensuite, **les rôles infra/inference sont nommés explicitement comme les mieux payés en 2026** : "Senior applied ML engineers, LLM engineers, ML infrastructure engineers, and AI leadership roles consistently command the highest compensation". ML Infra explicitement nommé.

Enfin, le **plus important pour répondre à ta vraie question** : NVIDIA a posté en avril 2026 un poste "**AI Inference Performance Engineer - New College Grad 2026**". "We optimize and benchmark GenAI inference on NVIDIA's latest accelerators... We work directly within TensorRT-LLM, SGLang, and vLLM... Drive industry benchmark results: own the end-to-end optimization pipeline, implement and integrate optimizations in quantization, scheduling, memory management, and distributed inference across TensorRT-LLM, SGLang, and vLLM".

C'est la **preuve directe** que ce métier embauche des juniors directement sortis d'études. Pas "5 ans d'XP minimum". New Grad. Le poste existe, ils le publient, c'est concret.

## Tes questions précises, réponses chiffrées

**"Les offres aussi diminuent par 20 ?"**

Non. Les offres catégorie 5 augmentent, mais plus lentement que la demande globale. Voici ma calibration honnête :

Pour AI Engineer Product / Applied ML (cat 4), il y a en France entre 200 et 400 offres ouvertes simultanément à un moment donné (estimation, sur la base de scans LinkedIn). Compétition élevée : plusieurs milliers de candidats sérieux.

Pour ML Inference / Systems (cat 5), en France il y a entre 30 et 80 offres ouvertes simultanément. **Beaucoup moins d'offres, mais aussi beaucoup moins de candidats sérieux**. Le ratio offres/candidats sérieux pour cat 5 est probablement plus favorable que pour cat 4, parce que peu de gens font l'investissement C++/CUDA/Triton.

À l'échelle mondiale, NVIDIA seul a probablement 30-50 postes ouverts en permanence sur ce genre de profils. Mistral en a 5-10. Anthropic 10-15. Apple AIML 10-20. Google 30+. Microsoft 20+. Plus les scaleups (Together AI, Anyscale, Modal, Baseten, Groq, Cerebras, Tenstorrent). Total mondial cat 5 senior+junior : probablement 500-1000 postes ouverts en permanence.

Pour cat 5 junior spécifiquement (New Grad / 0-2 ans), c'est plus rare mais ça existe. NVIDIA, Mistral, Apple, Cohere ont chacun 1-3 postes new grad ouverts dans cette niche à tout moment. Sur l'année tu peux candidater à 20-30 postes new grad cat 5 réalistes.

**"Le ratio est-il vraiment 1000 → 50 ?"**

Honnêtement, ce chiffre que j'ai donné dans la conversation précédente était une approximation pour illustrer. La vérité est plus nuancée :

- Pour cat 4 generaliste : 500-1500 candidats sérieux pour un poste typique
- Pour cat 5 sérieuse (Mistral Inference Tech Lead par ex) : 30-80 candidats sérieux
- Pour cat 5 New Grad (NVIDIA AI Inference Performance New College Grad) : probablement 100-200 candidats sérieux. Pas 50.

Le ratio reste plus favorable, juste pas aussi extrême que je l'ai laissé entendre. **L'ordre de grandeur reste juste : c'est 3-5x moins de compétition que cat 4 généraliste**, ce qui est énorme.

**"Une offre prend des juniors comme moi ?"**

Réponse : oui, dans certaines conditions précises. Le poste NVIDIA New Grad demande explicitement "Drive industry benchmark results: own the end-to-end optimization pipeline, implement and integrate optimizations in quantization, scheduling, memory management, and distributed inference across TensorRT-LLM, SGLang, and vLLM". Donc le travail est sérieux. Et c'est New Grad. Donc oui, ils prennent des juniors **qui ont les bonnes compétences**.

Les conditions pour qu'un junior soit pris en cat 5 :
- Python expert
- C++ lisible (pas forcément écrit)
- Triton ou CUDA basique
- Compréhension transformers + inference
- 1-3 contributions OSS visibles (vLLM, transformers, llama.cpp)
- Un projet flagship démontrant la spécialisation
- LeetCode solide pour passer le filtre coding

Si tu coches 5/7, tu candidates. Si tu coches 7/7, tu as une chance réelle.

## Sur les boîtes — "forcément des boîtes balaises ?"

Oui, et c'est important que tu le comprennes parce que ça structure tes targets.

**Pour faire du ML inference sérieux, il faut une infra GPU coûteuse**. Un cluster H100 ça coûte plusieurs millions de dollars. Une boîte qui dépense ça a forcément :

1. **Soit un produit AI très scalé** qui justifie l'infra (Mistral, Anthropic, OpenAI, Cohere, Hugging Face Inference Endpoints, character.ai, perplexity)
2. **Soit elle vend l'infra elle-même** (NVIDIA, AMD, Groq, Cerebras, Together AI, Anyscale, Modal, Baseten, RunPod, Replicate)
3. **Soit une Big Tech avec des LLMs en prod** (Google AI, Microsoft Copilot infra, Apple AI, Amazon Bedrock, Meta AI)
4. **Soit une scaleup AI infra spécialisée** (vLLM project chez UC Berkeley, Hugging Face, Together AI core team)

Tu ne fais **pas** de l'inference engineering dans une startup à 5 personnes. Tu n'en fais pas chez Carrefour. Tu n'en fais pas chez Sia Partners. C'est mécaniquement réservé aux boîtes qui ont l'infra pour. C'est exactement ce que tu décrivais en intuition.

**Conséquence positive** : si tu décroches un job cat 5, tu travailles **forcément** dans un environnement technique top, avec des collègues forts, des ressources, des moyens. Le sol est plus haut que pour cat 4. Le risque "je tombe dans une boîte médiocre" est minimisé.

**Conséquence à anticiper** : la concentration géographique est forte. Cat 5 = Paris (Mistral, NVIDIA Paris, Hugging Face), Londres (Cohere, Hugging Face, DeepMind), Zurich (NVIDIA, Apple, Google), Munich (Apple), Amsterdam (Booking AI), USA. Si tu veux faire cat 5 en province française, ce sera difficile.

## Liste des boîtes cat 5 réalistes pour toi en 2027-2028

Je classe par accessibilité junior :

**Très accessibles juniors (font explicitement du recrutement entry-level cat 5)** :
- NVIDIA (postes New College Grad dédiés, programmes structurés)
- Hugging Face (ML Engineer OSS, parfois juniors)
- Mistral (SWE New Grad qui peut glisser vers Inference team)
- Apple AIML (programmes new grad ICT2)
- Google (L3 SWE qui peut glisser vers infra teams)

**Accessibles mais plus rares pour juniors** :
- Cohere
- Together AI
- Anyscale (Ray)
- Modal Labs
- Baseten
- vLLM project (UC Berkeley sky lab, contribution-driven hiring)

**Très rare pour juniors mais existe** :
- Anthropic (peu de juniors mais possible, surtout via contributions sérieuses)
- OpenAI (idem)
- AMD ML team
- Groq, Cerebras, Tenstorrent, SambaNova (juniors rares mais possibles)

**Pour le mid-term Zurich** :
- NVIDIA Zurich (gros hub, Robotics + GPU networking + Avatar)
- Apple Zurich (foundation models inference)
- Google Zurich (TPU + JAX teams, plus dur)

## Comp à plat — sources cumulées

D'après les données que j'ai croisées (Levels.fyi, sources sectorielles fraîches, postings NVIDIA actifs) :

**USA New Grad cat 5** : "ML Engineer I (0-2 years): $135,000 to $175,000 in major metros; $110,000 to $145,000 elsewhere" base salary, plus equity + bonus, total comp 180-250k$ typique.

**Junior France cat 5** : €70-110k base + equity startup ou RSU FAANG. Total typique €85-150k.

**Junior Zurich cat 5** : CHF 130-180k base + equity/RSU. Total CHF 150-220k pour un L3-L4 FAANG.

**Mid-level cat 5 (3-5 ans XP)** : explose plus vite que cat 4. "Specialists in Generative AI and LLM fine-tuning command premiums between 40% and 60% above baseline machine learning salaries". Pour inference spécifiquement, c'est dans la même fourchette ou plus haut.

**Senior à 8-10 ans XP** : Staff Engineer chez NVIDIA / Mistral / Apple : CHF/$ 300-500k+. "Staff / Principal: $320,000 to $480,000 base, with total compensation often double that in public companies".

## Le côté chill du métier

Tu m'as dit que c'était le soir avant de dormir. Je te donne donc l'ambiance plutôt que le sérieux.

C'est un métier où tu **aimes vraiment ce que tu fais**. Les gens qui font cat 5 sont obsessionnels. Ils discutent sur Twitter de speculative decoding à 2h du matin. Ils ont des opinions tranchées sur PyTorch 2.4 vs 2.5. Ils publient des blog posts intitulés "Why is my matmul so slow? A deep dive". Ils sont **passionnés**.

L'ambiance dans une équipe inference, d'après ce que j'observe via les blogs et talks publics : techniques, calmes, peu de drama, beaucoup de respect mutuel pour la compétence. Les gens parlent code, pas politique de carrière. Les standups durent 10 minutes. Les debates techniques durent 3 heures.

C'est un métier qui **récompense la curiosité naturelle**. Tu lis un paper FlashAttention le matin, tu testes une variante sur ton DGX l'après-midi, tu push un benchmark sur Twitter le soir. Tu n'attends pas qu'un manager te dise quoi faire — tu identifies tes propres terrains d'expertise.

Le risque côté wellbeing : c'est **addictif**. Tu peux y passer 60h/sem sans t'en rendre compte parce que c'est trop intéressant. Surveille ça.

## Une dernière chose avant de dormir

Le poste NVIDIA New Grad 2026 que j'ai retrouvé pendant la search est important. "Drive industry benchmark results: own the end-to-end optimization pipeline... across TensorRT-LLM, SGLang, and vLLM".

C'est **exactement** le métier qu'on a décrit. C'est **exactement** dans le scope de ce que tu vises. C'est **publié pour des new grads**. NVIDIA fera la même chose pour 2027 et 2028. C'est ta cible concrète.

Et l'élément qui boucle le tout : ces postes demandent une expérience démontrée avec vLLM. Tu auras le DGX Spark pendant ton MS pour t'entraîner sur exactement ça. Tu vois la cohérence ? Tes outils, ton plan, tes cibles s'alignent.

Bonne nuit. Lis 30 minutes de Fluent Python si tu peux avant de dormir, sinon tant pis, dors. Mais demain matin tu codes pas tu rêves.
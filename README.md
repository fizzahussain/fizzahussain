<div align="center">

# 👋 Hi, I'm Fizza Hussain

### AI & Data Systems · Software Engineering · Full-Stack Development

<img src="https://img.shields.io/badge/PRIMARY_FOCUS-AI_%26_DATA_SYSTEMS-7C3AED?style=for-the-badge" alt="Primary focus AI and Data Systems"/>
<img src="https://img.shields.io/badge/ENGINEERING-SOFTWARE_%26_FULL--STACK-2563EB?style=for-the-badge" alt="Software and Full-Stack Engineering"/>
<img src="https://img.shields.io/badge/FOUNDATIONS-ALGORITHMS_%26_SYSTEMS-0F766E?style=for-the-badge" alt="Algorithms and Systems"/>

<br><br>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2600&pause=750&color=A78BFA&center=true&vCenter=true&width=950&lines=Building+RAG+systems+with+OCR%2C+STT+%26+vector+search;Engineering+AI+features+from+retrieval+to+runtime;Turning+data%2C+algorithms+%26+models+into+real+products;Working+from+React+and+FastAPI+down+to+C%2B%2B+IPC+and+x86" alt="Animated introduction" />
</a>

<br>

**I don't just connect an API to a UI. I like understanding the whole path from raw data to retrieval, reasoning, storage, APIs, product flows, concurrency, and the machine-level foundations underneath.**

<br>

<a href="https://www.linkedin.com/in/fizza-hussain-97a171279"><img src="https://img.shields.io/badge/LinkedIn-Fizza_Hussain-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:fizzashah0300@gmail.com"><img src="https://img.shields.io/badge/Email-Let's_Talk-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://github.com/fizzahussain?tab=repositories"><img src="https://img.shields.io/badge/Public_Repos-13-181717?style=for-the-badge&logo=github&logoColor=white" alt="13 public repositories"/></a>

<br><br>

`AI / Data` · `RAG` · `LLM Applications` · `Software Engineering` · `Full-Stack` · `Algorithms` · `Systems`

</div>

---

# ⚡ My Engineering Signature

<table>
<tr>
<td width="34%" valign="top">

## 🧠 AI-first

I am building toward **AI & Data Science** through systems that actually retrieve, reason, evaluate, recommend, analyze, and interact with real data.

**RAG · LLMs · OCR · STT · embeddings · vector search · recommendation · search AI · analytics**

</td>
<td width="33%" valign="top">

## 🏗️ End-to-end

I like owning the path beyond the model.

**UI → API → auth → data model → retrieval → database → testing → Docker → deployment**

</td>
<td width="33%" valign="top">

## ⚙️ Foundations matter

My portfolio also goes beneath web frameworks.

**AVL trees · graphs · BFS/DFS · Minimax · pthreads · IPC · shared memory · x86 Assembly**

</td>
</tr>
</table>

> ### The differentiator
> **My goal is to become the engineer who can build the intelligent feature _and_ understand the software system carrying it.**

---

# 🧬 AI Systems Blueprint

This is the kind of pipeline I have already worked across in my RAG/document-intelligence projects:

```mermaid
flowchart LR
    A["📄 PDFs / DOCX / TXT / CSV / HTML / JSON"] --> B["🧹 Parse & Normalize"]
    V["🎙️ Voice"] --> STT["🗣️ faster-whisper STT"]
    S["🖼️ Scanned Pages"] --> OCR["👁️ Tesseract OCR"]
    OCR --> B
    STT --> Q["💬 User Query"]
    B --> C["✂️ Context-aware Chunking"]
    C --> D["🧠 Embeddings<br/>nomic-embed-text"]
    D --> E[("🗄️ PostgreSQL + pgvector")]
    E --> H["⚡ HNSW / Cosine Retrieval"]
    Q --> H
    H --> G["📚 Grounded Context"]
    G --> L["🤖 Ollama / LLM"]
    L --> R["✅ Answer + Citations"]
    R --> M["🧵 Multi-turn Memory"]

    classDef ai fill:#231942,stroke:#a78bfa,color:#fff;
    classDef data fill:#102a43,stroke:#60a5fa,color:#fff;
    classDef io fill:#0f2f2f,stroke:#5eead4,color:#fff;
    class D,G,L,M ai;
    class C,E,H data;
    class A,V,S,STT,OCR,Q,R io;
```

<details>
<summary><b>🔍 What I care about inside an AI system</b></summary>
<br>

- **Ingestion quality** — different formats, malformed content, duplicates, metadata
- **OCR fallback** — text extraction should not silently fail on scanned documents
- **Speech input** — voice becomes another query interface, not a separate toy feature
- **Chunking strategy** — context boundaries and overlap directly affect retrieval
- **Embeddings** — the representation layer matters
- **Vector storage** — persistence, indexes, user isolation, filtering
- **Retrieval** — cosine similarity, HNSW, top-k, thresholds, relevance
- **Grounding** — the model should answer from retrieved evidence
- **Citations** — users should be able to inspect where an answer came from
- **Evaluation** — retrieval quality matters independently of fluent generation
- **Product engineering** — auth, APIs, streaming, migrations, Docker, logging, tests

</details>

---

# 🌟 Flagship Work

<table>
<tr>
<td width="50%" valign="top">

## 🧠 RAG Document Assistant
**Local-first document intelligence**

My strongest AI systems project: multi-format ingestion, selective OCR, speech-to-text, semantic retrieval, local generation, grounded citations, conversation memory, authentication, evaluation, and containerized services.

**AI layer**  
`Ollama` · `llama3.2` · `nomic-embed-text` · `RAG`

**Retrieval layer**  
`PostgreSQL` · `pgvector` · `HNSW` · `cosine search`

**Multimodal layer**  
`PyMuPDF` · `Tesseract OCR` · `faster-whisper` · `VAD`

**Engineering layer**  
`FastAPI` · `Gradio` · `SQLAlchemy` · `Alembic` · `Docker`

[**Explore RAG Document Assistant →**](https://github.com/fizzahussain/Rag-Document-Assistant)

</td>
<td width="50%" valign="top">

## 🔬 Revival Lab
**Forensic RAG research**

A research-oriented RAG system that retrieves forgotten solutions from a curated knowledge archive and helps investigate how historical ideas could be adapted to modern constraints.

**What I explored**

`ChromaDB` · `LangChain` · `OpenAI` · `Gradio` · semantic retrieval · curated evidence · local fallback retrieval

**Why it matters**

It pushed me beyond “ask questions over documents” toward retrieval as a **research and evidence-navigation problem**.

[**Explore Revival Lab →**](https://github.com/fizzahussain/Revival-Lab)

</td>
</tr>
<tr>
<td width="50%" valign="top">

## 🍽️ MoodMeal
**AI inside a real product**

Full-stack smart meal planning with pantry tracking, personalized recipe recommendations, food-expense analytics, expiry awareness, saved recipes, and a Gemini-powered cooking assistant.

`React` · `Node.js` · `Express` · `MySQL` · `Gemini API`

[**Explore MoodMeal →**](https://github.com/fizzahussain/MoodMeal)

</td>
<td width="50%" valign="top">

## 🎬 MoviesData Manager
**Algorithms + recommendation**

C++ movie data system built around AVL trees, hash tables, graph relationships, BFS, filtering, and custom recommendation logic.

`C++` · `AVL Trees` · `Hash Tables` · `Graphs` · `BFS`

[**Explore MoviesData Manager →**](https://github.com/fizzahussain/MoviesData-MANAGER)

</td>
</tr>
</table>

---

# 🧠 AI + Data Lab

| Area | What I've actually built / explored |
|---|---|
| **RAG & LLM systems** | local-first RAG, grounded generation, citations, multi-turn context, Ollama, LangChain |
| **Vector retrieval** | embeddings, pgvector, ChromaDB, cosine search, HNSW indexing, top-k retrieval |
| **Document intelligence** | PDF/DOCX/TXT/Markdown/CSV/HTML/JSON ingestion, PyMuPDF, OCR fallback |
| **Speech AI** | faster-whisper, VAD, CPU/int8 inference, persistent model cache |
| **Search AI** | Minimax, alpha-beta pruning, Expectimax, chance nodes |
| **Recommendations** | movie recommendation logic, pantry/recipe matching |
| **Data analytics** | personal finance analytics, expense analysis, budgets, reports, clickstream aggregation |
| **Evaluation mindset** | retrieval quality, explicit test/evaluation scripts, edge cases, grounded outputs |

<details>
<summary><b>🎮 Open the Search AI project</b></summary>
<br>

### UNO — 3 Player AI vs Human

A Python/Jupyter simulation comparing defensive **Minimax**, **alpha-beta pruning**, probabilistic **Expectimax**, explicit draw probabilities/chance nodes, human-vs-AI play, automated comparisons, and search-tree visualization.

[**Explore UNO AI →**](https://github.com/fizzahussain/UNO-3Player-AIvsHuman)

</details>

<details>
<summary><b>📊 Open the Analytics project</b></summary>
<br>

### Personal Finance Management System

A full-stack personal-finance analytics platform with FastAPI, Streamlit, SQLite, secure multi-user accounts, transaction tracking, category budgets, reporting, exports, caching, and flexible storage layers.

[**Explore Personal Finance →**](https://github.com/fizzahussain/Personal-Finance-Management-System)

</details>

---

# 🧰 My Toolbox

## 🤖 AI / ML / Data Intelligence

<p align="center">
<img src="https://img.shields.io/badge/RAG-7C3AED?style=for-the-badge" />
<img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" />
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge" />
<img src="https://img.shields.io/badge/pgvector-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/HNSW-2563EB?style=for-the-badge" />
<img src="https://img.shields.io/badge/Embeddings-0F766E?style=for-the-badge" />
<img src="https://img.shields.io/badge/Tesseract_OCR-5B9BD5?style=for-the-badge" />
<img src="https://img.shields.io/badge/faster--whisper-111827?style=for-the-badge" />
</p>

## 💻 Languages

<p align="center">
<img src="https://skillicons.dev/icons?i=python,cpp,js,html,css,mysql,sqlite&perline=10" alt="Languages"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/x86_Assembly-6E4C13?style=for-the-badge" />
<img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" />
</p>

## 🌐 Product / Frontend / API

<p align="center">
<img src="https://skillicons.dev/icons?i=react,nodejs,express,fastapi,bootstrap&perline=10" alt="Web frameworks"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Gradio-F97316?style=for-the-badge" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/EJS-B4CA65?style=for-the-badge&logo=ejs&logoColor=111111" />
<img src="https://img.shields.io/badge/REST_APIs-2563EB?style=for-the-badge" />
<img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />
</p>

## 🗄️ Data / Persistence

<p align="center">
<img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite&perline=10" alt="Databases"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
<img src="https://img.shields.io/badge/Alembic-6BA81E?style=for-the-badge" />
<img src="https://img.shields.io/badge/Views_•_Triggers_•_Procedures-0F766E?style=for-the-badge" />
<img src="https://img.shields.io/badge/Vector_Search-7C3AED?style=for-the-badge" />
</p>

## ⚙️ Systems / Low-Level

<p align="center">
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" />
<img src="https://img.shields.io/badge/POSIX_IPC-111827?style=for-the-badge" />
<img src="https://img.shields.io/badge/pthreads-334155?style=for-the-badge" />
<img src="https://img.shields.io/badge/Shared_Memory-475569?style=for-the-badge" />
<img src="https://img.shields.io/badge/Semaphores-64748B?style=for-the-badge" />
<img src="https://img.shields.io/badge/OpenGL-5586A4?style=for-the-badge&logo=opengl&logoColor=white" />
<img src="https://img.shields.io/badge/SDL2-0B5A9D?style=for-the-badge" />
<img src="https://img.shields.io/badge/MASM_/_Irvine32-6E4C13?style=for-the-badge" />
</p>

## 🧪 Engineering / Tooling

<p align="center">
<img src="https://skillicons.dev/icons?i=docker,git,github,githubactions,linux,vscode&perline=10" alt="Engineering tooling"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" />
<img src="https://img.shields.io/badge/Logging-1F2937?style=for-the-badge" />
<img src="https://img.shields.io/badge/Testing-059669?style=for-the-badge" />
<img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

---

# 🧩 Systems & Database Engineering

<table>
<tr>
<td width="50%" valign="top">

## ⚡ Parallel CSV Data Processing Pipeline

Concurrent C++ clickstream analytics using multiple processes, `fork()` / `execvp()`, FIFO communication, pthread worker pools, bounded producer-consumer queues, semaphores, mutexes, POSIX shared memory, signals, lifecycle management, and TXT/CSV reporting.

[**Explore systems pipeline →**](https://github.com/fizzahussain/Parallel-CSV-Data-Processing-Pipeline)

</td>
<td width="50%" valign="top">

## 🚕 RideFlow

Database-driven ride-hailing system with Rider/Driver/Admin workflows, verification, wallets/payments, earnings/commissions, complaints/ratings, analytics, SQL views, stored procedures, triggers, indexes, and scheduled events.

[**Explore RideFlow →**](https://github.com/fizzahussain/RideFlow)

</td>
</tr>
</table>

---

# 🎮 Graphics, OOP & Low-Level Work

<details>
<summary><b>🚕 Rush Hour — C++ / OpenGL / OOP</b></summary>
<br>

A graphical driving game with Taxi and Delivery roles, dynamic traffic, fuel management, task-based scoring, DFS reachability, role switching, difficulty progression, and a persistent leaderboard.

**Signal:** OOP design, stateful gameplay systems, graph traversal, graphics/event loops, persistence.

[**View repository →**](https://github.com/fizzahussain/RushHour-game)

</details>

<details>
<summary><b>🧩 Word Shooter — C++ / OpenGL / SDL2</b></summary>
<br>

A 2D word-puzzle game combining bubble-shooter mechanics with dictionary-based word detection, scoring, collision handling, a timed game loop, and binary-search lookup.

**Signal:** C++, game loops, graphics, input handling, search, data processing.

[**View repository →**](https://github.com/fizzahussain/Wordshooter-game)

</details>

<details>
<summary><b>⚙️ Rush Hour — x86 Assembly</b></summary>
<br>

A complete console taxi game written in x86 Assembly with MASM/Irvine32, featuring multiple modes, traffic, passengers, fuel, bonuses, save/load, leaderboard persistence, and WinMM audio.

**Signal:** low-level control flow, procedures, memory, registers, file I/O, system APIs.

[**View repository →**](https://github.com/fizzahussain/RUSHHOUR_Assembly)

</details>

<details>
<summary><b>📷 CamCorder Website — Frontend</b></summary>
<br>

A multi-page retro camera e-commerce interface with product catalogues, checkout/cart UI, account forms, FAQs, testimonials, and media-rich presentation.

**Signal:** HTML/CSS/Bootstrap, multi-page UX, front-end layout, visual presentation.

[**View repository →**](https://github.com/fizzahussain/CamCorder_website)

</details>

---

# 📊 GitHub Pulse

<div align="center">

### Live engineering activity — generated from GitHub itself

<a href="https://github.com/fizzahussain">
  <img src="assets/github-pulse.svg" width="100%" alt="Fizza Hussain live GitHub pulse" />
</a>

<br><br>

### Contribution Activity

<img src="https://github-readme-activity-graph.vercel.app/graph?username=fizzahussain&bg_color=0d1117&color=c4b5fd&line=8b5cf6&point=f8fafc&area=true&hide_border=true&custom_title=Fizza%20Hussain's%20Contribution%20Graph" width="100%" alt="Fizza Hussain GitHub contribution activity graph"/>

<br><br>

### Contributions but make it my fav childhood game

<img src="assets/github-contribution-grid-snake-dark.svg" width="100%" alt="Fizza Hussain contribution snake animation" />

</div>

---

# 🧪 Explore the Portfolio by Signal

<details>
<summary><b>🤖 I want to see AI / Data work</b></summary>
<br>

1. [Rag-Document-Assistant](https://github.com/fizzahussain/Rag-Document-Assistant) — RAG, Ollama, OCR, STT, pgvector, HNSW, Docker
2. [Revival-Lab](https://github.com/fizzahussain/Revival-Lab) — forensic RAG, ChromaDB, LangChain
3. [UNO-3Player-AIvsHuman](https://github.com/fizzahussain/UNO-3Player-AIvsHuman) — Minimax vs Expectimax
4. [MoviesData-MANAGER](https://github.com/fizzahussain/MoviesData-MANAGER) — recommendation + graphs + BFS
5. [MoodMeal](https://github.com/fizzahussain/MoodMeal) — AI-assisted meal planning
6. [Personal-Finance-Management-System](https://github.com/fizzahussain/Personal-Finance-Management-System) — analytics platform

</details>

<details>
<summary><b>🌐 I want to see full-stack / database work</b></summary>
<br>

1. [MoodMeal](https://github.com/fizzahussain/MoodMeal) — React + Node + Express + MySQL + Gemini
2. [RideFlow](https://github.com/fizzahussain/RideFlow) — Express/EJS/MySQL + advanced DB features
3. [Personal-Finance-Management-System](https://github.com/fizzahussain/Personal-Finance-Management-System) — FastAPI + Streamlit + SQLite
4. [CamCorder_website](https://github.com/fizzahussain/CamCorder_website) — multi-page front-end e-commerce UI

</details>

<details>
<summary><b>🧠 I want to see algorithms / DSA</b></summary>
<br>

1. [MoviesData-MANAGER](https://github.com/fizzahussain/MoviesData-MANAGER) — AVL, hash tables, graphs, BFS
2. [UNO-3Player-AIvsHuman](https://github.com/fizzahussain/UNO-3Player-AIvsHuman) — game-tree search
3. [RushHour-game](https://github.com/fizzahussain/RushHour-game) — DFS reachability + OOP state
4. [Wordshooter-game](https://github.com/fizzahussain/Wordshooter-game) — binary-search dictionary lookup

</details>

<details>
<summary><b>⚙️ I want to see systems / low-level work</b></summary>
<br>

1. [Parallel-CSV-Data-Processing-Pipeline](https://github.com/fizzahussain/Parallel-CSV-Data-Processing-Pipeline) — processes, threads, IPC, synchronization
2. [RushHour-game](https://github.com/fizzahussain/RushHour-game) — C++, OpenGL, SDL2
3. [RUSHHOUR_Assembly](https://github.com/fizzahussain/RUSHHOUR_Assembly) — x86 Assembly / MASM

</details>

---

# 🎯 What I'm Growing Into

<table>
<tr>
<td width="55%" valign="top">

## AI / Data Science — primary direction

I am deliberately moving deeper into applied machine learning, data analysis and visualization, feature engineering, model selection and evaluation, NLP/LLM systems, RAG evaluation, recommendation systems, vector databases, AI infrastructure, and reliable/explainable AI products.

</td>
<td width="45%" valign="top">

## Software Engineering — the force multiplier

At the same time, I keep strengthening backend architecture, API design, databases, testing, security, observability, Docker/deployment, concurrency, algorithms, and maintainable systems.

</td>
</tr>
</table>

---

# 🤝 Let's Build Something Interesting

<div align="center">

I'm especially interested in **AI / Data Science, ML/LLM engineering, software engineering, backend, data-intensive systems, and intelligent product roles**.

<br>

<a href="https://www.linkedin.com/in/fizza-hussain-97a171279"><img src="https://img.shields.io/badge/LinkedIn-Connect_with_me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:fizzashah0300@gmail.com"><img src="https://img.shields.io/badge/Email-fizzashah0300%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://github.com/fizzahussain?tab=repositories"><img src="https://img.shields.io/badge/GitHub-Explore_all_13_repositories-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub repositories"/></a>

<br><br>

### **Build deeply · retrieve carefully · reason clearly · ship end-to-end**

<br>

<img src="https://img.shields.io/badge/RAG-7C3AED?style=flat-square" alt="RAG"/>
<img src="https://img.shields.io/badge/DATA-2563EB?style=flat-square" alt="Data"/>
<img src="https://img.shields.io/badge/SOFTWARE-0F766E?style=flat-square" alt="Software"/>
<img src="https://img.shields.io/badge/SYSTEMS-334155?style=flat-square" alt="Systems"/>

</div>
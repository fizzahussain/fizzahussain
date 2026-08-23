<div align="center">

# 👋 Hi, I'm Fizza Hussain

### BS Data Science · FAST-NUCES Islamabad

<img src="https://img.shields.io/badge/AI_%26_DATA-7C3AED?style=for-the-badge" alt="AI and Data"/>
<img src="https://img.shields.io/badge/SOFTWARE-2563EB?style=for-the-badge" alt="Software"/>
<img src="https://img.shields.io/badge/ALGORITHMS_%26_SYSTEMS-0F766E?style=for-the-badge" alt="Algorithms and Systems"/>

<br><br>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2600&pause=750&color=A78BFA&center=true&vCenter=true&width=950&lines=Building+projects+to+understand+how+things+work;Learning+to+build+with+AI+as+a+tool;From+algorithms+and+data+to+working+applications" alt="Animated introduction" />
</a>

<br>

I'm a **third-year BS Data Science student at FAST-NUCES Islamabad**. I like figuring out how things work and then trying to build them myself, from algorithms and data projects to web applications and AI-powered tools.

I'm especially interested in **AI/ML, Data Science, NLP, and building applications around models and data**, while continuing to strengthen my software engineering and systems fundamentals.

<br>

<a href="https://www.linkedin.com/in/fizza-hussain-97a171279"><img src="https://img.shields.io/badge/LinkedIn-Fizza_Hussain-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:fizzashah0300@gmail.com"><img src="https://img.shields.io/badge/Email-Let's_Talk-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://github.com/fizzahussain?tab=repositories"><img src="https://img.shields.io/badge/GitHub-Projects-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub projects"/></a>

</div>

---

# 🌟 Flagship Work

A few projects that best represent what I've been building and learning recently.

<table>
<tr>
<td width="50%" valign="top">

## 🧠 RAG Document Assistant

**Local-first document intelligence**

A document assistant bringing together multi-format ingestion, selective OCR, speech-to-text, retrieval, local generation, citations, conversation memory, authentication, evaluation, and Dockerized services.

**AI layer**  
`Ollama` · `llama3.2` · `nomic-embed-text` · `RAG`

**Retrieval**  
`PostgreSQL` · `pgvector` · `HNSW` · `cosine search`

**Document & speech**  
`PyMuPDF` · `Tesseract OCR` · `faster-whisper` · `VAD`

**Application**  
`FastAPI` · `Gradio` · `SQLAlchemy` · `Alembic` · `Docker`

[**Explore RAG Document Assistant →**](https://github.com/fizzahussain/Rag-Document-Assistant)

</td>
<td width="50%" valign="top">

## 🔬 Revival Lab

**Research-oriented RAG**

A project that retrieves forgotten solutions from a curated knowledge archive and explores how historical ideas could be adapted to modern constraints.

**What I explored**  
`ChromaDB` · `LangChain` · `OpenAI` · `Gradio` · semantic retrieval · curated evidence · local fallback retrieval

It got me thinking about retrieval as a way to navigate evidence, rather than simply asking questions over documents.

[**Explore Revival Lab →**](https://github.com/fizzahussain/Revival-Lab)

</td>
</tr>

<tr>
<td width="50%" valign="top">

## 🍽️ MoodMeal

**Full-stack meal planning**

A meal planning application with pantry tracking, recipe recommendations, food-expense analytics, expiry awareness, saved recipes, and a Gemini-powered cooking assistant.

`React` · `Node.js` · `Express` · `MySQL` · `Gemini API`

[**Explore MoodMeal →**](https://github.com/fizzahussain/MoodMeal)

</td>
<td width="50%" valign="top">

## 🎬 MoviesData Manager

**Algorithms + recommendation**

A C++ movie data system built around AVL trees, hash tables, graph relationships, BFS, filtering, and custom recommendation logic.

`C++` · `AVL Trees` · `Hash Tables` · `Graphs` · `BFS`

[**Explore MoviesData Manager →**](https://github.com/fizzahussain/MoviesData-MANAGER)

</td>
</tr>
</table>

---

# 🧩 AI Systems Blueprint

The graph below shows the parts of an AI application I've worked with and wanted to understand beyond just calling a model API.

```mermaid
flowchart LR
    A["📄 Documents"] --> B["Parse / Normalize"]
    B --> C["Chunking"]
    C --> D["Embeddings"]
    D --> E[("Vector Store")]
    E --> F["Retrieval"]
    F --> G["Grounded Context"]
    G --> H["LLM"]
    H --> I["Answer + Citations"]

    S["🎙️ Speech"] --> STT["faster-whisper / VAD"]
    STT --> G

    O["🖼️ Scanned Pages"] --> OCR["Tesseract OCR"]
    OCR --> B

    E --> E1["pgvector / ChromaDB / Pinecone"]
    D --> D1["nomic-embed-text"]
    H --> H1["Ollama / OpenAI / Gemini"]
    I --> I1["FastAPI / Gradio / Streamlit"]
```

<details>
<summary><b>🔍 What I care about inside the system</b></summary>
<br>

- **Ingestion:** different formats, parsing, metadata, malformed content
- **OCR:** having a fallback when normal text extraction fails
- **Speech:** faster-whisper and VAD as another way to interact with the system
- **Chunking:** deciding what context should actually be retrieved
- **Embeddings:** how documents and queries are represented
- **Retrieval:** top-k search, cosine similarity, HNSW, relevance
- **Grounding:** giving the model useful retrieved context instead of just prompting it
- **Citations:** making the source of an answer inspectable
- **Evaluation:** checking retrieval and outputs rather than judging only by how fluent they sound
- **Application:** APIs, authentication, migrations, interfaces, Docker, and the software around the model

</details>

---

# 🧰 My Toolbox

**AI / Data**  
`Python` · `RAG` · `Ollama` · `llama3.2` · `nomic-embed-text` · `OpenAI` · `Gemini` · `LangChain` · `ChromaDB` · `Pinecone` · `pgvector` · `HNSW` · `Tesseract OCR` · `PyMuPDF` · `faster-whisper` · `VAD` · `NumPy` · `Pandas` · `Matplotlib` · `Power BI`

**Languages**  
`Python` · `C++` · `C` · `JavaScript` · `HTML` · `CSS` · `SQL` · `x86 Assembly` · `Bash`

**Web / APIs**  
`React` · `Node.js` · `Express` · `FastAPI` · `Bootstrap` · `Gradio` · `Streamlit` · `EJS` · `REST APIs` · `JWT`

**Databases / Persistence**  
`PostgreSQL` · `MySQL` · `SQLite` · `SQLAlchemy` · `Alembic` · `Views` · `Triggers` · `Stored Procedures` · `Vector Search`

**Systems / Graphics**  
`POSIX IPC` · `pthreads` · `Queues` · `Semaphores` · `Shared Memory` · `OpenGL` · `SDL2` · `MASM / Irvine32`

**Tools**  
`Docker` · `Docker Compose` · `Git` · `GitHub Actions` · `Linux` · `VS Code` · `pytest` · `Figma` · `Canva`

---

# 🧪 Explore the Portfolio by Signal

<details>
<summary><b>🤖 I want to see AI / Data work</b></summary>
<br>

1. [**RAG Document Assistant**](https://github.com/fizzahussain/Rag-Document-Assistant) — RAG, Ollama, OCR, STT, pgvector, HNSW, Docker
2. [**Revival Lab**](https://github.com/fizzahussain/Revival-Lab) — research-oriented RAG, ChromaDB, LangChain
3. [**UNO: 3 Player AI vs Human**](https://github.com/fizzahussain/UNO-3Player-AIvsHuman) — Minimax vs Expectimax
4. [**MoviesData Manager**](https://github.com/fizzahussain/MoviesData-MANAGER) — recommendation, graphs, BFS
5. [**MoodMeal**](https://github.com/fizzahussain/MoodMeal) — Gemini-powered meal planning
6. [**Personal Finance Management System**](https://github.com/fizzahussain/Personal-Finance-Management-System) — transaction analytics and data management

</details>

<details>
<summary><b>🌐 I want to see full-stack / database work</b></summary>
<br>

1. [**MoodMeal**](https://github.com/fizzahussain/MoodMeal) — React, Node, Express, MySQL, Gemini
2. [**RideFlow**](https://github.com/fizzahussain/RideFlow) — Express, EJS, MySQL, views, procedures, triggers
3. [**Personal Finance Management System**](https://github.com/fizzahussain/Personal-Finance-Management-System) — FastAPI, Streamlit, SQLite
4. [**CamCorder Website**](https://github.com/fizzahussain/CamCorder_website) — multi-page e-commerce UI

</details>

<details>
<summary><b>🧠 I want to see algorithms / DSA</b></summary>
<br>

1. [**MoviesData Manager**](https://github.com/fizzahussain/MoviesData-MANAGER) — AVL trees, hash tables, graphs, BFS
2. [**UNO: 3 Player AI vs Human**](https://github.com/fizzahussain/UNO-3Player-AIvsHuman) — game-tree search
3. [**Rush Hour**](https://github.com/fizzahussain/RushHour-game) — DFS reachability, OOP state
4. [**Word Shooter**](https://github.com/fizzahussain/Wordshooter-game) — binary-search dictionary lookup

</details>

<details>
<summary><b>⚙️ I want to see systems / low-level work</b></summary>
<br>

1. [**Parallel CSV Data Processing Pipeline**](https://github.com/fizzahussain/Parallel-CSV-Data-Processing-Pipeline) — processes, pthreads, queues, semaphores, shared memory
2. [**Rush Hour Assembly**](https://github.com/fizzahussain/RUSHHOUR_Assembly) — x86 Assembly, MASM/Irvine32, memory and file I/O
3. [**Rush Hour**](https://github.com/fizzahussain/RushHour-game) — C++, OpenGL, SDL2, game state
4. [**Word Shooter**](https://github.com/fizzahussain/Wordshooter-game) — C++, SDL2, OOP, game loop

</details>

<details>
<summary><b>📊 I want to see data / analytics work</b></summary>
<br>

1. [**Personal Finance Management System**](https://github.com/fizzahussain/Personal-Finance-Management-System) — transaction analytics, budgets, dashboards
2. [**RideFlow**](https://github.com/fizzahussain/RideFlow) — SQL analytics, views, procedures, reporting
3. [**MoviesData Manager**](https://github.com/fizzahussain/MoviesData-MANAGER) — structured data, filtering, recommendations

</details>

<br>

[**Explore all repositories →**](https://github.com/fizzahussain?tab=repositories) · [**Explore the portfolio →**](https://fizza-hussain.vercel.app/)

Some projects are **university coursework, some are personal projects, and some are things I've continued improving after coursework**. I like keeping that progression visible.

---

# 📊 GitHub Pulse

<div align="center">

### Live GitHub activity

<a href="https://github.com/fizzahussain">
  <img src="assets/github-pulse.svg" width="100%" alt="Fizza Hussain GitHub activity" />
</a>

<br><br>

### Contribution Activity

<img src="https://github-readme-activity-graph.vercel.app/graph?username=fizzahussain&bg_color=0d1117&color=c4b5fd&line=8b5cf6&point=f8fafc&area=true&hide_border=true&custom_title=Fizza%20Hussain's%20Contribution%20Graph" width="100%" alt="Fizza Hussain GitHub contribution activity graph"/>

<br><br>

### Contributions but make it my fav childhood game

<img src="assets/github-contribution-grid-snake-dark.svg" width="100%" alt="Fizza Hussain contribution snake animation"/>

</div>

---

# 🎯 What I'm Exploring Next

I'm currently going deeper into **machine learning, NLP, retrieval, recommendation systems, data engineering, and backend development**.

I'm also curious about areas outside the usual Data Science path. If something catches my attention, I like learning about it by building something and seeing where it leads.

---

# 🤝 Let's Connect

<div align="center">

I'm always interested in learning, building, collaborating, and exploring ideas across different areas of technology.

<a href="https://www.linkedin.com/in/fizza-hussain-97a171279"><img src="https://img.shields.io/badge/LinkedIn-Connect_with_me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:fizzashah0300@gmail.com"><img src="https://img.shields.io/badge/Email-fizzashah0300%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>

<br><br>

**Still learning · still experimenting · still building**

</div>
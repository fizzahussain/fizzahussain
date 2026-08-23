<div align="center">

# 👋 Hi, I'm Fizza Hussain

### Data Science · AI/ML · Software Development

<img src="https://img.shields.io/badge/AI_%26_DATA-7C3AED?style=for-the-badge" alt="AI and Data"/>
<img src="https://img.shields.io/badge/SOFTWARE-2563EB?style=for-the-badge" alt="Software"/>
<img src="https://img.shields.io/badge/ALGORITHMS_%26_SYSTEMS-0F766E?style=for-the-badge" alt="Algorithms and Systems"/>

<br><br>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2600&pause=750&color=A78BFA&center=true&vCenter=true&width=950&lines=Building+AI+and+data+projects;Learning+to+build+with+AI+as+a+tool;Exploring+retrieval%2C+recommendation%2C+and+game+AI;From+data+and+algorithms+to+working+applications" alt="Animated introduction" />
</a>

<br>

I'm a **third-year BS Data Science student at FAST-NUCES Islamabad**. I enjoy figuring out how things work and then trying to build them myself, from algorithms and data projects to web applications and AI-powered tools.

I'm especially interested in **AI/ML, Data Science, NLP, RAG, recommendation systems, and intelligent applications**, while continuing to build my software engineering and systems fundamentals.

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

My strongest AI systems project. It brings together multi-format document ingestion, selective OCR, speech-to-text, retrieval, local generation, citations, conversation memory, authentication, evaluation, and Dockerized services.

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

**Forensic RAG research**

A research-oriented RAG project that retrieves forgotten solutions from a curated knowledge archive and explores how historical ideas could be adapted to modern constraints.

**What I explored**  
`ChromaDB` · `LangChain` · `OpenAI` · `Gradio` · semantic retrieval · curated evidence · local fallback retrieval

It pushed me beyond simply asking questions over documents and into thinking about retrieval as a way to navigate evidence.

[**Explore Revival Lab →**](https://github.com/fizzahussain/Revival-Lab)

</td>
</tr>

<tr>
<td width="50%" valign="top">

## 🍽️ MoodMeal

**AI inside a real product**

A full-stack meal planning application with pantry tracking, recipe recommendations, food-expense analytics, expiry awareness, saved recipes, and a Gemini-powered cooking assistant.

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

The graph below shows the parts of an AI application I've actually worked with and wanted to understand beyond just calling a model API.

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

    E --> E1["pgvector / ChromaDB"]
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
- **Application:** APIs, authentication, migrations, interfaces, Docker, and the rest of the software around the model

</details>

---

# 🧰 My Toolbox

## 🤖 AI / Data

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/RAG-7C3AED?style=for-the-badge" />
<img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" />
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge" />
<img src="https://img.shields.io/badge/pgvector-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Tesseract_OCR-5B9BD5?style=for-the-badge" />
<img src="https://img.shields.io/badge/faster--whisper-111827?style=for-the-badge" />
</p>

## 💻 Development

<p align="center">
<img src="https://skillicons.dev/icons?i=python,cpp,c,js,html,css,react,nodejs,express,fastapi,bootstrap&perline=11" alt="Development technologies"/>
</p>

## 🗄️ Databases & Tools

<p align="center">
<img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite,docker,git,github,githubactions,linux,vscode&perline=9" alt="Databases and tools"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/Gradio-F97316?style=for-the-badge" />
<img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
<img src="https://img.shields.io/badge/Alembic-6BA81E?style=for-the-badge" />
<img src="https://img.shields.io/badge/OpenGL-5586A4?style=for-the-badge&logo=opengl&logoColor=white" />
<img src="https://img.shields.io/badge/x86_Assembly-6E4C13?style=for-the-badge" />
</p>

---

# 🔎 Explore More

<details>
<summary><b>Systems & Data</b></summary>
<br>

**Systems & concurrency**  
Processes, `fork()` / `execvp()`, pthreads, FIFO communication, producer-consumer queues, semaphores, shared memory, signals, and parallel data processing.

[**Parallel CSV Data Processing Pipeline →**](https://github.com/fizzahussain/Parallel-CSV-Data-Processing-Pipeline)

**Databases & backend**  
RideFlow, SQL views, procedures, triggers, indexes, APIs, SQLite, MySQL, and PostgreSQL.

[**RideFlow →**](https://github.com/fizzahussain/RideFlow) · [**Personal Finance Management System →**](https://github.com/fizzahussain/Personal-Finance-Management-System)

</details>

<details>
<summary><b>Graphics & Low-Level</b></summary>
<br>

**Games & graphics**  
C++ projects using OpenGL, SDL2, OOP, game loops, graph traversal, collision handling, and state management.

[**Rush Hour →**](https://github.com/fizzahussain/RushHour-game) · [**Word Shooter →**](https://github.com/fizzahussain/Wordshooter-game)

**Low-level work**  
An x86 Assembly version of Rush Hour using MASM/Irvine32, including registers, procedures, memory operations, file I/O, and system APIs.

[**Rush Hour Assembly →**](https://github.com/fizzahussain/RUSHHOUR_Assembly)

</details>

<details>
<summary><b>Data & Analytics</b></summary>
<br>

Exploratory analysis, visualization, financial reporting, dashboards, SQL, clickstream aggregation, and data-processing workflows across different projects.

</details>

[**Explore all repositories →**](https://github.com/fizzahussain?tab=repositories) · [**Explore the portfolio →**](https://fizza-hussain.vercel.app/)

Some projects are **university coursework, some are personal projects, and some are things I've continued improving after coursework**. I like keeping that progression visible.

---

# 📈 GitHub Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=fizzahussain&bg_color=0d1117&color=c4b5fd&line=8b5cf6&point=f8fafc&area=true&hide_border=true&custom_title=Fizza%20Hussain's%20Contribution%20Graph" width="100%" alt="Fizza Hussain GitHub contribution activity graph"/>

<br><br>

<img src="assets/github-contribution-grid-snake-dark.svg" width="100%" alt="GitHub contribution activity"/>

</div>

---

# 🎯 What I'm Exploring Next

I'm currently going deeper into **Machine Learning, NLP, retrieval, recommendation systems, data engineering, and backend development**.

I'm also interested in exploring areas outside the usual Data Science path when something catches my attention. I like learning by building and seeing where that takes me.

---

# 🤝 Let's Connect

<div align="center">

I'm always interested in learning, building, collaborating, and exploring ideas across different areas of technology.

<a href="https://www.linkedin.com/in/fizza-hussain-97a171279"><img src="https://img.shields.io/badge/LinkedIn-Connect_with_me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:fizzashah0300@gmail.com"><img src="https://img.shields.io/badge/Email-fizzashah0300%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>

<br><br>

**Still learning · still experimenting · still building**

</div>
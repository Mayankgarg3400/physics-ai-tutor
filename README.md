# 📚 Physics AI Tutor (RAG)

An AI-powered **Physics Question Answering System** built using **Retrieval-Augmented Generation (RAG)**.

This project allows users to ask questions from a Physics textbook and receive accurate answers using **semantic search**, **vector embeddings**, and a **local Qwen LLM** running via **Ollama**.

---

## 🚀 Features

- 📖 Ask questions from a Physics textbook
- 🤖 Local Qwen model (Ollama)
- 🔍 Semantic Search using ChromaDB
- 🧠 HuggingFace Embeddings
- 📄 PDF-based Retrieval-Augmented Generation (RAG)
- 💬 Streamlit Chat Interface
- 📚 Displays source pages used to generate answers
- ⚡ Fast local inference without external APIs

---

## 🏗️ Project Architecture

```
                    User
                      │
                      ▼
              Streamlit Interface
                      │
                      ▼
                 RAG Pipeline
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
   Chroma Retriever          Qwen (Ollama)
         │                         │
         └────────────┬────────────┘
                      ▼
              Final AI Response
```

---

## 🛠️ Tech Stack

- Python
- LangChain
- Streamlit
- Ollama
- Qwen 2.5
- HuggingFace Embeddings
- ChromaDB
- PyPDF

---

## 📂 Project Structure

```
physics-ai-tutor/
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── rag_chain.py
│
├── app.py
├── graph.py
├── ingest.py
├── prompts.py
├── config.py
├── main.py
│
├── data/
│   └── Physics-Book.pdf
│
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mayankgarg3400/physics-ai-tutor.git

cd physics-ai-tutor
```

---

### 2. Create Virtual Environment

```bash
uv venv
```

Activate it

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
uv sync
```

---

### 4. Install Ollama

Download Ollama

https://ollama.com

---

### 5. Pull Qwen Model

```bash
ollama pull qwen2.5:3b
```

---

### 6. Start Ollama

```bash
ollama serve
```

---

### 7. Create Vector Database

```bash
uv run ingest.py
```

---

### 8. Run the Application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What is Newton's Second Law?
- Explain Momentum.
- Define Friction.
- What is Potential Energy?
- Explain the Law of Gravitation.

---

## 📸 Demo

_Add screenshots or GIFs here._

Example:

```
assets/demo.png
```

---

## 📈 Future Improvements

- ✅ Dynamic PDF Upload
- ✅ Streaming Responses
- ✅ Better Source Preview
- ✅ Conversation Memory
- ✅ LangGraph Integration
- ✅ Multi-Agent Workflow
- ✅ Quiz Generator
- ✅ Formula Extraction
- ✅ Chapter Summarization
- ✅ Deploy on Streamlit Cloud

---
## 📸 Demo

![Physics AI Tutor](assets/demo.jpeg)

## 👨‍💻 Author

**Mayank Garg**

GitHub

https://github.com/Mayankgarg3400

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!



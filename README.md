# 📚 AI Knowledge Assistant (RAG Document Q&A Bot)

A Retrieval-Augmented Generation (RAG) based Document Question Answering system that allows users to ask natural language questions against a collection of documents and receive grounded answers with source citations.

The system ingests documents, splits them into chunks, generates embeddings, stores them in a vector database, retrieves relevant context, and uses a Large Language Model (LLM) to generate accurate responses.

---

# 🚀 Features

- Document ingestion from TXT and PDF files
- Recursive text chunking with overlap
- Batch embedding generation
- ChromaDB vector database with persistence
- Semantic similarity search
- Groq Llama 3.3 powered answer generation
- Source citations included in answers
- Handles unanswerable questions gracefully
- Command Line Interface (CLI)
- Streamlit Web Interface

---

# 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.11 |
| UI | Streamlit |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| LLM | Llama 3.3 70B (Groq) |
| Chunking | LangChain RecursiveCharacterTextSplitter |
| PDF Parsing | PyPDF |
| Environment Variables | python-dotenv |

---

# 🏗 Architecture Overview

```text
Documents
    ↓
Document Loader
    ↓
Text Chunking
    ↓
Embeddings
    ↓
ChromaDB Vector Store
    ↓
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Chunks
    ↓
Groq LLM
    ↓
Answer + Citations
```

---

# 📂 Project Structure

```text
document-qa-bot/
│
├── data/
│   ├── artificial_intelligence.txt
│   ├── machine_learning.txt
│   ├── cloud_computing.txt
│   ├── cybersecurity.txt
│   └── data_science.pdf
│
├── src/
│   ├── app.py
│   ├── chunker.py
│   ├── config.py
│   ├── document_loader.py
│   ├── embedder.py
│   ├── generator.py
│   ├── ingest.py
│   ├── main.py
│   ├── query.py
│   └── vector_store.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📄 Documents Used

The knowledge base consists of the following documents:

1. Artificial Intelligence
2. Machine Learning
3. Cloud Computing
4. Cybersecurity
5. Data Science

At least one document is provided in PDF format as required.

---

# ✂️ Chunking Strategy

The project uses LangChain's RecursiveCharacterTextSplitter.

Configuration:

```python
chunk_size = 1000
chunk_overlap = 200
```

Why?

- Preserves semantic meaning
- Prevents context loss at chunk boundaries
- Improves retrieval quality

---

# 🧠 Embedding Model

Model:

```text
all-MiniLM-L6-v2
```

Reason for selection:

- Lightweight and efficient
- Strong semantic search performance
- Open-source and free
- Fast embedding generation

All embeddings are generated in batches to improve performance.

---

# 🗄 Vector Database

Database:

```text
ChromaDB
```

Reason for selection:

- Easy local setup
- Persistent storage
- Fast similarity search
- Open-source

The database persists embeddings to disk and avoids re-indexing on every run.

---

# 🔍 Retrieval Process

1. User enters a question.
2. The question is converted into an embedding.
3. ChromaDB performs similarity search.
4. Top-K relevant chunks are retrieved.
5. Retrieved chunks are sent to the LLM as context.

Default:

```text
Top-K = 3
```

---

# 🤖 Answer Generation

LLM:

```text
Llama 3.3 70B (Groq)
```

The model receives only the retrieved context.

Prompt rules:

- Use only retrieved context.
- Do not use external knowledge.
- Return a fallback response if information is not available.

Fallback:

```text
I cannot find the answer in the provided documents.
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone <repository-url>
cd document-qa-bot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit API keys to GitHub.

---

# 📥 Index Documents

Run:

```bash
python src/ingest.py
```

Expected output:

```text
Loaded documents
Created chunks
Generated embeddings
Indexing completed successfully
```

---

# 💻 Run CLI Application

```bash
python src/main.py
```

---

# 🌐 Run Streamlit Application

```bash
streamlit run src/app.py
```

---

# 📝 Example Queries

```text
What is Artificial Intelligence?

What is supervised learning?

What are the benefits of cloud computing?

What are common cybersecurity threats?

How is Data Science used in healthcare?
```

Unanswerable query:

```text
Who won FIFA World Cup 2022?
```

Expected:

```text
I cannot find the answer in the provided documents.
```

---

# ⚠️ Known Limitations

- Performance depends on retrieval quality.
- Small document collection limits coverage.
- Uses local vector storage only.
- Page-level citations are basic.
- Does not support document uploads through the UI.

---

# 📹 Demo

The demonstration includes:

- Document ingestion
- Chunk generation
- Embedding creation
- ChromaDB indexing
- Question answering
- Source citations
- Handling unanswerable questions

---

# 👨‍💻 Author

Omprakash Karri

Built as part of an AI Engineering Internship Assignment.

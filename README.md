# 🧠 SmartFind - AI Memory Operating System

> **Your second brain that never forgets.**

SmartFind is an AI-powered semantic file search and personal knowledge operating system that helps users instantly find documents, presentations, notes, PDFs, and other files using natural language instead of remembering filenames or folder locations.

It combines **semantic search**, **vector databases**, and **Retrieval-Augmented Generation (RAG)** to transform how users interact with their personal knowledge.

---

# 🚀 Vision

Traditional file systems require users to remember:

- Folder names
- File names
- File locations

SmartFind changes this by allowing users to search using **memory**.

Example:

> "Find the DBMS notes my senior shared before second-year exams."

or

> "Show every document related to React Hooks."

Instead of searching filenames, SmartFind understands the **meaning** of the query and retrieves the most relevant documents.

---

# ✨ Features

## 📂 Smart File Search

- Semantic Search
- Natural Language Search
- Filename Search
- Metadata Search
- Time-based Search
- OCR Search *(Planned)*
- Duplicate Detection *(Planned)*
- Similar File Search *(Planned)*

---

## 🤖 AI Features

- Chat with Documents (RAG)
- PDF Summarization *(Planned)*
- Flashcard Generation *(Planned)*
- Quiz Generation *(Planned)*
- Mind Maps *(Planned)*
- Interview Questions *(Planned)*
- Cross-document Intelligence *(Planned)*
- Knowledge Graph *(Planned)*

---

## 🖥 Desktop Integration

- Local File System Indexing
- Folder Monitoring *(Planned)*
- Background Indexing *(Planned)*
- Multi-drive Search *(Planned)*
- External Drive Support *(Planned)*
- Cloud Storage Integration *(Planned)*

---

## 📈 AI Memory Timeline

Automatically tracks learning history.

Examples:

- Uploaded DBMS Notes
- Created Presentation
- Started Internship
- Downloaded React Book
- Learned Machine Learning

---

# 🏗 Architecture

```text
                     React + Electron
                           │
                           ▼
                    FastAPI Backend
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Authentication      File System         AI Engine
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                 Supabase PostgreSQL
             (Users, Metadata, Auth)
                           │
                           ▼
          Sentence Transformers Embeddings
             (all-MiniLM-L6-v2 - Local)
                           │
                           ▼
                Qdrant Cloud Vector DB
                           │
                           ▼
                  Semantic Search
                           │
                           ▼
                  Top Relevant Chunks
                           │
                           ▼
                    Groq LLM (RAG)
                           │
                           ▼
                  AI Generated Answer
```

---

# ⚙️ AI Processing Pipeline

```text
Document
    │
    ▼
Text Extraction
    │
    ▼
Text Cleaning
    │
    ▼
Smart Chunking
    │
    ▼
SentenceTransformer Embeddings
    │
    ▼
Qdrant Vector Database
    │
    ▼
Semantic Search
    │
    ▼
Top Relevant Chunks
    │
    ▼
Prompt Builder
    │
    ▼
Groq LLM
    │
    ▼
Final AI Response
```

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Tailwind CSS
- Electron *(Planned)*

---

## Backend

- FastAPI
- Python

---

## Database

- Supabase PostgreSQL
- Qdrant Cloud Vector Database

---

## AI

- Sentence Transformers
- all-MiniLM-L6-v2
- Retrieval-Augmented Generation (RAG)
- Groq LLM
- OCR *(Planned)*
- LangChain *(Future)*
- LlamaIndex *(Future)*

---

## Cloud & DevOps

- Supabase
- Qdrant Cloud
- Docker *(Future)*
- GitHub Actions *(Future)*

---

# 📂 Supported File Types

## Currently Supported

- ✅ PDF
- ✅ DOCX
- ✅ PPTX
- ✅ TXT

---

## Planned

- Images (PNG, JPG, JPEG)
- Audio (MP3, WAV)
- Video
- Excel
- CSV
- Markdown
- Source Code Files
- ZIP Archives

---

# 📅 Development Roadmap

## ✅ Phase 1 — Backend Foundation

- [x] Project Architecture
- [x] FastAPI Setup
- [x] Supabase Integration
- [x] JWT Authentication
- [x] User Profile APIs
- [x] Multi-user Support

---

## ✅ Phase 2 — File Management

- [x] Folder Registration
- [x] File Registration
- [x] File Metadata Storage
- [x] SHA-256 Hashing
- [x] Background File Processing
- [ ] Duplicate Detection
- [ ] Version Management

---

## ✅ Phase 3 — AI Processing

- [x] PDF Text Extraction
- [x] DOCX Extraction
- [x] PPTX Extraction
- [x] TXT Extraction
- [x] Text Cleaning
- [x] Smart Chunking
- [x] Local Embeddings
- [x] Sentence Transformers
- [x] Qdrant Cloud Integration
- [x] Semantic Search
- [x] Retrieval-Augmented Generation (RAG)
- [x] Groq LLM Integration
- [ ] OCR Pipeline
- [ ] Image Embeddings
- [ ] Audio Transcription

---

## 🚧 Phase 4 — Desktop AI

- [ ] Electron Desktop Application
- [ ] Folder Monitoring
- [ ] Queue-based Background Processing
- [ ] Background Indexing
- [ ] Multi-drive Search
- [ ] External Drive Support

---

## 🚧 Phase 5 — Advanced AI

- [ ] AI Memory Timeline
- [ ] Knowledge Graph
- [ ] Cross-document Intelligence
- [ ] Flashcard Generation
- [ ] Quiz Generation
- [ ] Mind Map Generation
- [ ] Voice Search
- [ ] AI Study Mode

---

# 📁 Project Structure

```
backend/
│
├── app/
│   ├── ai/
│   │   ├── embeddings/
│   │   ├── extractors/
│   │   ├── llm/
│   │   ├── pipeline/
│   │   ├── preprocessing/
│   │   ├── rag/
│   │   ├── search/
│   │   └── vector_store/
│   │
│   ├── api/
│   ├── core/
│   ├── middleware/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── workers/
│
└── main.py
```

---

# 🚀 Current Project Status

## ✅ Completed

- Authentication System
- User Profiles
- Multi-user Architecture
- File Registration APIs
- Metadata Storage
- SHA-256 File Hashing
- Document Processing Pipeline
- PDF / DOCX / PPTX / TXT Extraction
- Smart Chunking
- Local Embedding Generation
- Qdrant Cloud Integration
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Groq AI Integration
- Document Chat API

---

## 🚧 In Progress

- Queue-based Background Indexing
- Electron Desktop Client
- OCR Support
- Image Indexing
- Audio Processing
- Knowledge Graph
- AI Memory Timeline

---

# 🌟 Future Scope

SmartFind aims to evolve into a complete **AI Memory Operating System** capable of understanding, organizing, and retrieving knowledge across:

- Local Storage
- Cloud Drives
- Documents
- Images
- Audio Files
- Videos
- Emails
- Notes
- Code Repositories
- Research Papers

Future versions will introduce autonomous AI agents that proactively organize knowledge, recommend learning resources, generate study materials, and build a personalized knowledge graph for every user.

---

# 👩‍💻 Author

**Likhitha Cherukuru**

Final Year B.Tech – Information Technology

Andhra University College of Engineering

---

## ⭐ If you found this project interesting, consider giving it a star!
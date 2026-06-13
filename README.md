# 📚 Agentic Multi-PDF RAG Assistant

An AI-powered Career & Learning Assistant built using LangChain, Ollama, Pinecone, HuggingFace Embeddings, and Streamlit.

The application enables users to upload multiple PDF documents, interact with them using Retrieval-Augmented Generation (RAG), analyze resumes, match resumes with job descriptions, identify skill gaps, generate quizzes and flashcards, create interview questions, build personalized learning roadmaps, and intelligently route queries to specialized AI agents.

---

## 🚀 Features

### 📄 Multi-PDF Processing

* Upload multiple PDF documents
* Process and index documents for semantic search
* Store embeddings in Pinecone Vector Database

### 💬 Chat With PDFs

* Ask questions from uploaded documents
* Context-aware answers using RAG
* Conversation memory support
* Source document references

### 📊 Resume Analyzer

* Analyze resume strengths and weaknesses
* Identify missing sections
* Improve resume quality

### 🎯 Job Description Matcher

* Compare resume with job descriptions
* Evaluate compatibility
* Highlight matching and missing skills

### 📈 Skill Gap Analyzer

* Detect missing technical and soft skills
* Recommend improvement areas
* Generate learning suggestions

### 🧠 Quiz Generator

* Generate quizzes from uploaded documents
* Improve learning and revision

### 🃏 Flashcard Generator

* Create study flashcards automatically
* Quick concept revision

### 🎤 AI Interview Generator

* Generate interview questions based on resume content
* Technical and behavioral question support

### 🗺️ AI Roadmap Generator

* Generate personalized career roadmaps
* Learning path recommendations

### 🤖 Agent Router

* Automatically selects the best AI agent
* Routes user queries intelligently

### 📥 Chat Export

* Export conversations as PDF reports

---

## 🏗️ System Architecture

User → Streamlit UI → Agent Router → LangChain → Pinecone Vector Database → Ollama (Phi-3)

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / LLM

* Ollama
* Phi-3
* LangChain

### Vector Database

* Pinecone

### Embeddings

* HuggingFace Embeddings
* all-MiniLM-L6-v2

### Additional Libraries

* ReportLab
* PyPDF
* Python-dotenv

---

## 📸 Project Screenshots

### 💬 Chat With PDFs

![Chat With PDFs](screenshots/chat_with_pdf.png)

### 📄 Resume Analyzer

![Resume Analyzer](screenshots/resume_analyzer.png)

### 🎯 Job Matcher

![Job Matcher](screenshots/job_matcher.png)

### 📊 Skill Gap Analyzer

![Skill Gap Analyzer](screenshots/skill_gap.png)

### 🎤 AI Interview Generator

![Interview Generator](screenshots/interview_generator.png)

### 🗺️ Roadmap Generator

![Roadmap Generator](screenshots/roadmap_generator.png)

---

## 📂 Project Structure

```text
Agentic-Rag-Assistant/
│
├── app.py
├── ingest.py
├── requirements.txt
├── .gitignore
│
├── modules/
│   ├── chatbot.py
│   ├── retriever.py
│   ├── resume_analyzer.py
│   ├── job_matcher.py
│   ├── skill_gap.py
│   ├── quiz_generator.py
│   ├── flashcard_generator.py
│   ├── interview_generator.py
│   ├── roadmap_generator.py
│   ├── router.py
│   ├── memory.py
│   └── chat_export.py
│
└── screenshots/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/agentic-multi-pdf-rag-assistant.git
```

### Move Into Project

```bash
cd agentic-multi-pdf-rag-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Future Enhancements

* Voice-Based PDF Chat
* Multi-Agent Collaboration
* Interview Evaluation System
* Resume ATS Score Calculator
* Job Recommendation Engine
* Learning Progress Tracking

---

## 👩‍💻 Author

### Sowmya Srilakshmi

AI/ML Engineer | GenAI Enthusiast

Passionate about Artificial Intelligence, Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), Agentic AI Systems, and Machine Learning Applications.

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

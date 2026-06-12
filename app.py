import os
import streamlit as st

from ingest import ingest_documents
from modules.retriever import retrieve_documents
from modules.chatbot import generate_answer
from modules.resume_analyzer import analyze_resume
from modules.job_matcher import match_resume_job
from modules.quiz_generator import generate_quiz
from modules.flashcard_generator import generate_flashcards
from modules.interview_generator import generate_interview_questions
from modules.skill_gap import analyze_skill_gap
from modules.roadmap_generator import generate_roadmap
from modules.router import route_query
from modules.chat_export import create_chat_report

from modules.memory import (
    initialize_memory,
    add_to_memory,
    get_chat_history
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(
    page_title="Agentic Multi-PDF RAG Assistant",
    page_icon="📚",
    layout="wide"
)

initialize_memory()
st.sidebar.title(
    "🤖 Agentic Multi-PDF RAG Assistant"
)

st.sidebar.markdown(
    """
### 👩‍💻 Developer

**Sowmya Srilakshmi**

🎓 AI & Machine Learning Student

🚀 Building GenAI Applications

💡 Passionate about RAG, LLMs, and Agentic AI
"""
)

st.sidebar.markdown("---")

st.title("📚 Agentic Multi-PDF RAG Assistant")
st.caption(
    "An AI-powered Career & Learning Assistant using RAG, Ollama, Pinecone, and LangChain"
)
col1, col2, col3 = st.columns(3)

col1.metric(
    "Features",
    "10+"
)

col2.metric(
    "LLM",
    "Phi-3"
)

col3.metric(
    "Framework",
    "LangChain"
)

# =====================================
# SIDEBAR
# =====================================

page = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Chat With PDFs",
        "Resume Analyzer",
        "Job Matcher",
        "Skill Gap Analyzer",
        "Quiz Generator",
        "Flashcard Generator",
        "Interview Generator",
        "Roadmap Generator",
        "Agent Router"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
📚 Agentic Multi-PDF RAG Assistant

✅ PDF Chat
✅ Resume Analyzer
✅ Job Matcher
✅ Skill Gap Analyzer
✅ Quiz Generator
✅ Flashcards
✅ Interview Generator
✅ Roadmap Generator
✅ Agent Router
"""
)

# =====================================
# PDF UPLOAD
# =====================================

st.sidebar.markdown("---")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        path = os.path.join(
            UPLOAD_DIR,
            file.name
        )

        with open(path, "wb") as f:
            f.write(file.getbuffer())

    st.sidebar.success(
        "PDFs Uploaded"
    )

if st.sidebar.button(
    "Process PDFs"
):

    count = ingest_documents()

    st.sidebar.success(
        f"{count} chunks processed"
    )

# =====================================
# CHAT WITH PDF
# =====================================

if page == "Chat With PDFs":

    st.header("💬 Chat With PDFs")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        docs = retrieve_documents(
            question
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        history = ""

        for item in get_chat_history():

            history += f"""
User: {item['question']}
Assistant: {item['answer']}
"""

        answer = generate_answer(
            question,
            context,
            history
        )

        st.write(answer)

        add_to_memory(
            question,
            answer
        )

    st.subheader(
        "📝 Chat History"
    )

    for item in get_chat_history():

        st.write(
            f"🙋 {item['question']}"
        )

        st.write(
            f"🤖 {item['answer']}"
        )

    if st.button(
        "Export Chat Report"
    ):

        pdf_file = create_chat_report(
            get_chat_history()
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                "Download PDF",
                file,
                file_name=pdf_file
            )

# =====================================
# RESUME ANALYZER
# =====================================

elif page == "Resume Analyzer":

    st.header(
        "📄 Resume Analyzer"
    )

    if st.button(
        "Analyze Resume"
    ):

        docs = retrieve_documents(
            "resume skills projects education experience"
        )

        resume_text = "\n".join(
            [doc.page_content for doc in docs]
        )

        result = analyze_resume(
            resume_text
        )

        st.write(result)

# =====================================
# JOB MATCHER
# =====================================

elif page == "Job Matcher":

    st.header(
        "🎯 Job Matcher"
    )

    jd = st.text_area(
        "Paste Job Description"
    )

    if st.button(
        "Match Resume"
    ):

        docs = retrieve_documents(
            "resume skills projects education experience"
        )

        resume_text = "\n".join(
            [doc.page_content for doc in docs]
        )

        result = match_resume_job(
            resume_text,
            jd
        )

        st.write(result)

# =====================================
# SKILL GAP
# =====================================

elif page == "Skill Gap Analyzer":

    st.header(
        "📊 Skill Gap Analyzer"
    )

    jd = st.text_area(
        "Paste Job Description"
    )

    if st.button(
        "Analyze Skill Gap"
    ):

        docs = retrieve_documents(
            "resume skills projects education experience"
        )

        resume_text = "\n".join(
            [doc.page_content for doc in docs]
        )

        result = analyze_skill_gap(
            resume_text,
            jd
        )

        st.write(result)

# =====================================
# QUIZ
# =====================================

elif page == "Quiz Generator":

    st.header(
        "🧠 Quiz Generator"
    )

    if st.button(
        "Generate Quiz"
    ):

        docs = retrieve_documents(
            "important concepts"
        )

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        quiz = generate_quiz(
            context
        )

        st.write(quiz)

# =====================================
# FLASHCARDS
# =====================================

elif page == "Flashcard Generator":

    st.header(
        "🃏 Flashcard Generator"
    )

    if st.button(
        "Generate Flashcards"
    ):

        docs = retrieve_documents(
            "important concepts"
        )

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        flashcards = generate_flashcards(
            context
        )

        st.write(flashcards)

# =====================================
# INTERVIEW
# =====================================

elif page == "Interview Generator":

    st.header(
        "🎤 Interview Generator"
    )

    if st.button(
        "Generate Interview Questions"
    ):

        docs = retrieve_documents(
            "resume skills projects experience"
        )

        resume_text = "\n".join(
            [doc.page_content for doc in docs]
        )

        questions = (
            generate_interview_questions(
                resume_text
            )
        )

        st.write(questions)

# =====================================
# ROADMAP
# =====================================

elif page == "Roadmap Generator":

    st.header(
        "🗺️ Roadmap Generator"
    )

    goal = st.text_input(
        "Career Goal"
    )

    if st.button(
        "Generate Roadmap"
    ):

        result = generate_roadmap(
            goal
        )

        st.write(result)

# =====================================
# AGENT ROUTER
# =====================================

elif page == "Agent Router":

    st.header(
        "🤖 Agent Router"
    )

    query = st.text_input(
        "Ask Anything"
    )

    if query:

        agent = route_query(
            query
        )

        st.success(
            f"Selected Agent: {agent}"
        )

        st.write(
            "Agent routing active."
        )
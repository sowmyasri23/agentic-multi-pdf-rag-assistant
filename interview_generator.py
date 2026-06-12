from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def generate_interview_questions(resume_text):

    prompt = f"""
You are an expert technical interviewer.

Based on the resume below, generate:

1. 10 Technical Questions
2. 5 Project-Based Questions
3. 5 HR Questions

Resume:
{resume_text}

Format clearly with headings.
"""

    response = llm.invoke(prompt)

    return response.content
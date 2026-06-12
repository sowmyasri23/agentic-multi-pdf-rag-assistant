from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze this resume and provide:

1. ATS Score (out of 100)
2. Professional Summary
3. Technical Skills Found
4. Strengths
5. Weaknesses
6. Missing Skills
7. Resume Improvement Suggestions
8. AI/ML Engineer Readiness

Resume:

{resume_text}
"""

    response = llm.invoke(prompt)

    return response.content
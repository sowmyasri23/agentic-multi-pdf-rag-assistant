from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def match_resume_job(resume_text, job_description):

    prompt = f"""
You are an expert ATS and Recruitment Specialist.

Compare the resume with the job description.

Provide:

1. Match Score (0-100)
2. Matching Skills
3. Missing Skills
4. Strengths
5. Weaknesses
6. Improvement Suggestions

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = llm.invoke(prompt)

    return response.content
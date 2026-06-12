from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def analyze_skill_gap(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert career advisor.

Compare the resume and job description.

Provide:

1. Match Percentage
2. Skills Present
3. Missing Skills
4. Learning Recommendations
5. Improvement Suggestions

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = llm.invoke(prompt)

    return response.content
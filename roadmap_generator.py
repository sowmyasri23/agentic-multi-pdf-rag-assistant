from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def generate_roadmap(goal):

    prompt = f"""
You are an expert career mentor.

Create a detailed learning roadmap for:

{goal}

Include:

1. Beginner Stage
2. Intermediate Stage
3. Advanced Stage
4. Recommended Projects
5. Useful Tools & Technologies

Format clearly with headings and timelines.
"""

    response = llm.invoke(prompt)

    return response.content
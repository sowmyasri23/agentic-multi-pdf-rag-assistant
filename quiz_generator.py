from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def generate_quiz(context):

    prompt = f"""
You are an expert educator.

Generate 5 multiple-choice questions from the provided content.

For each question provide:

Question
A)
B)
C)
D)

Correct Answer

Content:
{context}
"""

    response = llm.invoke(prompt)

    return response.content

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def generate_answer(question, context, history=""):

    prompt = f"""
You are an intelligent AI assistant.

Previous Conversation:
{history}

Context:
{context}

Question:
{question}

Instructions:
- Use the provided context.
- Use conversation history when relevant.
- If answer is not found, say so clearly.
- Be concise and accurate.

Answer:
"""

    response = llm.invoke(prompt)

    return response.content
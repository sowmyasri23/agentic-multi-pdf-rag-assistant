from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

def generate_flashcards(context):

    prompt = f"""
You are an expert teacher.

Create 10 flashcards from the content.

Format:

Term:
Definition:

Term:
Definition:

Content:
{context}
"""

    response = llm.invoke(prompt)

    return response.content
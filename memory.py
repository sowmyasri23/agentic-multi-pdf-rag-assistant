import streamlit as st

def initialize_memory():

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_to_memory(question, answer):

    st.session_state.chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )

def get_chat_history():

    return st.session_state.chat_history
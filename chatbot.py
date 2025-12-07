from dotenv import load_dotenv
import streamlit as st

from langchain_groq import ChatGroq

#load env variables

print("**************************")
load_dotenv(".env")

#streamlit page setup

st.set_page_config(
    page_title="ChatBot",
    page_icon= "🤖",
    layout = "centered"
)

st.title("💬 Srini AI Bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})

    response=llm.invoke(
        input=[ {"role":"system","content":"You are a helpful assistant."}, *st.session_state.chat_history]
    )
    assistant_response=response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    print(st.session_state.chat_history)
    print("--------------------")
    print("--------------------")
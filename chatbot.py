import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv(".env")

# Streamlit page setup
st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="centered"
)

# Custom styles for title and footer
st.markdown(
    """
    <style>
    /* Chat title */
    .chat-title {
        font-family: 'Poppins', sans-serif; /* modern, clean font */
        font-size: 38px;
        font-weight: 800;
        color: #2E4057; /* elegant dark blue */
        letter-spacing: 1px;
        margin-bottom: 2px;
    }

    /* Footer text */
    .developed-text {
        font-family: 'Roboto', sans-serif; /* sleek and readable */
        font-size: 13px;           
        font-weight: 500;           
        color: rgba(46, 64, 87, 0.6); /* semi-transparent dark blue */
        margin-top: 0;          
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    }
    </style>

    <div class="chat-title">💬 Ask me..</div>
    <div class="developed-text">Chat with your AI Assistant — Developed by Srini</div>
    """,
    unsafe_allow_html=True
)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Chat input from user
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    # Display user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Generate response from LLM
    conversation = [{"role": "system", "content": "You are a helpful assistant."}] + st.session_state.chat_history
    response = llm.invoke(input=conversation)
    assistant_response = response.content

    # Store assistant response
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

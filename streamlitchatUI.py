import os
import openai
import streamlit as st
import requests
from dotenv import load_dotenv
load_dotenv("credentials.env")

st.title("Chat with me!")

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_type = "azure"
openai.api_version = os.environ['OPENAI_API_VERSION']
openai_model = os.environ['OPENAI_MODEL']


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = openai_model

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            engine=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ] + [{"role": "system", "content": "Assistant is a llm chatbot."}],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

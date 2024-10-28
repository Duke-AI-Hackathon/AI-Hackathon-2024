from bot_utils import *

import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="openai_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    gemini_api_key = st.text_input("Gemini API Key", key="gemini_api_key", type="password")
    "[Get a Gemini API key](https://aistudio.google.com/app/apikey)"

    huggingface_api_key = st.text_input("HuggingFace API Key", key="huggingface_api_key", type="password")
    "[Get a HuggingFace API key](https://huggingface.co/settings/tokens)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot")

option = st.selectbox(
    "Which LLM do you want to use?",
    ("GPT-3.5 Turbo", "Gemini 1.5 Flash", "HuggingFace Phi-3 Mini 4k Instruct"),
)

if option == "GPT-3.5 Turbo":

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        with st.chat_message("user"):
            st.markdown(prompt)

            st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            reply = get_completion_openai(st.session_state.messages, openai_api_key)

            st.markdown(reply)

            st.session_state.messages.append({"role": "assistant", "content": reply})

elif option == "Gemini 1.5 Flash":

    if "gem_messages" not in st.session_state:
        st.session_state.gem_messages = []
    if "gem_send" not in st.session_state:
        st.session_state.gem_send = []

    for message in st.session_state.gem_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        if not gemini_api_key:
            st.info("Please add your Gemini API key to continue.")
            st.stop()
        
        with st.chat_message("user"):
            st.markdown(prompt)

            st.session_state.gem_messages.append({"role": "user", "content": prompt})
            
            st.session_state.gem_send.append({"role": "user", "parts": [prompt]})

        with st.chat_message("assistant"):
            reply = get_completion_gemini(st.session_state.gem_send, gemini_api_key)

            st.markdown(reply)

            st.session_state.gem_messages.append({"role": "assistant", "content": reply})
            
            st.session_state.gem_send.append({"role": "model", "parts": [reply]})

elif option == "HuggingFace Phi-3 Mini 4k Instruct":

    if "hf_messages" not in st.session_state:
        st.session_state.hf_messages = []
    if "hf_send" not in st.session_state:
        st.session_state.hf_send = []
    
    for message in st.session_state.hf_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        if not huggingface_api_key:
            st.info("Please add your HuggingFace API key to continue.")
            st.stop()

        with st.chat_message("user"):
            st.markdown(prompt)

            st.session_state.hf_messages.append({"role": "user", "content": prompt})
            st.session_state.hf_send.append(("user", prompt))

        with st.chat_message("assistant"):
            reply = get_completion_hf(prompt, huggingface_api_key)

            st.markdown(reply)

            st.session_state.hf_messages.append({"role": "assistant", "content": reply})
            st.session_state.hf_send.append(("system", reply))
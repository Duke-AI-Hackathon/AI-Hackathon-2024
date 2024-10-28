from openai import OpenAI

import google.generativeai as genai

from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

def get_completion_openai(messages, openai_key):

    openai_client = OpenAI(
        api_key=openai_key,
    )

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )

    reply = response.choices[0].message.content

    return reply

def get_completion_gemini(messages, gemini_key):

    genai.configure(api_key=gemini_key)

    gemini_client = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a helpful assistant")

    response = gemini_client.generate_content(
        messages,
        generation_config=genai.GenerationConfig(
        # response_mime_type="application/json",
        temperature=0,
        )
    )

    return response.text

def get_completion_hf(messages, hf_key):
    
    login(token=hf_key)

    llm = HuggingFaceEndpoint(
        repo_id="microsoft/Phi-3-mini-4k-instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )

    hf_client = ChatHuggingFace(llm=llm, verbose=True)
    
    response = hf_client.invoke(messages)

    return response.content
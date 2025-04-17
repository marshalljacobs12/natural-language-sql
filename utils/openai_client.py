## utils/openai_client.py
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_key = st.secrets["openai"]["api_key"] if "openai" in st.secrets else os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)

def get_embeddings(texts: list[str]) -> list[list[float]]:
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [d.embedding for d in res.data]

def chat_completion(prompt: str, model="gpt-4") -> str:
    res = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful SQL assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
    )
    return res.choices[0].message.content.strip()



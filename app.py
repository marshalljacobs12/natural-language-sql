## app.py
import streamlit as st
import numpy as np

from rag.schema_utils import extract_schema
from rag.retriever import load_chroma_index
from rag.prompt_builder import build_prompt
from rag.sql_executor import execute_sql, is_query_safe, explain_sql
from utils.openai_client import get_embeddings, chat_completion

# Load vector index and metadata from Chroma
db = load_chroma_index()

# Streamlit UI
st.set_page_config(page_title="SQL RAG Assistant", layout="wide")
st.title("🧠 Chat with Your SQL Database")

st.subheader("1. Ask your question")
question = st.text_input("Your question:")

if question:
    # Embed user question and retrieve top-k chunks
    question_vec = get_embeddings([question])[0]  # Get single embedding
    results = db.similarity_search_by_vector(question_vec, k=3)
    top_chunks = [doc.page_content for doc in results]

    st.subheader("2. Retrieved Schema Context")
    st.code("\n\n".join(top_chunks), language="text")

    # Build prompt and get SQL
    full_prompt = build_prompt(question, top_chunks)
    generated_sql = chat_completion(full_prompt)

    st.subheader("3. Generated SQL")
    editable_sql = st.text_area("Edit SQL before running:", value=generated_sql, height=150)

    if st.button("Run SQL"):
        if is_query_safe(editable_sql):
            try:
                cols, rows = execute_sql(editable_sql)
                st.success("Query ran successfully!")
                st.subheader("4. Query Results")
                st.dataframe([dict(zip(cols, row)) for row in rows])
            except Exception as e:
                st.error(f"SQL Execution Error: {e}")
        else:
            st.error("Unsafe SQL query detected. Only SELECT statements are allowed.")

    if st.button("Explain this SQL"):
        explanation = explain_sql(editable_sql, chat_completion)
        st.subheader("5. Explanation")
        st.markdown(f"**Explanation:**\n{explanation}")

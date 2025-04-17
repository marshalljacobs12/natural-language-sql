## rag/prompt_builder.py

def build_prompt(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    return f"""
You are an expert SQL assistant.
Given the following database schema and user question, generate a syntactically correct and safe SQL query.

Schema:
{context}

Question:
{question}

SQL:
""".strip()
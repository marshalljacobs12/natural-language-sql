## scripts/train.py
import os
from rag.schema_utils import extract_schema
from rag.retriever import build_chroma_index
from langchain.schema import Document

DB_PATH = "data/sample.db"

def train():
    print("[+] Extracting schema from DB...")
    chunks = extract_schema(DB_PATH)

    print(f"[+] Found {len(chunks)} chunks. Building Chroma index...")

    # Wrap strings into LangChain Documents
    docs = [Document(page_content=chunk) for chunk in chunks]
    build_chroma_index(docs)

    print("Index built and saved to ./chroma_db.")

if __name__ == "__main__":
    train()

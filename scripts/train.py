## scripts/train.py
import os
from rag.schema_utils import extract_schema
from rag.retriever import build_faiss_index

DB_PATH = "data/sample.db"
INDEX_PATH = "faiss_index/schema.index"

def train():
    print("[+] Extracting schema from DB...")
    chunks = extract_schema(DB_PATH)

    print(f"[+] Found {len(chunks)} chunks. Building FAISS index...")
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    build_faiss_index(chunks, INDEX_PATH)

    print("Index built and saved.")

if __name__ == "__main__":
    train()
import os
from typing import List
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])

CHROMA_DIR = "./chroma_db"

def embed_texts(texts: List[str]) -> List[List[float]]:
    """Return list of embeddings for each text."""
    return embedding_model.embed_documents(texts)

def build_chroma_index(docs: List[Document]):
    """Builds a Chroma vector index from documents."""
    db = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory=CHROMA_DIR
    )
    db.persist()
    return db

def load_chroma_index():
    """Loads the existing Chroma index from disk."""
    return Chroma(
        embedding_function=embedding_model,
        persist_directory=CHROMA_DIR
    )

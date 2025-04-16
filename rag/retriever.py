# retriever.py
import faiss
import numpy as np
from typing import List
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])


def embed_texts(texts: List[str]) -> np.ndarray:
    return np.array(embedding_model.embed_documents(texts))


def build_faiss_index(texts: List[str], index_path: str):
    vectors = embed_texts(texts)
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    faiss.write_index(index, index_path)

    with open(index_path + ".meta", "w") as f:
        for t in texts:
            f.write(t.replace("\n", " ") + "\n")

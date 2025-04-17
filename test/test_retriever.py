from rag.retriever import embed_texts

def test_embedding_format():
    chunks = ["Table: users", "Table: orders"]
    vectors = embed_texts(chunks)
    assert len(vectors) == 2

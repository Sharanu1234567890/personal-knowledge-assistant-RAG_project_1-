# src/retriever.py
def retrieve_docs(query, collection, model, top_k=5):
    query_emb = model.encode([query])
    results = collection.query(query_embeddings=query_emb, n_results=top_k)
    docs = results["documents"][0]
    return docs

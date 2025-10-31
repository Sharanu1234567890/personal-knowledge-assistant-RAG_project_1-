# src/embed_store.py
from sentence_transformers import SentenceTransformer
import chromadb

def create_vector_store(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection("docs")

    for i, ch in enumerate(chunks):
        emb = model.encode([ch["content"]])[0]
        collection.add(
            embeddings=[emb],
            documents=[ch["content"]],
            metadatas=[{"source": ch["source"]}],
            ids=[str(i)]
        )
    return collection, model

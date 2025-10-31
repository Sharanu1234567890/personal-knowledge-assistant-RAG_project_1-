# src/chunker.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = []
    for doc in texts:
        for chunk in splitter.split_text(doc["text"]):
            chunks.append({"source": doc["name"], "content": chunk})
    return chunks

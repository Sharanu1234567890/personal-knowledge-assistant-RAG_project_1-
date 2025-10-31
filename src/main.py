# src/main.py

from openai import OpenAI
from loader import load_documents
from chunker import chunk_documents
from embeded_store import create_vector_store
from Retriver import retrieve_docs

# ✅ Use Groq API endpoint
client = OpenAI(
    api_key="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",  # Replace with your Groq key
    base_url="https://api.groq.com/openai/v1"
)

# 🧩 Step 1: Load and process data
texts = load_documents("data")
chunks = chunk_documents(texts)
collection, model = create_vector_store(chunks)

# 🧠 Step 2: Get query and retrieve top docs
query = input("Ask your question: ")
docs = retrieve_docs(query, collection, model)

# 📚 Step 3: Build context for LLM
context = "\n\n".join(docs)
prompt = f"Use the context below to answer:\n{context}\n\nQuestion: {query}"

# 🤖 Step 4: Send to Groq LLM (Llama 3.1)
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

# 📝 Step 5: Display answer
print("\nAnswer:\n", response.choices[0].message.content)

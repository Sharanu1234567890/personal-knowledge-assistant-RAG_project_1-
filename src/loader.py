# src/loader.py
from PyPDF2 import PdfReader
import os

def load_documents(data_path="data"):
    texts = []
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(data_path, file))
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            texts.append({"name": file, "text": text})
        elif file.endswith(".txt"):
            with open(os.path.join(data_path, file), "r", encoding="utf-8") as f:
                texts.append({"name": file, "text": f.read()})
    return texts

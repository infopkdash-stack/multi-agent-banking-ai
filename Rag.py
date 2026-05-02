from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import json

class SafeGoogleEmbeddings(GoogleGenerativeAIEmbeddings):
    def embed_documents(self, texts):
        # Workaround for the Gemini embedding API bug that returns 1 embedding for a list
        return [self.embed_query(text) for text in texts]

def load_data():
    with open("data/incidents.json") as f:
        data = json.load(f)
    texts = [f"{d['issue']} {d['resolution']}" for d in data]
    return texts

def create_vector_store():
    embeddings = SafeGoogleEmbeddings(model="models/gemini-embedding-2")
    texts = load_data()
    return FAISS.from_texts(texts, embeddings)
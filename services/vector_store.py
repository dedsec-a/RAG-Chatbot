from langchain_community.vectorstores import FAISS
import os 

VECTOR_STORE_PATH = "faiss store"

def save_to_vector_store(docs,embeddings):
    db = FAISS.from_documents(documents=docs ,embedding=embeddings)
    db.save_local(VECTOR_STORE_PATH)

def load_vector_store(embeddings):
    if os.path.exists(VECTOR_STORE_PATH):
        return FAISS.load_local(VECTOR_STORE_PATH,embeddings=embeddings,allow_dangerous_deserialization= True)
    else:
        return None

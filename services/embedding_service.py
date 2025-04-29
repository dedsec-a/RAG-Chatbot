from langchain_community.embeddings import HuggingFaceEmbeddings
from services.vector_store import save_to_vector_store
from utils.pdf_loader import split_pdf


def embed_docs(file_content):

    docs = split_pdf(file_content=file_content)
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    save_to_vector_store(docs,embeddings)

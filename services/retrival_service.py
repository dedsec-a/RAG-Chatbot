# Making the ReTrival Chain 
from services.vector_store import load_vector_store
from services.llm_services import generate_answer
from langchain_community.embeddings import HuggingFaceEmbeddings


# Main Logic of  Generating the Answers

def get_answer(question:str):
    embedings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    db = load_vector_store(embeddings=embedings)
    if not db:
        return "No Documents Found . Please Upload the PDF First"
    
    retriver = db.as_retriever()
    docs  = retriver.invoke(question)
    return generate_answer(docs= docs , question= question)

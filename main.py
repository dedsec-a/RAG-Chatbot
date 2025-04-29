from fastapi import FastAPI ,UploadFile ,File
from services.embedding_service import embed_docs
from services.retrival_service import get_answer
from models.request_model import Question_request

app = FastAPI()

@app.post("/upload_pdf")
async def upload_def(file :UploadFile = File(...)):
    content = await file.read() # reading the Content 
    embed_docs(content) # Embeding the Content to Make a Vector Store
    return {"message":"Documnet Embeded and Stored Sucessufully"}

@app.post("/ask_question")
async def ask_question(request:Question_request):
    answer = get_answer(request.question)
    return {"answer":answer}

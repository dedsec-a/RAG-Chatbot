from pydantic import BaseModel

class Question_request(BaseModel):
    question: str
from fastapi import FastAPI
from pydantic import BaseModel
from src.embedding import create_and_populate_collection
from src.retrieval import retrieve
from src.generation import generate_answer

app = FastAPI()
col = create_and_populate_collection(...)

class Q(BaseModel):
    question: str

@app.post("/rag/")
def rag(q: Q):
    docs = retrieve(q.question, col)
    context = "\n\n".join(docs)
    answer = generate_answer(context, q.question)
    return {"answer": answer}

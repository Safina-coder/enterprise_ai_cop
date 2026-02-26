from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import add_docs, generate_answer
from app.agentic import agentic_task

app = FastAPI(title="Enterprise AI Copilot")

class Question(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    docs = [
        "Enterprise AI Copilot helps automate internal workflows.",
        "RAG pipelines retrieve documents and feed them to LLM for context.",
        "Agentic AI can suggest next steps after analyzing documents."
    ]
    add_docs(docs)

@app.post("/ask")
def ask_question(q: Question):
    return {"answer": generate_answer(q.question)}

@app.post("/agentic")
def ask_agentic(q: Question):
    return agentic_task(q.question)

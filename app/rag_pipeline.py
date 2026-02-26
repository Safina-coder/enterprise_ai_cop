from .embeddings import get_embedding
from .vector_db import upsert_document, query_vector
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def add_docs(docs):
    for i, doc in enumerate(docs):
        emb = get_embedding(doc)
        upsert_document(f"doc_{i}", emb, {"text": doc})

def generate_answer(question):
    q_emb = get_embedding(question)
    context_docs = query_vector(q_emb, top_k=3)
    context_text = "\n".join(context_docs)
    
    prompt = f"Answer the question based on the context below:\nContext:\n{context_text}\nQuestion: {question}\nAnswer:"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=300
    )
    return response['choices'][0]['text'].strip()

import pinecone
import os
from dotenv import load_dotenv

load_dotenv()
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT")
)

INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(INDEX_NAME, dimension=1536)

index = pinecone.Index(INDEX_NAME)

def upsert_document(doc_id, embedding, metadata):
    index.upsert([(doc_id, embedding, metadata)])

def query_vector(query_embedding, top_k=3):
    results = index.query(query_embedding, top_k=top_k, include_metadata=True)
    return [r['metadata']['text'] for r in results['matches']]

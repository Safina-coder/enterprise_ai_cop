# enterprise_ai_cop

Features:
- RAG pipeline with Pinecone vector DB
- OpenAI LLM integration
- Agentic multi-step workflows
- React frontend + FastAPI backend
- Docker & Docker Compose ready

Setup:
1. Copy `.env.example` → `.env` and add API keys
2. `docker-compose up --build`
3. Frontend: http://localhost:3000
4. Backend API: http://localhost:8000

Endpoints:
- POST `/ask` → simple RAG answer
- POST `/agentic` → answer + suggested next steps

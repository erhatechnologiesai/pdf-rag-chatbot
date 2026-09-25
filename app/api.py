from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import QueryRequest, QueryResponse
from app.services.rag_engine import search_and_synthesize, populate_sample_pdf

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.on_event("startup")
def init():
    populate_sample_pdf()

@app.get("/")
def index():
    return {"rag_engine": settings.PROJECT_NAME, "status": "active"}

@app.post("/query", response_model=QueryResponse)
def query_pdf(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    ans, citations = search_and_synthesize(req.query, req.top_k)
    return QueryResponse(query=req.query, answer=ans, citations=citations)

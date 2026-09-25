from pydantic import BaseModel
from typing import List, Optional

class DocumentChunk(BaseModel):
    chunk_id: str
    source_pdf: str
    page_number: int
    text: str

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: List[dict]

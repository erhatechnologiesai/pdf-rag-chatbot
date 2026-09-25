import math
import re
from typing import List, Dict
from app.config import settings

CHUNKS_STORE: List[Dict] = []

def chunk_text(text: str, doc_name: str = "sample.pdf", page: int = 1):
    words = text.split()
    step = settings.CHUNK_SIZE - settings.CHUNK_OVERLAP
    chunks = []
    idx = 0
    for i in range(0, len(words), max(1, step)):
        chunk_words = words[i:i + settings.CHUNK_SIZE]
        if not chunk_words:
            continue
        c_text = " ".join(chunk_words)
        chunks.append({
            "chunk_id": f"{doc_name}-p{page}-c{idx}",
            "source_pdf": doc_name,
            "page_number": page,
            "text": c_text
        })
        idx += 1
    return chunks

def populate_sample_pdf():
    global CHUNKS_STORE
    sample_text = (
        "Erha Technologies specializes in autonomous multi-agent systems and enterprise RAG pipelines. "
        "Our RAG framework uses hybrid search combining dense embeddings with BM25 lexical ranking. "
        "Data ingested through our pipelines undergoes semantic chunking, deduplication, and metadata enrichment. "
        "The retrieval latency averages under 35 milliseconds on optimized vector indices. "
        "Security is enforced through granular role-based document access controls."
    )
    CHUNKS_STORE = chunk_text(sample_text, "Erha_AI_Whitepaper.pdf", 1)

def compute_similarity(q: str, doc: str) -> float:
    q_words = set(re.findall(r'\w+', q.lower()))
    doc_words = set(re.findall(r'\w+', doc.lower()))
    if not q_words or not doc_words:
        return 0.0
    intersection = len(q_words.intersection(doc_words))
    return intersection / math.sqrt(len(q_words) * len(doc_words))

def search_and_synthesize(query: str, top_k: int = 3):
    if not CHUNKS_STORE:
        populate_sample_pdf()
        
    scored = []
    for c in CHUNKS_STORE:
        score = compute_similarity(query, c["text"])
        scored.append((score, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    
    top_results = [item[1] for item in scored[:top_k] if item[0] > 0]
    if not top_results:
        top_results = CHUNKS_STORE[:1]
        
    context = " ".join([c["text"] for c in top_results])
    answer = f"Based on the analyzed document: {context}"
    citations = [{"source": c["source_pdf"], "page": c["page_number"], "chunk_id": c["chunk_id"]} for c in top_results]
    return answer, citations

# PDF RAG Chatbot

An end-to-end Retrieval-Augmented Generation (RAG) chatbot for PDF document analysis featuring text extraction, sliding-window chunking, vector similarity retrieval, and exact page-level source citations.

Part of the **50 AI Automation Projects Portfolio** by [ERHA TECHNOLOGIES](https://github.com/erhatechnologiesai).

---

## Architecture
```mermaid
flowchart TD
    PDF[PDF Upload] --> Extractor[Text & Page Extractor]
    Extractor --> Chunker[Sliding Window Chunker]
    Chunker --> Embeddings[Vector Embeddings Store]
    Query([User Query]) --> Search[Cosine Similarity Search]
    Embeddings --> Search
    Search --> Context[Relevant Context Chunks]
    Context --> LLM[Context-Augmented LLM Synthesizer]
    LLM --> Answer[Answer with Page Citations]
```

## Testing
```bash
python -m unittest tests/test_pdf_rag.py
```

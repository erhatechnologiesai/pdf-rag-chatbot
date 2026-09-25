import os
class Settings:
    PROJECT_NAME: str = "PDF RAG Chatbot"
    VERSION: str = "1.0.0"
    CHUNK_SIZE: int = 250
    CHUNK_OVERLAP: int = 50
    DEMO_MODE: bool = os.getenv("DEMO_MODE", "true").lower() == "true"
settings = Settings()

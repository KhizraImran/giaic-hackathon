import os
import google.generativeai as genai
from qdrant_client import QdrantClient, models
import logging

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")

# Try to connect to remote Qdrant first, fallback to local mode if not available
try:
    # Attempt to connect to remote Qdrant server
    qdrant_client = QdrantClient(
        url=QDRANT_HOST,
        api_key=QDRANT_API_KEY,
    )
    # Test connection
    qdrant_client.get_collections()
    logging.info("Successfully connected to remote Qdrant server")
except Exception as e:
    logging.warning(f"Could not connect to remote Qdrant server: {e}. Using local mode.")
    # Fallback to local Qdrant instance
    qdrant_client = QdrantClient(path="./qdrant_data_local")
    logging.info("Initialized local Qdrant instance")

def get_qdrant_client() -> QdrantClient:
    return qdrant_client

def generate_gemini_embedding(text: str) -> list[float]:
    try:
        response = genai.embed_content(model="models/embedding-001", content=text)
        return response['embedding']
    except Exception as e:
        print(f"Error generating Gemini embedding: {e}")
        return []


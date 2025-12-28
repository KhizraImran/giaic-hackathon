# ingest_docs.py
import os
import asyncio
import logging
import uuid
from pathlib import Path
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import sys
import logging as log

# Add the project root (one level above chatbot_backend) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "book_content"

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(f"Loaded QDRANT_HOST: {repr(QDRANT_HOST)}")
logger.debug(f"Loaded QDRANT_API_KEY: {repr(QDRANT_API_KEY)}")

# Try to connect to remote Qdrant first, fallback to local mode if not available
try:
    # Attempt to connect to remote Qdrant server
    client = QdrantClient(
        url=QDRANT_HOST,
        api_key=QDRANT_API_KEY,
    )
    # Test connection
    client.get_collections()
    logger.info("Successfully connected to remote Qdrant server")
except Exception as e:
    logger.warning(f"Could not connect to remote Qdrant server: {e}. Using local mode.")
    # Fallback to local Qdrant instance
    client = QdrantClient(path="./qdrant_data_local")
    logger.info("Initialized local Qdrant instance")

# Create collection if it doesn't exist
if not client.collection_exists(COLLECTION_NAME):
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE) # Gemini embedding-001 size
    )
    logger.info(f"Collection '{COLLECTION_NAME}' created.")
else:
    logger.info(f"Collection '{COLLECTION_NAME}' already exists.")

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables and configure Gemini API
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    logger.error("GEMINI_API_KEY not found in environment variables. Please set it.")

def generate_gemini_embedding(text: str) -> list[float]:
    try:
        response = genai.embed_content(model="models/embedding-001", content=text)
        return response['embedding']
    except Exception as e:
        logger.error(f"Error generating Gemini embedding: {e}")
        return []

# Read and process documents
def ingest_documents():
    docs_path = Path(__file__).parent.parent / "website" / "docs"
    md_files = list(docs_path.rglob("*.md"))

    for doc_file in md_files:
        logger.info(f"Processing {doc_file}...")
        try:
            text = doc_file.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Failed to read {doc_file}: {e}")
            continue

        # Simple chunking by 500 characters
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        points = []

        for chunk in chunks:
            embedding = generate_gemini_embedding(chunk)
            if embedding:  # Only add points if embedding was generated successfully
                points.append(
                    PointStruct(
                        id=str(uuid.uuid4()),  # Safe UUID for Qdrant
                        vector=embedding,
                        payload={"text": chunk, "source": str(doc_file)}
                    )
                )

        # Upsert points to Qdrant
        try:
            client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)
        except Exception as e:
            logger.error(f"Failed to upsert points for {doc_file}: {e}")

# Run ingestion
if __name__ == "__main__":
    ingest_documents()
    logger.info("Ingestion completed.")

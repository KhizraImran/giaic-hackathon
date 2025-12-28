import os
import pytest
from qdrant_client import models

# Assuming qdrant_client is initialized in app/services/qdrant.py
# For testing, we might need a way to inject a mock client or ensure it's configured.
# For now, we'll try to use the actual client, assuming .env is loaded.

# Load environment variables for local testing if not already loaded
from dotenv import load_dotenv
load_dotenv()

# Import the actual qdrant_client from the services module
# This might need adjustment based on how the client is exposed.
# For now, let's assume get_qdrant_client() is callable directly or mocked.
from chatbot_backend.app.services.qdrant import get_qdrant_client

@pytest.fixture(scope="module")
def qdrant_test_client():
    client = get_qdrant_client()
    # Ensure the client is connected before tests run
    # In a real scenario, you might have a dedicated test collection
    # or clear existing data.
    try:
        client.get_collections()
    except Exception as e:
        pytest.fail(f"Qdrant client initialization failed: {e}")
    return client

def test_qdrant_connection(qdrant_test_client):
    # If the fixture ran without failing, the connection is good
    assert qdrant_test_client is not None

def test_qdrant_collection_management(qdrant_test_client):
    collection_name = "test_collection_for_rag"
    # Ensure collection does not exist from previous runs
    qdrant_test_client.delete_collection(collection_name=collection_name, timeout=5) # Added timeout

    # Create a new collection
    qdrant_test_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
        timeout=5 # Added timeout
    )

    # Check if the collection exists
    collections = qdrant_test_client.get_collections().collections
    assert any(c.name == collection_name for c in collections)

    # Clean up: delete the collection
    qdrant_test_client.delete_collection(collection_name=collection_name, timeout=5) # Added timeout
    collections = qdrant_test_client.get_collections().collections
    assert not any(c.name == collection_name for c in collections)

def test_qdrant_upsertion(qdrant_test_client):
    collection_name = "test_upsertion_collection"
    qdrant_test_client.delete_collection(collection_name=collection_name, timeout=5) # Added timeout

    qdrant_test_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
        timeout=5 # Added timeout
    )

    # Simulate upserting a point
    points = [
        models.PointStruct(
            id=1,
            vector=[0.1] * 768, # Dummy vector
            payload={
                "text": "This is a test document about physical AI.",
                "source": "test_document_1"
            }
        )
    ]

    qdrant_test_client.upsert(
        collection_name=collection_name,
        points=points,
        wait=True # Ensure points are indexed before next operation
    )

    # Verify upsertion by retrieving the point
    retrieved_points = qdrant_test_client.retrieve(collection_name=collection_name, ids=[1])
    assert len(retrieved_points) == 1
    assert retrieved_points[0].payload["text"] == "This is a test document about physical AI."

    qdrant_test_client.delete_collection(collection_name=collection_name, timeout=5) # Added timeout

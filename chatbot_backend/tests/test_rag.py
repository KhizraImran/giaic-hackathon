import pytest
from fastapi.testclient import TestClient
from app.main import app as fastapi_app  # Assuming app is in chatbot_backend/app/main.py

# Adjust this if your main app is in a different location

def test_rag_chat_endpoint():
    with TestClient(fastapi_app) as client:
        # First, ensure there's some content in Qdrant for RAG to work.
        # This part might need to be mocked in a true unit test or handled in setup.
        # For this integration test, we'll assume Qdrant is accessible and has data.
        # (The Qdrant client unit tests already confirm basic Qdrant functionality.)

        response = client.post("/rag/chat", json={
            "user_query": "What is ROS 2?",
            "collection_name": "book_content" # Ensure this collection exists and is populated
        })

        assert response.status_code == 200
        response_data = response.json()
        assert "response" in response_data
        assert isinstance(response_data["response"], str)
        assert len(response_data["response"]) > 0

        # Optional: Add more assertions to check the content of the response
        # For example, checking for keywords that should be present if RAG works

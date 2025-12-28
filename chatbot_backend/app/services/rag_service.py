import os
import google.generativeai as genai
from typing import List, Dict, Any

from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from app.services.qdrant import get_qdrant_client, generate_gemini_embedding

# Configure Gemini API - moved to main.py
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# if GEMINI_API_KEY:
#     genai.configure(api_key=GEMINI_API_KEY)
# else:
#     print("GEMINI_API_KEY not found in environment variables.")

def get_gemini_model():
    try:
        # Ensure the model is available before returning
        model = genai.GenerativeModel('gemini-pro')
        return model
    except Exception as e:
        print(f"Error initializing Gemini model: {e}")
        return None

async def retrieve_context_from_qdrant(query_embedding: List[float], collection_name: str, limit: int = 3, selected_text: str = None) -> List[Dict[str, Any]]:
    qdrant_client = get_qdrant_client()
    search_params = {"hnsw_ef": 128, "exact": False}

    query_filter = None
    if selected_text:
        # If specific text is selected, try to prioritize documents containing that text
        # This is a simplified approach, a more advanced solution might involve re-ranking or keyword extraction
        query_filter = Filter(must=[
            FieldCondition(
                key="text",
                match=MatchValue(value=selected_text)
            )
        ])

    search_result = qdrant_client.search(
        collection_name=collection_name,
        query_vector=query_embedding,
        query_filter=query_filter,
        limit=limit,
        with_payload=True,
        search_params=search_params,
    )

    context = []
    for hit in search_result:
        context.append({"text": hit.payload.get("text"), "source": hit.payload.get("source")})
    return context

async def generate_rag_response(user_query: str, collection_name: str, selected_text: str = None) -> str:

    gemini_model = get_gemini_model()
    if not gemini_model:
        return "Error: Gemini model not initialized."

    # 1. Generate embedding for the user query
    query_embedding = generate_gemini_embedding(user_query)
    if not query_embedding:
        return "Error: Could not generate embedding for the query."

    # 2. Retrieve relevant context from Qdrant
    context = await retrieve_context_from_qdrant(query_embedding, collection_name, selected_text=selected_text)

    if not context:
        return "I couldn't find any relevant information in the textbook to answer your question."

    # 3. Construct prompt for Gemini with retrieved context
    context_str = "\n".join([doc["text"] for doc in context])
    prompt_parts = [
        f"You are a helpful assistant for a Physical AI & Humanoid Robotics textbook. Answer the user's question based ONLY on the following context. If the answer is not in the context, state that you don't know.\n\nContext:\n{context_str}\n\nQuestion: {user_query}",
    ]
    if selected_text:
        prompt_parts.insert(0, f"The user has also highlighted this text: {selected_text}\n")

    # 4. Generate response using Gemini
    try:
        response = await gemini_model.generate_content_async(prompt_parts)
        return response.text
    except Exception as e:
        print(f"Error generating Gemini response: {e}")
        return "An error occurred while generating the response."

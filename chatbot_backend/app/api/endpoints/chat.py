from fastapi import APIRouter, HTTPException, Body
from typing import Annotated
from ...services.rag_service import generate_rag_response

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(
    user_query: Annotated[str, Body(..., description="The user's query")],
    collection_name: Annotated[str, Body(..., description="The Qdrant collection to query")],
    selected_text: Annotated[str | None, Body(description="Optional selected text from the document for context")] = None,
):
    """
    Handles RAG chat queries.
    """
    try:
        response = await generate_rag_response(user_query, collection_name, selected_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

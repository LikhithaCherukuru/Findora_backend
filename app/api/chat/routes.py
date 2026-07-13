from fastapi import APIRouter

from app.schemas.chat.chat_request import ChatRequest
from app.schemas.chat.chat_response import ChatResponse

from app.services.ai.chat_service import ChatService


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)

chat_service = ChatService()


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
):

    return chat_service.ask(
        request.question
    )
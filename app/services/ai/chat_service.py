from app.ai.rag.rag_service import RAGService


class ChatService:

    def __init__(self):
        self.rag = RAGService()

    def ask(self, message: str):
        return self.rag.ask(message)
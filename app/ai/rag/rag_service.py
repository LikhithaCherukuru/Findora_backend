from app.ai.search.search_service import SearchService
from app.ai.rag.prompt_builder import PromptBuilder
from app.ai.rag.llm_service import LLMService


class RAGService:

    def __init__(self):
        self.search = SearchService()
        self.llm = LLMService()

    def ask(self, question: str):

        chunks = self.search.search_documents(question)

        prompt = PromptBuilder.build(question, chunks)

        answer = self.llm.generate(prompt)

        files = []

        for chunk in chunks:
            file_name = chunk["file_id"]

            if file_name not in files:
                files.append(file_name)

        return {
            "answer": answer,
            "sources": files,
        }
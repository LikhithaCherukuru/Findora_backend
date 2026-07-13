from app.ai.llm.groq_service import GroqService


class LLMService:

    def __init__(self):

        self.llm = GroqService()


    def generate(
        self,
        prompt: str
    ):

        return self.llm.generate(prompt)
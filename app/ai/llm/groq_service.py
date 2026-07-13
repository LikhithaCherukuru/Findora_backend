from groq import Groq

from app.core.config import settings


class GroqService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = "llama-3.3-70b-versatile"

    def generate(
        self,
        prompt: str
    ):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=0,

            max_tokens=1024,
        )

        return response.choices[0].message.content
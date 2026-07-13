class PromptBuilder:

    @staticmethod
    def build(question: str, chunks: list):

        context = "\n\n".join(
            chunk["chunk_text"]
            for chunk in chunks
        )

        prompt = f"""
You are an AI assistant for Smart File Finder.

Answer ONLY using the information below.

If the answer is not present, reply exactly:

"I couldn't find that information in your documents."

Context:

{context}

Question:

{question}

Answer:
"""

        return prompt
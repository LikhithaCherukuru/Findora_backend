import re


class TextCleaner:

    def clean(self, text: str) -> str:

        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text)

        # Remove blank lines
        text = re.sub(r"\n+", "\n", text)

        return text.strip()
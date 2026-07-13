from pathlib import Path

from app.ai.extractors.extractor_factory import ExtractorFactory
from app.ai.preprocessing.cleaner import TextCleaner
from app.ai.preprocessing.chunker import TextChunker
from app.ai.embeddings.embedding_service import EmbeddingService
from app.ai.vector_store.qdrant_service import QdrantService


class ProcessingPipeline:

    def __init__(self):

        self.cleaner = TextCleaner()

        self.chunker = TextChunker(
            chunk_size=500,
            overlap=50,
        )

        self.embedding_service = EmbeddingService()

        self.qdrant_service = QdrantService()


    def process_file(
        self,
        file_path: str,
        file_id: str,
        page_number: int | None = None,
    ):

        extension = Path(file_path).suffix.lower()

        extractor = ExtractorFactory.get_extractor(extension)

        if extractor is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )


        text = extractor.extract_text(file_path)


        cleaned_text = self.cleaner.clean(text)


        chunks = self.chunker.split_text(cleaned_text)


        for index, chunk in enumerate(chunks):

            embedding = self.embedding_service.create_embedding(
                chunk
            )


            self.qdrant_service.upsert_embedding(

                embedding=embedding,

                chunk_text=chunk,

                metadata={
                    "file_id": file_id,
                    "file_name": Path(file_path).name,
                    "chunk_index": index,
                    "page_number": page_number,
                    "token_count": len(chunk.split()),
                    "embedding_model": "all-MiniLM-L6-v2"
                }
            )


        return len(chunks)
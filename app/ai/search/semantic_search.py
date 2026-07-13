from app.ai.embeddings.embedding_service import EmbeddingService
from app.ai.vector_store.qdrant_service import QdrantService


class SemanticSearch:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.qdrant_service = QdrantService()


    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = (
            self.embedding_service
            .create_embedding(query)
        )


        results = (
            self.qdrant_service
            .search(
                query_embedding=query_embedding,
                top_k=top_k
            )
        )


        return results
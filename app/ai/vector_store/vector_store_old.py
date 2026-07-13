from app.core.database import supabase


class VectorStore:

    def insert_chunk(
        self,
        file_id: str,
        chunk_index: int,
        page_number: int | None,
        chunk_text: str,
        token_count: int,
    ):

        response = (
            supabase.table("document_chunks")
            .insert(
                {
                    "file_id": file_id,
                    "chunk_index": chunk_index,
                    "page_number": page_number,
                    "chunk_text": chunk_text,
                    "token_count": token_count,
                }
            )
            .execute()
        )

        return response.data[0]

    def insert_embedding(
        self,
        chunk_id: str,
        embedding: list[float],
        model_name: str = "all-MiniLM-L6-v2",
    ):

        response = (
            supabase.table("embeddings")
            .insert(
                {
                    "chunk_id": chunk_id,
                    "embedding_model": model_name,
                    "embedding": embedding,
                }
            )
            .execute()
        )

        return response.data[0]

    def get_chunks_by_file(self, file_id: str):

        response = (
            supabase.table("document_chunks")
            .select("*")
            .eq("file_id", file_id)
            .order("chunk_index")
            .execute()
        )

        return response.data
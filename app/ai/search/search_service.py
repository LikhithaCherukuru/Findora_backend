from app.ai.search.semantic_search import SemanticSearch


class SearchService:

    def __init__(self):
        self.search_engine = SemanticSearch()

    def search_documents(self, query: str):

        results = self.search_engine.search(query)

        return results
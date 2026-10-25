import chromadb

class ChromaDBClient:
    """Class responsible for interacting with the ChromaDB database, creating collections, adding documents, and querying the database.
    
    """
    def __init__(self, collection_name, configuration=None):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name = collection_name, configuration=configuration)
    
    def add_document(self, ids: list[str], documents: list[str], metadatas: list[dict] = None):
        self.collection.add(ids=ids, documents=documents, metadatas=metadatas)
        
    def query(self, query_text: str, n_results: int = 1):
        results = self.collection.query(query_texts=[query_text], n_results=n_results)
        return results
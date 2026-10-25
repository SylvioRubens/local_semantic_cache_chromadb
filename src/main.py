from .chroma import ChromaDBClient 
from . import config
import json

def main():
    
    # Configuration for the ChromaDB collection, specifying the use of cosine similarity for the HNSW index.
    configuration = {
        "hnsw": {
            "space": "cosine"
        }
    }
    chroma_client = ChromaDBClient(
        collection_name=config.COLLECTION_NAME,
        configuration=configuration
    )
    
    # Add 3 questions with distinct IDS
    with open(f"{config.PROJECT_ROOT}/data/evaluation/questions_v1.json", "r") as f:
        data = json.load(f)
        questions = data["questions"]
        
        #Getting only the first 3 questions for demonstration purposes
        for i, question in enumerate(questions[:3]):
            chroma_client.add_document(
                ids=[question["question_id"]],
                documents=[question["question"]]
            )
            
    #Exact match query
    # query_question = "Under READ COMMITTED, can I read data before another transaction commits?"
    
    #Different question with similar meaning to the one added to the collection
    query_question = "Does READ COMMITTED allow a transaction to see another transaction's uncommitted changes?"

    query_results = chroma_client.query(query_text=query_question, n_results=1)

    distance = query_results['distances'][0][0]
    matched_id = query_results['ids'][0][0]
    similarity_score = 1 - distance  # Convert distance to similarity score
    
    print(f"Query: {query_question}")
    print(f"Matched ID: {matched_id}")
    print(f"Distance: {distance}")
    print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()
    

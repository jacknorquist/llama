import chromadb
from chromadb.utils import embedding_functions


import chromadb
from chromadb.utils import embedding_functions

# Load persistent collection
def load_collection(persist_dir="chroma_store"):
    client = chromadb.PersistentClient(path=persist_dir)
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-small-en-v1.5")
    return client.get_or_create_collection(name="rag_docs", embedding_function=ef)

# Semantic search function
def semantic_search(collection, query, n=3):
    results = collection.query(
        query_texts=[query],
        n_results=n,
        include=["documents", "distances"]
    )

    for i in range(n):
        print(f"\n🔍 Match {i+1}")
        print(f"📄 Document: {results['documents'][0][i][:300]}...")
        print(f"📏 Distance: {results['distances'][0][i]:.4f}")


# Example usage
if __name__ == "__main__":
    collection = load_collection()
    query = input("Enter Your Question:")
    semantic_search(collection, query)

import os
import json
from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings


def preprocess_and_save(input_dir="data/raw", output_dir="data/processed"):
    os.makedirs(output_dir, exist_ok=True)
    for path in Path(input_dir).glob("*"):
        text = Path(path).read_text(encoding="utf-8")
        # TODO: better splitting (by paragraphs / tokens)
        chunks = [text[i:i + 2000] for i in range(0, len(text), 2000)]
        for idx, chunk in enumerate(chunks):
            out = Path(output_dir) / f"{path.stem}_{idx}.json"
            out.write_text(json.dumps({"text": chunk}))


def create_and_populate_collection(processed_dir="data/processed", persist_dir="chroma_store"):
    client = chromadb.PersistentClient(path=persist_dir)

    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-small-en-v1.5")

    collection = client.get_or_create_collection("rag_docs", embedding_function=ef)

    docs, ids = [], []
    for file in Path(processed_dir).glob("*.json"):
        data = json.loads(file.read_text())
        ids.append(file.stem)
        docs.append(data["text"])

    collection.add(documents=docs, ids=ids)

    return collection


if __name__ == "__main__":
    preprocess_and_save()
    collection = create_and_populate_collection()


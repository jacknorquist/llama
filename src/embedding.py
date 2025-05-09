import os, json
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
from sentence_transformers import SentenceTransformer

def preprocess_and_save(input_dir="data/raw", output_dir="data/processed"):
    os.makedirs(output_dir, exist_ok=True)
    for path in Path(input_dir).glob("*"):
        text = Path(path).read_text(encoding="utf-8")
        # TODO: better splitting (by paragraphs / tokens)
        chunks = [text[i:i+2000] for i in range(0, len(text), 2000)]
        for idx, chunk in enumerate(chunks):
            out = Path(output_dir) / f"{path.stem}_{idx}.json"
            out.write_text(json.dumps({"text": chunk}))

def create_and_populate_collection(processed_dir="data/processed"):
    client = chromadb.Client()
    ef = embedding_functions.SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")
    col = client.create_collection("rag_docs", embedding_function=ef)

    docs, ids = [], []
    for file in Path(processed_dir).glob("*.json"):
        data = json.loads(file.read_text())
        ids.append(file.stem)
        docs.append(data["text"])
    col.add(documents=docs, ids=ids)
    return col
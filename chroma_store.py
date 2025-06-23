# chroma_store.py

import chromadb
import os
from datetime import datetime

def store_versions_in_chroma(chapter_id: str):
    db_path = "chroma_db"

    # ✅ Use the new client interface (2024+)
    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_or_create_collection(name="book_chapters")

    base_path = "outputs"
    version_files = {
        "original": f"{chapter_id}.txt",
        "spun": f"{chapter_id}_spun.txt",
        "reviewed": f"{chapter_id}_reviewed.txt",
        "final": f"{chapter_id}_final.txt"
    }

    for version, filename in version_files.items():
        file_path = os.path.join(base_path, filename)
        if not os.path.exists(file_path):
            print(f"[⚠️] Missing: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        doc_id = f"{chapter_id}_{version}"
        metadata = {
            "chapter_id": chapter_id,
            "version": version,
            "timestamp": str(datetime.now())
        }

        collection.add(
            documents=[content],
            metadatas=[metadata],
            ids=[doc_id]
        )

        print(f"[✅] Stored: {doc_id}")

    print("\n📚 All available versions stored in ChromaDB.")

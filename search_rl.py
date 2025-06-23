# search_rl.py

import chromadb
import os

def load_text_length(base_path, file_name):
    path = os.path.join(base_path, file_name)
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        return len(f.read())

def calculate_score(version, original_len, version_len):
    ai_scores = {
        "spun": 0.7,
        "reviewed": 0.8,
        "final": 0.85,
        "original": 0.6
    }

    length_ratio = 1 - abs(original_len - version_len) / max(original_len, 1)
    human_bonus = 0.2 if version == "final" else 0

    return ai_scores.get(version, 0.5) + length_ratio + human_bonus

def get_best_version(chapter_id: str):
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("book_chapters")

    results = collection.get(where={"chapter_id": chapter_id}, include=["documents", "metadatas"])

    if not results["documents"]:
        print(f"[❌] No versions found for {chapter_id}")
        return None

    base_path = "outputs"
    original_len = load_text_length(base_path, f"{chapter_id}.txt")

    best_score = -1
    best_version = None

    print("\n📊 RL-Mock Scoring Report:")

    for doc, meta in zip(results["documents"], results["metadatas"]):
        version = meta["version"]
        version_len = len(doc)
        score = calculate_score(version, original_len, version_len)
        version_id = f"{chapter_id}_{version}"
        print(f"🔹 {version_id}: Score = {score:.2f}")
        if score > best_score:
            best_score = score
            best_version = (version_id, doc)

    print(f"\n🏆 Best version chosen: {best_version[0]}")
    return best_version

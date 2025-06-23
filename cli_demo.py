# cli_demo.py

import chromadb
import os
from search_rl import get_best_version

def list_versions(chapter_id):
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("book_chapters")
    results = collection.get(where={"chapter_id": chapter_id}, include=["documents", "metadatas"])

    if not results["documents"]:
        print(f"[❌] No versions found for {chapter_id}")
        return []

    versions = []
    for meta, doc in zip(results["metadatas"], results["documents"]):
        version_id = f"{chapter_id}_{meta['version']}"
        versions.append((version_id, doc))
    return versions

def cli():
    print("📘 Welcome to the Book Chapter Version CLI")
    chapter_id = input("Enter Chapter ID (e.g., chapter_1): ").strip()

    while True:
        print("\n🔹 Options:")
        print("1. 📊 List all available versions")
        print("2. 🏆 View BEST version (RL logic)")
        print("3. 📖 Read a specific version")
        print("4. ❌ Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            versions = list_versions(chapter_id)
            if versions:
                print("\n📚 Available Versions:")
                for v, _ in versions:
                    print("•", v)

        elif choice == "2":
            best = get_best_version(chapter_id)
            if best:
                print(f"\n🏆 Best Version: {best[0]}")
                print(f"\n📝 Preview:\n{best[1][:700]}")

        elif choice == "3":
            version = input("Enter version name (e.g., chapter_1_final): ").strip()
            path = os.path.join("outputs", f"{version}.txt")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    print(f"\n📝 Content of {version}:\n")
                    print(f.read()[:1000])  # Limit output
            else:
                print("❌ File not found.")

        elif choice == "4":
            print("👋 Exiting...")
            break

        else:
            print("⚠️ Invalid input. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    cli()

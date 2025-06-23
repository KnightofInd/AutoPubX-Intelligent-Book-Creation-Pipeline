# pipeline.py

import argparse
from scrapebook import scrape_chapter
from spin_the_wheel import spin_chapter
from review_time_by_llm import review_chapter
from human_editor_simulation import simulate_edit
from chroma_store import store_versions_in_chroma


def run_pipeline(url, chapter_id):
    print(f"\n📘 Starting pipeline for Chapter: {chapter_id}")

    # 🧠 Get custom prompt from user input
    print("\n✍️ Enter your custom prompt for the LLM:")
    prompt = input(">>> ")

    print("\n🔍 [1/4] Scraping chapter content and screenshot...")
    original_text = scrape_chapter(url, chapter_id)

    print("🌀 [2/4] Spinning chapter with Gemini...")
    spun_text = spin_chapter(original_text, chapter_id, prompt)

    print("\n✅ Pipeline completed up to LLM spin.")
    print(f"📄 Files saved in: outputs/{chapter_id}*.txt and outputs/{chapter_id}.png\n")

    print("🌀 [2/4] Spinning chapter with Gemini...")
    spun_text = spin_chapter(original_text, chapter_id, prompt)

    print("📝 [3/4] Reviewing spun chapter with Gemini editor...")
    reviewed_text = review_chapter(spun_text, chapter_id)

    print("📝 [3/4] Reviewing spun chapter with Gemini editor...")
    reviewed_text = review_chapter(spun_text, chapter_id)

    print("👤 [4/4] Simulating human manual edits...")
    final_text = simulate_edit(reviewed_text, chapter_id)

    print("🧠 [5/5] Storing all versions in ChromaDB...")
    store_versions_in_chroma(chapter_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Book Pipeline")
    parser.add_argument("--url", type=str, required=True, help="URL of the chapter to scrape")
    parser.add_argument("--chapter_id", type=str, default="chapter_1", help="Unique chapter ID")

    args = parser.parse_args()
    run_pipeline(args.url, args.chapter_id)

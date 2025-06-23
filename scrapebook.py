# scrape.py
from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url: str, chapter_id: str) -> str:
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    text_path = os.path.join(output_dir, f"{chapter_id}.txt")
    img_path = os.path.join(output_dir, f"{chapter_id}.png")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        page.screenshot(path=img_path, full_page=True)
        print(f"[📸] Screenshot saved: {img_path}")

        content = page.locator("#mw-content-text").inner_text()
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[📄] Text saved: {text_path}")

        browser.close()

    return content

# spin_the_wheel.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def spin_chapter(text: str, chapter_id: str, prompt: str) -> str:
    prompt = f"{prompt}\n\n{text}"

    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    spun_text = response.text

    output_path = os.path.join("outputs", f"{chapter_id}_spun.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(spun_text)

    print(f"[🌀] Spun version saved: {output_path}")
    return spun_text

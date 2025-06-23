# llm_review.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def review_chapter(spun_text: str, chapter_id: str) -> str:
    review_prompt = (
        "You are an experienced editor. Improve the grammar, structure, clarity, and flow of the following text "
        "without changing the meaning or storyline. Keep the language natural and professional.\n\n"
        f"{spun_text}"
    )

    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
    response = model.generate_content(review_prompt)
    reviewed_text = response.text

    output_path = os.path.join("outputs", f"{chapter_id}_reviewed.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(reviewed_text)

    print(f"[📝] Reviewed version saved: {output_path}")
    return reviewed_text

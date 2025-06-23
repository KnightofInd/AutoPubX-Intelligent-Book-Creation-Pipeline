# simulate_human_edit.py

import os

def simulate_edit(reviewed_text: str, chapter_id: str) -> str:
    # Add a simple line that simulates a "manual edit"
    simulated_final = f"[Edited by human editor]\n\n{reviewed_text.strip()}"

    output_path = os.path.join("outputs", f"{chapter_id}_final.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(simulated_final)

    print(f"[👤] Final (simulated human edited) version saved: {output_path}")
    return simulated_final

# run_rl.py

import sys
from search_rl import get_best_version

if len(sys.argv) != 2:
    print("Usage: python run_rl.py <chapter_id>")
    sys.exit(1)

chapter_id = sys.argv[1]
result = get_best_version(chapter_id)

if result:
    print("\n📄 Preview of Best Version:\n")
    print(result[1][:700]) 

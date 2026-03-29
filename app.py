import os
from src.pipeline import InsightGen

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "data.txt")

engine = InsightGen()

# Step 1: Take input from user
print("\nPaste your document below (press ENTER twice to finish):\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

# Step 2: Save to file
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(text)

# Step 3: Summarize
summary = engine.summarize_document(DATA_PATH)

# Step 4: Output
print("\n--- SUMMARY ---\n")
print(summary)
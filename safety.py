from src.pipeline import InsightGen
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample.txt")

engine = InsightGen()

print("=== SAFETY TESTS ===\n")

# 🔥 Test cases
test_cases = {
    "Empty Input": "",
    "Short Input": "AI is useful.",
    "Long Input": "Artificial intelligence is transforming healthcare. " * 200,
    "Normal Input": """Artificial intelligence is transforming healthcare by improving diagnosis,
    treatment accuracy, and patient care workflows while also introducing challenges such as
    data privacy and high implementation costs."""
}

for name, text in test_cases.items():
    print(f"\n--- {name} ---")

    # Write test input
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    try:
        summary = engine.summarize_document(DATA_PATH)

        if len(summary.strip()) == 0:
            print("⚠️ Empty summary generated")
        else:
            print("Summary:", summary)

    except Exception as e:
        print("❌ Error:", e)
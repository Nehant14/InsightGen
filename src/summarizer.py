from transformers import pipeline

class Summarizer:
    def __init__(self):
        self.model = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize(self, text):
        words = text.split()
        input_len = len(words)

        # Handle very small input
        if input_len < 30:
            return text

        # Dynamic length control
        max_len = max(40, int(input_len * 0.5))
        min_len = max(20, int(input_len * 0.25))

        # Ensure valid relationship
        if min_len >= max_len:
            min_len = max_len - 10

        return self.model(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False,
            no_repeat_ngram_size=3
        )[0]['summary_text']
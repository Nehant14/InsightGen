import os
from src.loader import DocumentLoader
from src.chunker import TextChunker
from src.summarizer import Summarizer

class InsightGen:
    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.summarizer = Summarizer()

    def summarize_document(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Load full text
        text = self.loader.load_txt(file_path)

        # Split into chunks
        chunks = self.chunker.chunk(text)

        # Step 1: summarize each chunk
        partial_summaries = []
        for chunk in chunks:
            summary = self.summarizer.summarize(chunk[:800])
            partial_summaries.append(summary)

        # Step 2: combine summaries
        combined = " ".join(partial_summaries)

        # # Step 3: final summary
        # final_summary = self.summarizer.summarize(combined[:1000])

        return combined
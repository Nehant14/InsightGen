import re
import nltk
from nltk.tokenize import sent_tokenize


def ensure_nltk():
    """
    Ensure required NLTK resources are available
    """
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')


class TextChunker:
    def __init__(self, chunk_size=150, overlap=30):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

        # Ensure tokenizer is ready
        ensure_nltk()

    def split_sentences(self, text):
        """
        Split text into sentences using NLTK
        """
        sentences = sent_tokenize(text.strip())

        # Fallback: if NLTK fails (e.g., one giant sentence), split by comma
        if len(sentences) <= 1:
            sentences = re.split(r',\s+', text.strip())  # strip to remove leading/trailing whitespace 

        return sentences

    def chunk(self, text):
        """
        Convert text into overlapping semantic chunks
        """
        sentences = self.split_sentences(text)

        chunks = []  # final chunk list -> list of string.
        current_chunk = []
        current_length = 0

        for sentence in sentences:
            words = sentence.split()
            sentence_length = len(words)

            # Handle extremely long sentence
            if sentence_length > self.chunk_size:   # split it into sub-chunks of exactly chunk_size words.
                words_list = sentence.split() # split the sentence into words
                for i in range(0, len(words_list), self.chunk_size): # iterate over the words 
                    chunks.append(" ".join(words_list[i:i + self.chunk_size])) # create a chunk of chunk_size words and add it to the chunks list
                continue

            # If adding sentence exceeds chunk size → finalize chunk
            if current_length + sentence_length > self.chunk_size:
                if current_chunk:
                    chunks.append(" ".join(current_chunk))

                # Apply overlap
                if self.overlap > 0 and current_chunk:
                    overlap_words = " ".join(current_chunk).split()[-self.overlap:]
                    current_chunk = [" ".join(overlap_words)]
                    current_length = len(overlap_words)
                else:
                    current_chunk = []
                    current_length = 0

            current_chunk.append(sentence)
            current_length += sentence_length

        # ✅ Add last chunk
        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks
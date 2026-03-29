import os

class DocumentLoader:
    def load_txt(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
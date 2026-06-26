# InsightGen

**InsightGen** is a Retrieval-Augmented Generation (RAG) based research paper summarization system that enables users to upload research papers and receive accurate, context-aware summaries. Instead of relying solely on the language model's internal knowledge, the system retrieves the most relevant sections from the uploaded document and uses them to generate responses. This approach significantly reduces hallucinations while improving factual accuracy and relevance.

The project is designed for students, researchers, and professionals who need to quickly understand lengthy academic papers. Along with summarization, it can answer questions about the uploaded paper by retrieving only the most relevant information before generating a response.

## Features

* 📄 Upload research papers in PDF format.
* 🔍 Retrieval-Augmented Generation (RAG) pipeline for accurate context retrieval.
* 🤖 AI-generated summaries based on document content.
* ❓ Interactive question-answering using retrieved document chunks.
* ⚡ Fast semantic search using vector embeddings.
* 🛡️ Built-in safety evaluation to assess robustness against prompt injection and unsafe inputs.
* 📊 Evaluation script for measuring retrieval and summarization performance.

## Technology Stack

* **Python** for backend development.
* **Large Language Models (LLMs)** for summarization and question answering.
* **Vector Database / Embedding Model** for semantic document retrieval.
* **RAG Pipeline** to combine retrieval with AI-generated responses.

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application using:

```bash
python app.py
```

This launches the RAG-based research paper summarization system, allowing users to upload research papers, generate summaries, and ask context-aware questions.

## Evaluation

To evaluate the performance of the retrieval and summarization pipeline, run:

```bash
python evaluate.py
```

The evaluation script can be used to analyze metrics such as retrieval quality, answer relevance, summarization accuracy, and overall system effectiveness.

## Safety Testing

To verify the application's robustness against malicious prompts and unsafe inputs, execute:

```bash
python safety.py
```

The safety testing module checks how well the system handles prompt injection attempts, harmful queries, invalid inputs, and other security-related edge cases to ensure reliable and trustworthy responses.

## Future Improvements

* Multi-document retrieval and comparison.
* Citation-aware answer generation.
* Support for additional document formats such as DOCX and TXT.
* Improved evaluation metrics and benchmarking.
* Enhanced user interface and deployment options.

## License

This project is intended for educational and research purposes.

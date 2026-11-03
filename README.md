# Document Q&A Assistant using a Local LLM

A Python-based application that extracts text from PDF documents and answers user questions using a locally hosted Large Language Model (LLM). It uses Ollama and Qwen 2.5 3B to generate context-based answers in structured JSON format without requiring paid API services.

## Features

- Extracts text from PDF documents.
- Answers questions based on the provided document.
- Uses a locally hosted LLM through Ollama.
- Generates structured JSON responses containing the answer, source, and confidence.
- Runs locally without requiring a paid API key.

## Tech Stack

- **Language:** Python
- **LLM Runtime:** Ollama
- **LLM Model:** Qwen 2.5 3B
- **PDF Processing:** PyPDF
- **Output Format:** JSON

## Project Structure

```text
Document Extraction/
├── documents/
│   └── sample.pdf
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- Ollama installed on your computer
- Qwen 2.5 3B model downloaded

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the LLM model

```bash
ollama pull qwen2.5:3b
```

### 5. Add a PDF document

Place your PDF inside the `documents` folder and name it `sample.pdf`.

### 6. Run the application

```bash
python main.py
```

Enter your questions when prompted. Type `exit` to stop the application.

## Example Output

```json
{
  "answer": "Data recovery is the process of retrieving lost or inaccessible data.",
  "source": "Page 2",
  "confidence": "High"
}
```

*Example response only. Actual answers depend on the PDF document.*

## Future Improvements

- Implement Retrieval-Augmented Generation (RAG) for larger documents.
- Add document chunking and semantic search.
- Develop a web interface for uploading PDFs and asking questions.

## License

This project is intended for educational and learning purposes.

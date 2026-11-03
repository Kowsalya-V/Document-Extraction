import ollama
from pypdf import PdfReader


def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)

    document_text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""

        document_text += f"\nPage {page_number}:\n{page_text}"

    return document_text


def ask_question(document_text, question):
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": """
                Answer questions using only the provided document.
                If the answer is missing, say that it is not available.
                Return JSON with answer, source, and confidence.
                """
            },
            {
                "role": "user",
                "content": f"""
                Document:
                {document_text}

                Question:
                {question}
                """
            }
        ],
        format="json"
    )

    return response["message"]["content"]


# Load the PDF
document_text = extract_pdf_text("documents/sample.pdf")

print("PDF loaded successfully!")

# Ask questions
while True:
    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    answer = ask_question(document_text, question)

    print("\nAnswer:")
    print(answer)
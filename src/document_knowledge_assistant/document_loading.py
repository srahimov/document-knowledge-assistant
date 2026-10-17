from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document


def load_pdf(pdf_path: Path) -> Document:
    """Read a PDF and return its text with source information."""
    reader = PdfReader(pdf_path)

    page_texts = []
    for page in reader.pages:
        page_texts.append(page.extract_text() or "")

    text = "\n\n".join(page_texts)

    return Document(
        page_content=text,
        metadata={"source": pdf_path.name},
    )
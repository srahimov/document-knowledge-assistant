import json
from pathlib import Path

from langchain_core.documents import Document


def save_chunks(chunks: list[Document], output_path: Path) -> None:
    """Save chunk text and metadata to a JSON file."""
    records = []

    for chunk in chunks:
        records.append({
            "page_content": chunk.page_content,
            "metadata": chunk.metadata,
        })

    output_path.parent.mkdir(parents=True, exist_ok=True)

    json_text = json.dumps(records, indent=2, ensure_ascii=False)
    output_path.write_text(json_text, encoding="utf-8")


def load_chunks(input_path: Path) -> list[Document]:
    """Read saved chunk records and rebuild LangChain Documents."""
    json_text = input_path.read_text(encoding="utf-8")
    records = json.loads(json_text)

    chunks = []

    for record in records:
        document = Document(
            page_content=record["page_content"],
            metadata=record["metadata"],
        )
        chunks.append(document)

    return chunks
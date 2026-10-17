import json
from pathlib import Path

from langchain_core.documents import Document

from document_knowledge_assistant.document_loading import load_pdf
from document_knowledge_assistant.text_splitting import split_document
from document_knowledge_assistant.local_storage import save_chunks


def ingest_current_documents(
    source_dir: Path,
    output_path: Path,
) -> list[Document]:
    """Load, split, and save the current hotel documents."""
    manifest_path = source_dir / "corpus_manifest.json"
    manifest_text = manifest_path.read_text(encoding="utf-8")
    manifest = json.loads(manifest_text)

    all_chunks = []

    for source in manifest["source_documents"]:
        if not source["ingest"] or source["status"] != "CURRENT":
            continue

        pdf_path = source_dir / source["filename"]
        document = load_pdf(pdf_path)

        document.metadata.update({
            "doc_id": source["doc_id"],
            "title": source["title"],
            "version": source["version"],
            "status": source["status"],
            "audience": source["audience"],
            "owner": source["owner"],
            "effective_from": source["effective_from"],
            "effective_to": source["effective_to"],
        })

        chunks = split_document(document)
        all_chunks.extend(chunks)

        print(f"{source['filename']}: {len(chunks)} chunks")

    save_chunks(all_chunks, output_path)

    return all_chunks
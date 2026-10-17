from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document(document: Document) -> list[Document]:
    """Split a document into smaller chunks, keeping its metadata."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 150,
    )

    return splitter.split_documents([document])

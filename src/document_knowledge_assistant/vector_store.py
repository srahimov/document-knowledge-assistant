from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import InMemoryVectorStore
from pathlib import Path


def build_vector_store(
    chunks: list[Document],
    embedding_model: Embeddings,
) -> InMemoryVectorStore:
    """Embed the chunks and store their vectors in memory."""
    vector_store = InMemoryVectorStore(embedding_model)
    vector_store.add_documents(chunks)

    return vector_store

def save_vector_store(
    vector_store: InMemoryVectorStore,
    index_path: Path,
) -> None:
    """Save vectors, text, and metadata to a local file."""
    vector_store.dump(str(index_path))


def load_vector_store(
    index_path: Path,
    embedding_model: Embeddings,
) -> InMemoryVectorStore:
    """Restore a saved vector store without embedding its chunks again."""
    return InMemoryVectorStore.load(
        str(index_path),
        embedding=embedding_model,
    )
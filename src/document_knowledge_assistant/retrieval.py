from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore


def search_chunks(
    vector_store: InMemoryVectorStore,
    question: str,
    k: int = 3,
) -> list[Document]:
    """Return the chunks most similar to the question."""
    return vector_store.similarity_search(question, k=k)
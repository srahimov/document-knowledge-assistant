from langchain.tools import tool
from langchain_core.tools import BaseTool
from langchain_core.vectorstores import InMemoryVectorStore

from document_knowledge_assistant.retrieval import search_chunks


def create_search_tool(
    vector_store: InMemoryVectorStore,
) -> BaseTool:
    """Create a search tool connected to the local vector store."""

    @tool
    def search_hotel_documents(question: str) -> str:
        """Search current Skyview Hotel documents for policies, operations,
        employee onboarding, rooms, amenities, meetings, and events."""
        chunks = search_chunks(vector_store, question)

        passages = []

        for chunk in chunks:
            passages.append(
                f"Source: {chunk.metadata['source']}\n"
                f"{chunk.page_content}"
            )

        return "\n\n".join(passages)

    return search_hotel_documents
from langchain_openai import OpenAIEmbeddings


def create_embeddings() -> OpenAIEmbeddings:
    """Create the OpenAI embedding client."""
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
    )
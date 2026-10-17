from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel


def create_chat_model() -> BaseChatModel:
    """Create the chat model used to answer hotel questions."""
    return init_chat_model(
        "openai:gpt-6-luna",
    )
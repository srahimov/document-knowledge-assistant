from langgraph.checkpoint.memory import InMemorySaver

def create_checkpointer() -> InMemorySaver:
    """Create conversation-state storage for this application run."""

    return InMemorySaver()

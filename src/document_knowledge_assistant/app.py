from pathlib import Path

from document_knowledge_assistant.ingestion import ingest_current_documents
from document_knowledge_assistant.embeddings import create_embeddings
from document_knowledge_assistant.vector_store import (
    build_vector_store,
    save_vector_store,
    load_vector_store,
)
from document_knowledge_assistant.agents import create_hotel_agent


def run() -> None:
    project_root = Path(__file__).resolve().parents[2]

    source_dir = project_root / "output/pdf/skyview-hotel"
    chunks_path = project_root / "data/chunks/skyview_current.json"
    index_path = project_root / "data/indexes/skyview_current.json"

    embedding_model = create_embeddings()

    if index_path.exists():
        vector_store = load_vector_store(index_path, embedding_model)
        print("Loaded the current hotel document index")
    else:
        chunks = ingest_current_documents(source_dir, chunks_path)

        print("*" * 25)
        print(f"Prepared {len(chunks)} chunks across current documents")
        print(f"Saved chunks to: {chunks_path}")

        vector_store = build_vector_store(chunks, embedding_model)
        save_vector_store(vector_store, index_path)

        print(f"Saved the new vector index to: {index_path}")


    agent = create_hotel_agent(vector_store)

    print("\nSkyview Hotel Assistant")
    print("Type a hotel question, or type exit to finish.")

    thread_config = {
        "configurable": {
            "thread_id": "hotel-session"
        }
    }

    message_count = 0

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Session ended.")
            break

        if not question:
            continue

        result = agent.invoke({
            "messages": [
                {"role": "user", "content": question}
            ]
        }, config = thread_config)

        new_messages = result["messages"][message_count:]
        message_count = len(result["messages"])

        for message in new_messages:
            if message.type == "tool":
                print(f"\nTool used: {message.name}")

        print(f"Conversation messages: {message_count}")

        print("\nAssistant:")
        print(result["messages"][-1].text)
from pathlib import Path

from dotenv import load_dotenv

from document_knowledge_assistant.app import run


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    load_dotenv(project_root / ".env")

    run()
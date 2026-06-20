from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def chunk_documents(documents):
    """
    Split documents into chunks
    while preserving metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for document in documents:

        text = document["text"]

        metadata = document["metadata"]

        split_texts = splitter.split_text(text)

        for chunk_text in split_texts:

            chunks.append(
    {
        "text": chunk_text,
        "metadata": {
            **metadata,
            "chunk_id": len(chunks)
        }
    }
)

    return chunks
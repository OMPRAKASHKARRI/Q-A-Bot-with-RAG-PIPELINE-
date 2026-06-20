from document_loader import load_documents
from chunker import chunk_documents

from vector_store import get_collection
from embedder import get_embeddings


def run_ingestion():

    print("\nLoading documents...\n")

    documents = load_documents("data")

    print(
        f"Loaded {len(documents)} documents"
    )

    print("\nChunking...\n")

    chunks = chunk_documents(documents)

    print(
        f"Created {len(chunks)} chunks"
    )

    collection = get_collection()

    documents_text = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        chunk["metadata"]
        for chunk in chunks
    ]

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    print("\nGenerating embeddings...\n")

    embeddings = get_embeddings(
        documents_text
    )

    print(
        f"Generated {len(embeddings)} embeddings"
    )

    collection.add(
    ids=ids,
    documents=documents_text,
    embeddings=embeddings,
    metadatas=metadatas
)
    print(
        "\nIndexing completed successfully!"
    )


if __name__ == "__main__":
    run_ingestion()
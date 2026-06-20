from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def get_embeddings(texts):
    """
    Generate embeddings in batches.
    Assignment requirement:
    Batch embedding generation.
    """

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings.tolist()
from sentence_transformers import SentenceTransformer
from vector_store import get_collection
from config import TOP_K

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(user_query):

    collection = get_collection()

    query_embedding = model.encode(
        user_query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    contexts = []
    citations = []

    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):

        source = meta["source"]
        page = meta["page"]

        contexts.append(
            {
                "text": doc,
                "source": source,
                "page": page
            }
        )

        citations.append(
            f"{source} (Page {page})"
        )

    return contexts, citations
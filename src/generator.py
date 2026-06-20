from groq import Groq
from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)


def generate_answer(
    question,
    contexts,
    citations
):

    context_text = "\n\n".join(
        [context["text"] for context in contexts]
    )

    prompt = f"""
You are a document question answering assistant.

Use ONLY the provided context.

If the answer is not found in the context, respond exactly:

"I cannot find the answer in the provided documents."

Do not use external knowledge.

Context:
{context_text}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    if "I cannot find the answer" in answer:
        return answer

    unique_citations = list(
        dict.fromkeys(citations)
    )

    citation_text = "\n".join(
        [f"- {c}" for c in unique_citations]
    )

    final_response = f"""
{answer}

Sources:
{citation_text}
"""

    return final_response
from query import retrieve_context
from generator import generate_answer

question = "What is artifical Intelligence"

contexts, citations = retrieve_context(
    question
)

answer = generate_answer(
    question,
    contexts,
    citations
)

print(answer)
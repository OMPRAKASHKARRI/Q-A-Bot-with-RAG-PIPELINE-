from query import retrieve_context
from generator import generate_answer


def main():

    print("\n" + "=" * 60)
    print("📚 DOCUMENT Q&A BOT (RAG)")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    while True:

        question = input(
            "Ask a question: "
        )

        if question.lower() == "exit":

            print("\nGoodbye! 👋")

            break

        try:

            contexts, citations = retrieve_context(
                question
            )

            answer = generate_answer(
                question,
                contexts,
                citations
            )

            print("\n" + "=" * 60)
            print("ANSWER")
            print("=" * 60)

            print(answer)

            print("\n" + "=" * 60)
            print("RETRIEVED CHUNKS")
            print("=" * 60)

            for i, context in enumerate(
                contexts,
                start=1
            ):

                print(f"\nChunk {i}")

                print("-" * 40)

                print(
                    f"Source: {context['source']}"
                )

                print(
                    f"Page: {context['page']}"
                )

                print()

                print(
                    context["text"][:300]
                )

            print("\n")

        except Exception as e:

            print(
                f"\nError: {e}\n"
            )


if __name__ == "__main__":
    main()
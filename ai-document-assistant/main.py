import argparse
import os

from openai import OpenAI


def answer_local(document: str, question: str) -> str:
    doc_lower = document.lower()
    question_terms = [w for w in question.lower().split() if len(w) > 3]
    if any(term in doc_lower for term in question_terms):
        return "Relevant information appears in the document. Use OpenAI mode for a richer answer."
    return "I could not find a confident local answer."


def answer_openai(document: str, question: str, model: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": "Answer using only the provided document text."},
            {
                "role": "user",
                "content": f"Document:\n{document}\n\nQuestion:\n{question}",
            },
        ],
    )
    return response.output_text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask questions about document text.")
    parser.add_argument("--document", required=True, help="Document text")
    parser.add_argument("--question", required=True)
    parser.add_argument("--mode", choices=["local", "openai"], default="local")
    parser.add_argument("--model", default="gpt-4.1-mini")
    args = parser.parse_args()

    if args.mode == "local":
        print(answer_local(args.document, args.question))
    else:
        print(answer_openai(args.document, args.question, args.model))


if __name__ == "__main__":
    main()

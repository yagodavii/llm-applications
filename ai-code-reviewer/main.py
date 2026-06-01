import argparse
import os
import re

from openai import OpenAI


def local_review(code: str) -> dict:
    issues = []
    improvements = []

    if "except:" in code:
        issues.append("Bare except detected; it can hide real errors.")
        improvements.append("Catch specific exceptions instead of using bare except.")

    if "eval(" in code:
        issues.append("Potential security risk: eval() usage.")
        improvements.append("Avoid eval(); prefer safe parsers or explicit logic.")

    if re.search(r"print\(.*debug", code, flags=re.IGNORECASE):
        improvements.append("Remove debug prints before production.")

    if "TODO" in code:
        improvements.append("Resolve TODOs before merging.")

    if not issues:
        issues.append("No obvious critical issues found by local heuristics.")

    if not improvements:
        improvements.append("Add tests and type hints to improve reliability.")

    return {"issues": issues, "improvements": improvements}


def openai_review(code: str, model: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": "You are a senior software reviewer."},
            {
                "role": "user",
                "content": (
                    "Review this code and return potential bugs, maintainability issues, and concrete improvements."
                    f"\n\nCode:\n{code}"
                ),
            },
        ],
    )
    return response.output_text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Review a code snippet with AI.")
    parser.add_argument("--code", required=True)
    parser.add_argument("--mode", choices=["local", "openai"], default="local")
    parser.add_argument("--model", default="gpt-4.1-mini")
    args = parser.parse_args()

    if args.mode == "local":
        result = local_review(args.code)
        print("Code Review")
        print("Issues:")
        for i in result["issues"]:
            print(f"- {i}")
        print("Improvements:")
        for i in result["improvements"]:
            print(f"- {i}")
    else:
        print(openai_review(args.code, args.model))


if __name__ == "__main__":
    main()

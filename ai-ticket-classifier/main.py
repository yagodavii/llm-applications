import argparse
import os
import re

from openai import OpenAI

CATEGORY_RULES = {
    "billing": ["invoice", "payment", "charge", "refund", "billing"],
    "technical": ["error", "bug", "crash", "exception", "login", "timeout"],
    "account": ["password", "account", "profile", "username", "locked"],
    "feature_request": ["feature", "request", "improve", "enhancement"],
}


def local_classify(text: str) -> dict:
    t = text.lower()

    category = "general"
    max_hits = 0
    for cat, keywords in CATEGORY_RULES.items():
        hits = sum(1 for k in keywords if k in t)
        if hits > max_hits:
            max_hits = hits
            category = cat

    if any(x in t for x in ["urgent", "asap", "down", "cannot"]):
        priority = "high"
    elif any(x in t for x in ["soon", "when possible", "question"]):
        priority = "medium"
    else:
        priority = "low"

    pos = len(re.findall(r"\b(great|thanks|good|awesome|love)\b", t))
    neg = len(re.findall(r"\b(bad|angry|hate|terrible|frustrated|issue|problem)\b", t))
    if neg > pos:
        sentiment = "negative"
    elif pos > neg:
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return {"category": category, "priority": priority, "sentiment": sentiment}


def openai_classify(text: str, model: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": "You classify support tickets."},
            {
                "role": "user",
                "content": (
                    "Classify this support ticket into category, priority, and sentiment. "
                    f"Return concise JSON.\n\nTicket:\n{text}"
                ),
            },
        ],
    )
    return response.output_text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify support tickets.")
    parser.add_argument("--text", required=True)
    parser.add_argument("--mode", choices=["local", "openai"], default="local")
    parser.add_argument("--model", default="gpt-4.1-mini")
    args = parser.parse_args()

    if args.mode == "local":
        result = local_classify(args.text)
        print("Ticket Classification")
        for k, v in result.items():
            print(f"{k}: {v}")
    else:
        print(openai_classify(args.text, args.model))


if __name__ == "__main__":
    main()

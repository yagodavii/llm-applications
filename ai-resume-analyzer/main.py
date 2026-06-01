import argparse
import os
import re
from collections import Counter

from openai import OpenAI

TECH_KEYWORDS = {
    "python", "java", "javascript", "typescript", "sql", "aws", "azure", "gcp", "docker", "kubernetes",
    "react", "node", "fastapi", "django", "flask", "pandas", "numpy", "pytorch", "tensorflow", "git",
}


def extract_technologies(text: str) -> list[str]:
    tokens = set(re.findall(r"[a-zA-Z0-9+#.]+", text.lower()))
    return sorted(t for t in TECH_KEYWORDS if t in tokens)


def local_analysis(resume_text: str) -> dict:
    technologies = extract_technologies(resume_text)
    words = re.findall(r"\w+", resume_text)
    word_count = len(words)

    strengths = []
    weaknesses = []
    suggestions = []

    if technologies:
        strengths.append("Mentions relevant technologies.")
    else:
        weaknesses.append("No clear technologies identified.")
        suggestions.append("Add a dedicated technical skills section.")

    if word_count >= 180:
        strengths.append("Resume has reasonable detail.")
    else:
        weaknesses.append("Resume may be too short.")
        suggestions.append("Add measurable achievements and project impact.")

    if "project" in resume_text.lower():
        strengths.append("Includes project experience.")
    else:
        weaknesses.append("Project experience is not explicit.")
        suggestions.append("Include 2-3 projects with outcomes and technologies used.")

    if not suggestions:
        suggestions.append("Tailor your resume for each role and quantify impact with metrics.")

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "technologies": technologies,
        "suggestions": suggestions,
    }


def openai_analysis(resume_text: str, model: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": "You are an expert technical recruiter."},
            {
                "role": "user",
                "content": (
                    "Analyze this resume and return: strengths, weaknesses, detected technologies, "
                    f"and improvement suggestions.\n\nResume:\n{resume_text}"
                ),
            },
        ],
    )
    return response.output_text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a resume with local heuristics or OpenAI.")
    parser.add_argument("--text", required=True, help="Resume text")
    parser.add_argument("--mode", choices=["local", "openai"], default="local")
    parser.add_argument("--model", default="gpt-4.1-mini")
    args = parser.parse_args()

    if args.mode == "local":
        result = local_analysis(args.text)
        print("Resume Analysis")
        for key, values in result.items():
            print(f"\n{key.capitalize()}:")
            if values:
                for item in values:
                    print(f"- {item}")
            else:
                print("- None")
    else:
        print(openai_analysis(args.text, args.model))


if __name__ == "__main__":
    main()

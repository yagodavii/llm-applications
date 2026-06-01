# AI Resume Analyzer

Analyzes a resume and returns strengths, weaknesses, technologies, and improvement suggestions.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --mode local --text "<paste resume text>"
```

OpenAI mode:

```bash
set OPENAI_API_KEY=your_key_here
python main.py --mode openai --model gpt-4.1-mini --text "<paste resume text>"
```

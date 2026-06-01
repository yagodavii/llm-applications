# AI Document Assistant

Ask questions about a document or long text.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --mode local --document "<document text>" --question "What is the deadline?"
```

OpenAI mode:

```bash
set OPENAI_API_KEY=your_key_here
python main.py --mode openai --model gpt-4.1-mini --document "..." --question "..."
```

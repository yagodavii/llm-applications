# AI Code Reviewer

Receives a code snippet and returns possible bugs and improvements.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --mode local --code "try:\n    run()\nexcept:\n    pass"
```

OpenAI mode:

```bash
set OPENAI_API_KEY=your_key_here
python main.py --mode openai --model gpt-4.1-mini --code "<your code>"
```

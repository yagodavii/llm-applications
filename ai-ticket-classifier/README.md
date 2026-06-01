# AI Ticket Classifier

Classifies support tickets by category, priority, and sentiment.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --mode local --text "I cannot log in and this is urgent"
```

OpenAI mode:

```bash
set OPENAI_API_KEY=your_key_here
python main.py --mode openai --model gpt-4.1-mini --text "..."
```

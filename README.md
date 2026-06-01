# LLM Applications

A curated collection of practical LLM applications built with Python.

This repository was designed to showcase applied AI skills for international software and AI engineering opportunities, focused on real business use cases.

## Repository Structure

```text
llm-applications/
+-- ai-resume-analyzer/
¦   +-- main.py
¦   +-- requirements.txt
¦   +-- README.md
+-- ai-ticket-classifier/
¦   +-- main.py
¦   +-- requirements.txt
¦   +-- README.md
+-- ai-document-assistant/
¦   +-- main.py
¦   +-- requirements.txt
¦   +-- README.md
+-- ai-code-reviewer/
¦   +-- main.py
¦   +-- requirements.txt
¦   +-- README.md
+-- prompt-engineering-lab/
¦   +-- README.md
+-- README.md
```

## Projects Overview

### 1) ai-resume-analyzer
Analyzes resume content and returns strengths, weaknesses, detected technologies, and improvement suggestions.

### 2) ai-ticket-classifier
Classifies support tickets by category, priority, and sentiment for faster triage workflows.

### 3) ai-document-assistant
Answers questions about a provided document or text, using local logic or LLM-based reasoning.

### 4) ai-code-reviewer
Reviews code snippets and highlights potential bugs, maintainability risks, and concrete improvements.

### 5) prompt-engineering-lab
A reusable prompt library for summarization, classification, analysis, generation, and automation scenarios.

## Quick Start

1. Enter a project folder.
2. Install dependencies.
3. Run `main.py` with the options from that folder's `README.md`.

Example:

```bash
cd ai-ticket-classifier
pip install -r requirements.txt
python main.py --mode local --text "I cannot access my account and this is urgent."
```

## Tech Stack

- Python
- OpenAI API integration
- Prompt engineering
- LLM workflow design
- Text analysis and classification

## Portfolio Goal

Demonstrate hands-on LLM engineering skills with runnable examples that solve realistic operational and product problems.

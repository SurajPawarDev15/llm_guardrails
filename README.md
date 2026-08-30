```

```

# LLM Guardrails Project

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/SurajPawarDev15/llm_guardrails)

A FastAPI-based demo application that shows how to build a secure AI workflow using input guardrails, Gemini model integration, and output validation.

## GitHub Repository

https://github.com/SurajPawarDev15/llm_guardrails

## Overview

This project demonstrates a simple but practical security pipeline for LLM applications:

1. User sends a prompt.
2. The input is checked for unsafe content.
3. A Gemini model generates a response if the prompt is allowed.
4. The model output is checked before it is shown to the user.

This project is designed for educational and workshop use to explain responsible AI and enterprise AI security principles.

## Features

- FastAPI backend
- Frontend web UI with a cyber-security dashboard style
- Input prompt filtering for blocked keywords and prompt injection patterns
- Output validation to flag sensitive content
- Gemini API integration
- Security demonstration pipeline

## Project Structure

```text
llm_guardrails/
├── app.py
├── config.py
├── gemini_service.py
├── guardrails.py
├── output_guardrails.py
├── requirements.txt
├── .env
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

## Requirements

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root with your Gemini configuration:

```env
GEMINI_API_KEY=your_google_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash
```

Important:

- Use a valid Google Gemini model name for the Google GenAI SDK.
- Example valid values: `gemini-2.0-flash`, `gemini-1.5-flash`
- Do not use Ollama-style names like `gemma3:270m` with the Google SDK.

## Running the App

From the project root, run:

```bash
uvicorn app:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001
```

## Security Pipeline

The application follows this flow:

```text
User Prompt
   ↓
Input Guardrail
   ↓
Gemini Model
   ↓
Output Guardrail
   ↓
User Response
```

## Guardrail Rules

### Input Guardrail

Blocks prompts containing:

- blocked dangerous keywords
- prompt injection phrases
- jailbreak attempts
- restricted instructions

### Output Guardrail

Blocks responses containing suspicious or sensitive patterns such as:

- API keys
- passwords
- secret keys

## Example Use Cases

- AI security workshop demo
- Secure LLM prompt testing
- Demonstrating prompt injection defense
- Output sanitization example

## Notes

This is a demonstration project and is intended for learning and security awareness. It should not be used as a full production-grade AI security system without additional review, validation, and deployment hardening.

## License

This project is for educational use. Thank you...!!!

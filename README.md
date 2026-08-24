# Local LLM Chatbot

A small project built to explore **running and interacting with a local LLM** using [Ollama](https://ollama.com/), the **OpenAI Python SDK**, and **Gradio**.

The project was created as a hands-on exercise to understand how local language models can be connected to a Python application and used to build a simple conversational interface.

## Features

- Run an LLM locally with Ollama
- Connect to Ollama through its OpenAI-compatible API
- Maintain conversation history
- Stream model responses
- Interact with the model through a simple Gradio interface

## Project Structure

```text
📁
├── 📁 codes
│   └── 🐍 chat.py      # CLI-based Chat-bot
├── 🐍 app.py           # Gradio web interface
├── ⚖️ LICENSE
└── 📘 README.md
```

## Requirements

- Python 3.10+
- Ollama
- A compatible local language model
- `openai`
- `gradio`

Install the Python dependencies with:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install openai gradio
```

Make sure Ollama is installed and running, and that the desired model is available locally. For example:

```bash
ollama pull llama3.1
```

By default, Ollama exposes its OpenAI-compatible API at `http://localhost:11434/v1`. If your Ollama instance runs elsewhere, update the base URL in `app.py` / `chat.py` accordingly.

## Running the App

Start the Gradio web interface with:

```bash
python app.py
```

The application will launch a local web interface where you can interact with the model.

Alternatively, run the CLI-based chatbot:

```bash
python codes/chat.py
```

## Purpose

This is a small learning project rather than a production-ready chatbot. The main goal was to get hands-on experience with local LLMs, Ollama, API-based model interaction, response streaming, conversation history, and Gradio.

Sometimes the best way to get comfortable with a new technology is simply to build something small with it.

## License

[MIT](./LICENSE)
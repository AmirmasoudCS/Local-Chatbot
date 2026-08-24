import os
import gradio as gr
from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    timeout=60.0,
)

MODEL = os.environ.get("GEMMA_MODEL", "gemma4:e4b")


def normalize_history(history):
    messages = []

    for turn in history or []:

        if isinstance(turn, dict):
            messages.append({
                "role": turn["role"],
                "content": turn["content"],
            })

        elif isinstance(turn, (list, tuple)) and len(turn) == 2:
            user_msg, bot_msg = turn

            if user_msg:
                messages.append({
                    "role": "user",
                    "content": user_msg,
                })

            if bot_msg:
                messages.append({
                    "role": "assistant",
                    "content": bot_msg,
                })

    return messages


def chat(message, history):

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        }
    ]

    messages += normalize_history(history)

    messages.append({
        "role": "user",
        "content": message,
    })

    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )

    reply = ""

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            reply += content
            yield reply


def build_demo():

    css = """
    .gradio-container {
        height: 100vh !important;
    }
    """

    with gr.Blocks(fill_height=True) as demo:

        gr.ChatInterface(
            fn=chat,
            title="Local Gemma 4 Model",
            description="Powered entirely by Gemma 4 running locally on the machine.",
        )

    return demo, css


if __name__ == "__main__":

    demo, css = build_demo()

    demo.launch(css=css)
import os
import gradio as gr
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama", timeout=60.0)
MODEL = os.environ.get("GEMMA_MODEL", "gemma4:e4b")

def normalize_history(history):

    messages = []
    for turn in history or []:
        if isinstance(turn, dict):
            messages.append({"role": turn["role"], "content": turn["content"]})
        elif isinstance(turn, (list, tuple)) and len(turn) == 2:
            user_msg, bot_msg = turn
            if user_msg:
                messages.append({"role":"user", "content":user_msg})
            if bot_msg:
                messages.append({"role":"assistant", "content":bot_msg})
    return messages
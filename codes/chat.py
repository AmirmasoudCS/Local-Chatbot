import os
from openai import OpenAI

STREAM = True

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

MODEL = os.environ.get("GEMMA_MODEL", "gemma4:e4b")

messages = [
    {
        "role": "system",
        "content": "You are a helpful, friendly assistant."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ("quit", "exit"):
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        stream = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=STREAM,
        )

        print("Gemma: ", end="", flush=True)

        reply = ""

        for chunk in stream:
            content = chunk.choices[0].delta.content

            if content:
                print(content, end="", flush=True)
                reply += content

        print("\n")

        messages.append({
            "role": "assistant",
            "content": reply
        })
    except Exception as e:
        print(f"\n[Error talking to Gemma: {e}]")
        print("Is Ollama running? Try 'ollama serve' or chck the model name.\n")
        messages.pop()
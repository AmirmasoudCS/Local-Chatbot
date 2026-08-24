import os
from openai import OpenAI

STREAM = True

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

question = input("Ask local Gemma: ")

response = client.chat.completions.create(
    model=os.environ.get("GEMMA_MODEL", "gemma4:e4b"),
    messages=[{"role": "user", "content": question}],
    stream=STREAM,
)

if STREAM:
    for chunk in response:
        content = chunk.choices[0].delta.content

        if content:
            print(content, end="", flush=True)

    print()  # newline after streaming finishes

else:
    print(response.choices[0].message.content)
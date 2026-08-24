import os
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1143/v1",
    api_key="ollama",
)

question = input("Ask local Gemma: ")

response = client.chat.completions.create(
    model=os.environ.get("GEMMA_MODEL", "gemma4"),
    messages=[{"role":"user", "content":"question"}],
)

print(response.choices[0].message.content)
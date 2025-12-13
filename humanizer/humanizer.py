import re
from datetime import datetime

from ollama import Client

model = "qwen3:14b"
print(f"Using model {model}, loading...")
client = Client(
    host="http://localhost:11434"
)

print("Reading system prompt...")
with open("prompts/prompt_v2.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()
user_prompt = """
Paragraph: {}
Sentence: {}
"""

print("Reading essay...")
with open("essay_to_humanize.txt", "r", encoding="utf-8") as f:
    essay = f.read()

hum_essay = ""
paragraphs = [l.strip() for l in essay.split("\n") if l]
for i, p in enumerate(paragraphs, start=1):
    print(f"\r[{datetime.now().strftime("%H:%M:%S")}] Processing paragraph: {i} / {len(paragraphs)}", end="")
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', p) if s]
    for s in sentences:
        response = client.chat(model=model, messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt.format(p, s),
            }
        ])
        hum_sentence = response.message.content.strip()
        hum_essay += hum_sentence
    hum_essay += "\n"

with open("humanized_essay.txt", "w", encoding="utf-8") as f:
    f.write(hum_essay)

import re
from datetime import datetime

from ollama import Client

model = "qwen3:14b"
print(f"Using model {model}, loading...")
client = Client(
    host="http://localhost:11434"
)

print("Reading essay...")
with open("essay_to_humanize.txt", "r", encoding="utf-8") as f:
    essay = f.read()

print("Reading system prompt for translation...")
with open("prompts/prompt_v3_translate.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

print("Translating essay...")
response = client.chat(model=model, messages=[
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "user",
        "content": essay,
    }
])
chinese_essay = response.message.content.strip()

print("Reading system prompt for rewriting...")
with open("prompts/prompt_v3_rewrite.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()
user_prompt = """
Paragraph: {}
Sentence: {}
"""

hum_essay = ""
paragraphs = [l.strip() for l in chinese_essay.split("\n") if l]
paragraph_len = len(paragraphs)
for i, p in enumerate(paragraphs, start=1):
    sentences = [s.strip() for s in re.split(r'(?<=[。！？])', p) if s]
    sentence_len = len(sentences)
    for j, s in enumerate(sentences, start=1):
        print(f"\r[{datetime.now().strftime("%H:%M:%S")}] Processing paragraph: [{i}/{paragraph_len}] Translating: [{j}/{sentence_len}]", end="")
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
        hum_sentence = response.message.content.strip() + " "
        hum_essay += hum_sentence
    hum_essay += "\n"

with open("humanized_essay.txt", "w", encoding="utf-8") as f:
    f.write(hum_essay)

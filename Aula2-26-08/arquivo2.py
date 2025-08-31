import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "melhor time do brasil",
        }
    ],
    model="openai/gpt-oss-20b",
    stream=False,
)

print(chat_completion.choices[0].message.content)
from openai import OpenAI

client = OpenAI()
  

response = client.responses.create(
  model="gpt-4o-mini",
  input="Quem é o melhor time de 2025?",
  store=True,
)

print(response.output_text)
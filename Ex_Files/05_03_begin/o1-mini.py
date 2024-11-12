import os
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

console = Console()


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
model = "o1-mini"

response = client.chat.completions.create(
  model=model,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is the o complexity of a binary search."
        }
      ]
    },
  ]
)

md = Markdown(response.choices[0].message.content)
console.print(md)

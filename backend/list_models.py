from openai import OpenAI
from app import config

client = OpenAI(api_key=config.LLM_API_KEY, base_url=config.LLM_BASE_URL)
for m in client.models.list().data:
    print(m.id)
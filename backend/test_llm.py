import asyncio
from openai import AsyncOpenAI
from app import config

client = AsyncOpenAI(api_key=config.LLM_API_KEY, base_url=config.LLM_BASE_URL)

async def main():
    resp = await client.chat.completions.create(
        model=config.LLM_MODEL,
        messages=[{"role": "user", "content": "Explain a deadlock in one sentence."}],
        max_tokens=200,
    )
    print(resp.choices[0].message.content)
    print(resp.usage)

asyncio.run(main())
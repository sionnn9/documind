from openai import AsyncOpenAI
from app import config

client = AsyncOpenAI(
    api_key=config.LLM_API_KEY,
    base_url=config.LLM_BASE_URL,
    timeout=60,
)

async def complete(messages, **kwargs):
    return await client.chat.completions.create(
        model=config.LLM_MODEL, messages=messages, **kwargs
    )

async def stream_chat(messages, **kwargs):
    stream = await client.chat.completions.create(
        model=config.LLM_MODEL, messages=messages, stream=True, **kwargs
    )
    async for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
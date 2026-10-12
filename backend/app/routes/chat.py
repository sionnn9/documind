import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from openai import APIError

from app.llm import stream_chat
from app.schemas import ChatRequest

router = APIRouter()

SYSTEM_PROMPT = "You are DocuMind, a helpful study assistant. Be clear and concise."

@router.post("/chat")
async def chat(req: ChatRequest):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += [m.model_dump() for m in req.messages]

    async def event_stream():
        try:
            async for token in stream_chat(messages, max_tokens=1500):
                yield f"data: {json.dumps({'token': token})}\n\n"
            yield "data: [DONE]\n\n"
        except APIError as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
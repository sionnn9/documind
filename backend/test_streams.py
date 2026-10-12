import json
import httpx

body = {"messages": [{"role": "user", "content": "Explain a deadlock in 3 sentences."}]}

with httpx.stream("POST", "http://127.0.0.1:8000/chat", json=body, timeout=60) as r:
    for line in r.iter_lines():
        if not line.startswith("data: "):
            continue
        data = line[6:]
        if data == "[DONE]":
            break
        event = json.loads(data)
        if "error" in event:
            print("\nERROR:", event["error"])
            break
        print(event["token"], end="", flush=True)
print()
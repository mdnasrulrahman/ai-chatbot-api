# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import anthropic, os

app = FastAPI()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
history = []  # simple memory (production mein database use karo)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    history.append({"role": "user", "content": req.message})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=history,
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return {"reply": reply}
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
from llama_cpp import Llama
import json

app = FastAPI()

llm = Llama(
    model_path="/home/dmin/models/chronos-hermes-13b-v2.Q5_0.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,
    seed=0,
    verbose=False,
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 512
    stream: Optional[bool] = False


@app.post("/v1/chat/completions")
def chat_completions(req: ChatRequest):

    # Build prompt
    prompt = ""
    for m in req.messages:
        prompt += f"{m.role}: {m.content}\n"
    prompt += "assistant:"

    # If not streaming, return a normal JSON response
    if not req.stream:
        output = llm(
            prompt,
            max_tokens=req.max_tokens,
            temperature=req.temperature,
            stop=["user:", "assistant:"],
        )
        text = output["choices"][0]["text"]

        return {
            "id": "chatcmpl-local",
            "object": "chat.completion",
            "model": req.model,
            "choices": [
                {
                    "index": 0,
                    "finish_reason": "stop",
                    "message": {"role": "assistant", "content": text},
                }
            ],
            "usage": {
                "prompt_tokens": output.get("prompt_tokens", 0),
                "completion_tokens": output.get("completion_tokens", 0),
                "total_tokens": output.get("prompt_tokens", 0)
                + output.get("completion_tokens", 0),
            },
        }

    # STREAMING MODE
    def stream_generator():
        for chunk in llm(
            prompt,
            max_tokens=req.max_tokens,
            temperature=req.temperature,
            stop=["user:", "assistant:"],
            stream=True,
        ):
            token = chunk["choices"][0]["text"]
            if token:
                data = {
                    "id": "chatcmpl-local",
                    "object": "chat.completion.chunk",
                    "model": req.model,
                    "choices": [
                        {"index": 0, "delta": {"content": token}}
                    ],
                }
                yield f"data: {json.dumps(data)}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional, Any
from llama_cpp import Llama
import os
import json
import time
import sys

app = FastAPI(title="AITextAdventure AI Server")

# ── Model Configuration (aligned with story_suggestion_server.py + your log) ──
MODEL_PATH = os.getenv(
    "MODEL_PATH", 
    "/home/dmin/models/Qwen2.5-14B_Uncensored_Instruct-Q5_K_M.gguf"
)
MODEL_CTX = int(os.getenv("MODEL_CTX", "32768"))

print(f"[INIT] MODEL_PATH={MODEL_PATH}", file=sys.stderr)
print(f"[INIT] MODEL_CTX={MODEL_CTX}", file=sys.stderr)

llm = None

def get_llm():
    global llm
    if llm is None:
        print(f"[MODEL] Loading model from {MODEL_PATH}...", file=sys.stderr)
        try:
            llm = Llama(
                model_path=MODEL_PATH,
                n_ctx=MODEL_CTX,
                n_gpu_layers=-1,      # Offload as much as possible to GPU
                seed=0,
                verbose=True,         # Matches your log for detailed output
            )
            print("[MODEL] Model loaded successfully", file=sys.stderr)
        except Exception as e:
            print(f"[MODEL ERROR] {type(e).__name__}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            raise
    return llm


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1024
    stream: Optional[bool] = False
    # VS Code / tool-calling compatibility
    tools: Optional[Any] = None
    tool_choice: Optional[Any] = None
    functions: Optional[Any] = None
    function_call: Optional[Any] = None


# ── Model listing for VS Code ──
@app.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "qwen2.5-14b-uncensored",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "local",
            }
        ],
    }


@app.post("/v1/chat/completions")
def chat_completions(req: ChatRequest):
    llm_instance = get_llm()

    if not req.stream:
        # Non-streaming
        output = llm_instance.create_chat_completion(
            messages=[m.dict() for m in req.messages],
            max_tokens=req.max_tokens,
            temperature=req.temperature,
            # Tool support (if VS Code sends them)
            tools=req.tools,
            tool_choice=req.tool_choice,
        )

        return {
            "id": "chatcmpl-local",
            "object": "chat.completion",
            "model": req.model,
            "choices": [
                {
                    "index": 0,
                    "finish_reason": output["choices"][0].get("finish_reason", "stop"),
                    "message": output["choices"][0]["message"],
                }
            ],
            "usage": output.get("usage", {}),
        }

    # Streaming
    def stream_generator():
        stream = llm_instance.create_chat_completion(
            messages=[m.dict() for m in req.messages],
            max_tokens=req.max_tokens,
            temperature=req.temperature,
            tools=req.tools,
            tool_choice=req.tool_choice,
            stream=True,
        )
        for chunk in stream:
            if "choices" in chunk and chunk["choices"]:
                delta = chunk["choices"][0].get("delta", {})
                if delta:
                    data = {
                        "id": "chatcmpl-local",
                        "object": "chat.completion.chunk",
                        "model": req.model,
                        "choices": [{"index": 0, "delta": delta}],
                    }
                    yield f"data: {json.dumps(data)}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")
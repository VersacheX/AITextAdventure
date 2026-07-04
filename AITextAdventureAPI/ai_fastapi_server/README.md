### This readme is for story_suggestion_server.py and story_suggestion_cli.py

### to run the server:
(base) dmin@DESKTOP-3K6IPDC:/mnt/d/dev/source/repos/AITextAdventure$ cd aitextadventureapi
(base) dmin@DESKTOP-3K6IPDC:/mnt/d/dev/source/repos/AITextAdventure/aitextadventureapi$ source .venv_wsl/bin/activate
(.venv_wsl) (base) dmin@DESKTOP-3K6IPDC:/mnt/d/dev/source/repos/AITextAdventure/aitextadventureapi$ cd ai_fastapi_server
(.venv_wsl) (base) dmin@DESKTOP-3K6IPDC:/mnt/d/dev/source/repos/AITextAdventure/aitextadventureapi/ai_fastapi_server$ uvicorn story_suggestion_server:app --host 0.0.0.0 --port 8000

### Running the CLI client:
(.venv_wsl) (base) dmin@DESKTOP-3K6IPDC:/mnt/d/dev/source/repos/AITextAdventure/aitextadventureapi/ai_fastapi_server$ python story_suggestion_cli.py --act "ACT I" --chapter 1 --task "TASK_NAME" --prompt "Make this dialogue more suspenseful." --temperature 0.8 --max-tokens 512

### Parameters:
- `--act`: The act name to analyze (e.g., "ACT I", "ACT II").
- `--chapter`: The chapter number(s) to analyze (can be specified multiple times).
- `--task`: The specific task name(s) to analyze (can be specified multiple times).
- `--prompt`: Custom instruction for the model (e.g., "Make this dialogue more suspenseful.").
- `--temperature`: Sampling temperature for the model (default: 0.7).
- `--max-tokens`: Maximum number of tokens to generate (default: 512).
- `--no-stream`: Disable streaming output (default: streaming is enabled).
- `--server`: Specify the server URL (default: http://127.0.0.1:8000).

### Server response format:
- If streaming is enabled, the server will send Server-Sent Events (SSE) with chunks of generated suggestions.
- If streaming is disabled, the server will return a JSON response containing the suggestions.
'''
- json response format:
{
  "suggestions": [
    {
      "task": "TASK_NAME",
      "original": "Original dialogue line.",
      "suggestion": "Improved/Replaced dialogue line.",
      "why": "Explanation of changes based on character psychology."
    },
    ...
  ]
}
'''

### Future features:
- Add more sophisticated parsing of NPC files to extract detailed character profiles.
- Allow for full custom prompting to forgo character and act/chapter/task lookup. i.e. add endpoint for direct prompting

### Referenced files:
\AITextAdventureAPI\ai_fastapi_server\story_suggestion_cli.py
\AITextAdventureAPI\ai_fastapi_server\story_suggestion_server.py

############################### story_suggestion_server.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict
from llama_cpp import Llama
import os
import json
import glob
import traceback
import sys
import re

app = FastAPI(title="Story Suggestion Server (Cached)")

"""
alternate installed models
chronos-hermes-13b-v2.Q5_0.gguf
"""

MODEL_PATH = os.getenv("HERMES_MODEL_PATH", "/home/dmin/models/Qwen2.5-14B_Uncensored_Instruct-Q5_K_M.gguf")
MODEL_CTX = int(os.getenv("HERMES_CTX", "32768"))
WORKSPACE_ROOT = os.getenv("WORKSPACE_ROOT", r"/mnt/d/dev/source/repos/AITextAdventure")

print(f"[INIT] MODEL_PATH={MODEL_PATH}", file=sys.stderr)
print(f"[INIT] WORKSPACE_ROOT={WORKSPACE_ROOT}", file=sys.stderr)

llm = None
TIMELINE_CACHE = {}  # {act_name: {chapter_num: {task_name: task_content}}}
NPC_CACHE = {}       # {npc_id: npc_data_dict}

def get_llm():
    global llm
    if llm is None:
        print(f"[MODEL] Loading model from {MODEL_PATH}...", file=sys.stderr)
        try:
            llm = Llama(model_path=MODEL_PATH, n_ctx=MODEL_CTX, n_gpu_layers=-1, seed=0, verbose=True)
            print("[MODEL] Model loaded successfully", file=sys.stderr)
        except Exception as e:
            print(f"[MODEL ERROR] {type(e).__name__}: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            raise
    return llm

class SuggestRequest(BaseModel):
    act: Optional[str] = "ACT I"
    chapters: Optional[List[int]] = None
    tasks: Optional[List[str]] = None
    custom_prompt: Optional[str] = None  # NEW: user's custom instruction
    temperature: Optional[float] = 0.9
    max_tokens: Optional[int] = 4096
    stream: Optional[bool] = True

def safe_resolve(path: str) -> str:
    try:
        if os.path.isabs(path):
            resolved = os.path.normpath(path)
        else:
            resolved = os.path.normpath(os.path.join(WORKSPACE_ROOT, path))
        workspace_norm = os.path.normpath(WORKSPACE_ROOT)
        if not os.path.commonprefix([resolved.lower(), workspace_norm.lower()]) == workspace_norm.lower():
            raise FileNotFoundError(f"Path outside workspace: {resolved}")
        if not os.path.exists(resolved):
            raise FileNotFoundError(resolved)
        return resolved
    except Exception as e:
        print(f"[PATH ERROR] Failed to resolve {path}: {e}", file=sys.stderr)
        raise

def parse_timeline_to_dict(timeline_text: str) -> Dict[int, Dict[str, str]]:
    """
    Parse timeline .mmd into {chapter_num: {task_name: task_content}}
    """
    result = {}
    chapter_pattern = r'section Chapter (\d+)[^\n]*'
    task_pattern = r'TASK - ([^:]+)\s*:'
    
    chapter_splits = re.split(chapter_pattern, timeline_text)
    
    for i in range(1, len(chapter_splits), 2):
        if i+1 >= len(chapter_splits):
            break
        chapter_num = int(chapter_splits[i])
        chapter_body = chapter_splits[i+1]
        
        task_splits = re.split(task_pattern, chapter_body)
        tasks = {}
        for j in range(1, len(task_splits), 2):
            if j+1 >= len(task_splits):
                break
            task_name = task_splits[j].strip()
            task_content = task_splits[j+1].strip()
            tasks[task_name] = task_content
        
        result[chapter_num] = tasks
    
    return result

def parse_npc_file(npc_text: str) -> Dict[str, dict]:
    """
    Parse NPC file into {npc_id: {...npc_data...}}
    Assumes Python dict format with 'npc_id' keys
    """
    npcs = {}
    # Simple regex to extract dicts with npc_id
    npc_pattern = r"\{\s*['\"]npc_id['\"]\s*:\s*['\"]([^'\"]+)['\"][^}]*\}"
    
    for match in re.finditer(npc_pattern, npc_text, re.DOTALL):
        npc_id = match.group(1)
        npc_block = match.group(0)
        npcs[npc_id] = npc_block  # Store the raw dict string for now
    
    return npcs

def extract_npc_names(text: str) -> set:
    """
    Extract NPC names/IDs mentioned in dialogue/events.
    """
    names = set()
    # Pattern 1: "Name - dialogue"
    dialogue_pattern = r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+-\s+'
    names.update(re.findall(dialogue_pattern, text))
    
    # Pattern 2: npc_id in events
    npc_id_pattern = r'(?:create_npc|show_npc|hide_npc|set_npc_standing_text)\s+-\s+([a-z_]+)'
    names.update(re.findall(npc_id_pattern, text))
    
    return names

def filter_npcs_from_cache(mentioned_names: set) -> str:
    """
    Filter NPCs from cache to only include those mentioned.
    """
    filtered = []
    for npc_id, npc_block in NPC_CACHE.items():
        # Check if npc_id or any variant matches mentioned names
        if any(name.lower().replace(' ', '_') == npc_id or name.lower() in npc_block.lower() for name in mentioned_names):
            filtered.append(npc_block)
    
    if not filtered:
        # Fallback: return first 10 NPCs
        filtered = list(NPC_CACHE.values())[:10]
    
    result = "NPCS = [\n" + ",\n".join(filtered) + "\n]"
    print(f"[NPC FILTER] Kept {len(filtered)} NPCs from {len(mentioned_names)} detected names", file=sys.stderr)
    return result

def load_timeline_cache():
    """
    Load all timeline files on startup
    """
    global TIMELINE_CACHE
    pattern = os.path.join(WORKSPACE_ROOT, "AITextAdventureAPI", "old", "STORY DOCUMENTS FOR AI", "TIMELINE ACT *.mmd")
    files = sorted(glob.glob(pattern))
    
    for filepath in files:
        # Extract act name from filename (e.g. "TIMELINE ACT I.mmd" -> "ACT I")
        filename = os.path.basename(filepath)
        act_match = re.search(r'ACT\s+[IVX]+', filename)
        if not act_match:
            continue
        act_name = act_match.group(0)
        
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            timeline_text = f.read()
        
        TIMELINE_CACHE[act_name] = parse_timeline_to_dict(timeline_text)
        print(f"[CACHE] Loaded {act_name}: {len(TIMELINE_CACHE[act_name])} chapters", file=sys.stderr)

def load_npc_cache():
    """
    Load NPC file on startup
    """
    global NPC_CACHE
    npc_path = os.path.join(WORKSPACE_ROOT, "AITextAdventureAPI", "old", "STORY DOCUMENTS FOR AI", "NPCS FULL LIST.txt")
    
    with open(npc_path, 'r', encoding='utf-8', errors='replace') as f:
        npc_text = f.read()
    
    NPC_CACHE = parse_npc_file(npc_text)
    print(f"[CACHE] Loaded {len(NPC_CACHE)} NPCs", file=sys.stderr)

@app.on_event("startup")
def startup_event():
    print("[STARTUP] Loading timeline and NPC caches...", file=sys.stderr)
    load_timeline_cache()
    load_npc_cache()
    print(f"[STARTUP] Cache ready: {len(TIMELINE_CACHE)} acts, {len(NPC_CACHE)} NPCs", file=sys.stderr)

def build_prompt(npcs_text: str, timeline_snippet: str, custom_instruction: Optional[str] = None) -> Dict[str, str]:
    system_message = (
        "You are a professional story editor specializing in character voice analysis. "
        "You review game dialogue and suggest improvements based on deep character psychology."
    )
    
    # Default analysis focus
    default_focus = (
        "Review the timeline dialogue below. Identify any lines that feel:\n"
        "- Generic or cliche\n"
        "- Inconsistent with the character's MBTI/Enneagram profile\n"
        "- Flat or lacking emotional depth\n\n"
    )
    
    # Use custom prompt if provided, otherwise use default
    if custom_instruction:
        analysis_instruction = f"CUSTOM REQUEST: {custom_instruction}\n\n"
    else:
        analysis_instruction = default_focus
    
    user_message = (
        f"{analysis_instruction}"
        "Return ONLY a JSON array. Each suggestion must include:\n"
        "- task: exact task name from the timeline\n"
        "- original: the problematic dialogue line\n"
        "- suggestion: your improved version\n"
        "- why: explanation referencing the character's personality traits and your changes\n\n"
        "---\n\n"
        f"CHARACTER PROFILES:\n{npcs_text}\n\n"
        "---\n\n"
        f"TIMELINE DIALOGUE TO ANALYZE:\n{timeline_snippet}\n\n"
        "---\n\n"
        "Analyze the timeline above and return your suggestions as a JSON array:"
    )
    
    return {
        "system": system_message,
        "user": user_message
    }

@app.get("/v1/config")
def info():
    return {
        "workspace_root": WORKSPACE_ROOT,
        "model_path": MODEL_PATH,
        "model_ctx": MODEL_CTX,
        "cached_acts": list(TIMELINE_CACHE.keys()),
        "cached_npcs": len(NPC_CACHE)
    }

@app.post("/v1/story/suggestions")
def story_suggestions(req: SuggestRequest):
    try:
        print(f"[REQUEST] Act={req.act}, Chapters={req.chapters}, Tasks={req.tasks}", file=sys.stderr)
        
        # Lookup act
        if req.act not in TIMELINE_CACHE:
            raise HTTPException(status_code=400, detail=f"Act '{req.act}' not found. Available: {list(TIMELINE_CACHE.keys())}")
        
        act_data = TIMELINE_CACHE[req.act]
        
        # Extract requested chapters/tasks
        if not req.chapters:
            req.chapters = [1]  # default to chapter 1
        
        timeline_snippet = ""
        for chapter in req.chapters:
            if chapter not in act_data:
                continue
            tasks = act_data[chapter]
            if req.tasks:
                tasks = {k: v for k, v in tasks.items() if k in req.tasks}
            timeline_snippet += f"\n\n=== {req.act} - CHAPTER {chapter} ===\n"
            for task_name, task_content in tasks.items():
                timeline_snippet += f"\nTASK: {task_name}\n{task_content}\n"
        
        if not timeline_snippet:
            raise HTTPException(status_code=400, detail="No matching chapters/tasks found.")
        
        # Filter NPCs
        mentioned_names = extract_npc_names(timeline_snippet)
        npc_text = filter_npcs_from_cache(mentioned_names)
        
        # Build messages for chat format
        messages_dict = build_prompt(npc_text, timeline_snippet, req.custom_prompt)
        
        # print(f"[PROMPT] {messages_dict}", file=sys.stderr)
        # input()

        if not req.stream:
            # Use chat completion format
            output = get_llm().create_chat_completion(
                messages=[
                    {"role": "system", "content": messages_dict["system"]},
                    {"role": "user", "content": messages_dict["user"]}
                ],
                max_tokens=req.max_tokens,
                temperature=req.temperature,
                response_format={"type": "json_object"}  # Force JSON output
            )
            text = output["choices"][0]["message"]["content"]
            try:
                parsed = json.loads(text)
                return JSONResponse(content={"suggestions": parsed})
            except Exception:
                return JSONResponse(content={"raw": text})

        def gen():
            stream = get_llm().create_chat_completion(
                messages=[
                    {"role": "system", "content": messages_dict["system"]},
                    {"role": "user", "content": messages_dict["user"]}
                ],
                max_tokens=req.max_tokens,
                temperature=req.temperature,
                stream=True
            )
            for chunk in stream:
                delta = chunk["choices"][0]["delta"]
                if "content" in delta:
                    token = delta["content"]
                    if token:
                        data = {"chunk": token}
                        yield f"data: {json.dumps(data)}\n\n"
            yield "data: [DONE]\n\n"

        return StreamingResponse(gen(), media_type="text/event-stream")
        
    except Exception as e:
        print(f"[ENDPOINT ERROR] {type(e).__name__}: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise HTTPException(status_code=500, detail=str(e))
#################################################################


### story_suggestion_cli

#!/usr/bin/env python3
"""
CLI client to call the story suggestion endpoint.
Adjust default file paths to match your repo if necessary.
"""
import argparse
import requests
import sys
import json

DEFAULT_SERVER = "http://127.0.0.1:8000"

def stream_sse(resp):
    # simple SSE stream reader
    try:
        for line in resp.iter_lines(decode_unicode=True):
            if line:
                if line.startswith("data: "):
                    payload = line[len("data: "):]
                    if payload.strip() == "[DONE]":
                        print("\n[STREAM DONE]")
                        break
                    try:
                        obj = json.loads(payload)
                        chunk = obj.get("chunk", "")
                        print(chunk, end="", flush=True)
                    except Exception:
                        print(payload)
    except KeyboardInterrupt:
        print("\nAborted by user")

def main():
    parser = argparse.ArgumentParser(description="Story suggestion CLI (cached)")
    parser.add_argument("--server", default=DEFAULT_SERVER)
    parser.add_argument("--act", default="ACT I", help="Act name (e.g. 'ACT I', 'ACT II')")
    parser.add_argument("--chapter", action="append", type=int, help="Chapter number(s)", default=None)
    parser.add_argument("--task", action="append", help="Task name(s) to extract", default=None)
    parser.add_argument("--prompt", help="Custom instruction (e.g. 'Make this darker', 'Add more tension')")  # NEW
    parser.add_argument("--no-stream", dest="stream", action="store_false")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args()

    payload = {
        "act": args.act,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "stream": args.stream
    }
    if args.chapter:
        payload["chapters"] = args.chapter
    if args.task:
        payload["tasks"] = args.task
    if args.prompt:
        payload["custom_prompt"] = args.prompt  # NEW

    url = args.server.rstrip("/") + "/v1/story/suggestions"
    headers = {"Content-Type": "application/json"}
    
    if args.stream:
        try:
            with requests.post(url, json=payload, headers=headers, stream=True, timeout=(10, 600)) as resp:
                if resp.status_code != 200:
                    print("Server error:", resp.status_code, resp.text, file=sys.stderr)
                    sys.exit(1)
                stream_sse(resp)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=(10, 600))
            if resp.status_code != 200:
                print("Server error:", resp.status_code, resp.text, file=sys.stderr)
                sys.exit(1)
            print(json.dumps(resp.json(), indent=2))
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()

#############################################
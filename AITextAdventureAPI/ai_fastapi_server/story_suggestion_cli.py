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
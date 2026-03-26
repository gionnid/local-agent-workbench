import json
from pathlib import Path
import requests
from agent_workbench.config import Config


def load_transcript():
    with open(Path(__file__).parent / "transcript.txt") as f:
        return f.read()


PROMPTS = {
    "sysPrompt": None,
    "userPrompt": f"""You are an agent that makes synthetic summaries.

# Content
This summary is for the Eoliann Sales team to understand the customer needs and requirements: be very synthetic describing the contribution from Eoliann and focus on the customer side.

# Format: 
- You receive a json and produce few bullet points.
- You clearly include at the beginning of the bullet point the relevant people addressed, if possible.
- Be very synthetic, less than 2000 chars. Don't use markdown or symbols: just text, with CAPSLOCK to highlight and - for bullet points.
- Summarize in English whatever language you find in the transcript.

Transcript:
```
{load_transcript()}
```
""",
}


def main():
    chat()


def chat():
    body = {
        "model": Config.DEFAULT_MODEL,
        "prompt": PROMPTS["userPrompt"],
        # "system": "Synthetic answer, few words only.",
        "stream": False,
    }

    response = requests.post(f"{Config.OLLAMA_URI}/api/generate", json=body)
    print(response.json()["response"])


def api_tags():
    response = requests.get(f"{Config.OLLAMA_URI}/api/tags")
    print(json.dumps(response.json(), indent=2))

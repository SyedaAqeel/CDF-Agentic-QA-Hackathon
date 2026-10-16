from __future__ import annotations

import json
import os
from pathlib import Path
from google import genai
from google.genai import types

from .models import Requirement

_DEFAULT_REQUIREMENTS = Path(__file__).resolve().parent / "data" / "requirements.json"

# Global dictionary to track token usage without breaking the return signature
llm_usage = {"input_tokens": 0, "output_tokens": 0}

def load_requirements(prd_path: Path | None) -> list[Requirement]:
    """
    Load the checklist used for reporting. If a PRD path is provided,
    use Gemini to dynamically extract requirements instead of the bundled JSON.
    """
    global llm_usage
    
    if prd_path is not None:
        if not prd_path.is_file():
            raise FileNotFoundError(f"PRD not found: {prd_path}")
            
        # Read the raw PRD text
        prd_text = prd_path.read_text(encoding="utf-8")
        
        # Initialize Gemini using your environment variable
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        prompt = """
        You are an expert QA engineer. Read the following PRD and extract all verifiable requirements.
        Return ONLY a raw JSON array of objects. Each object must have three string keys: 'id', 'section', and 'text'.
        Do not wrap the response in markdown blocks.
        """
        
        # Generate the dynamic requirements
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"{prompt}\n\nPRD Document:\n{prd_text}",
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        
        # Track costs and parse the JSON payload
        llm_usage["input_tokens"] = response.usage_metadata.prompt_token_count
        llm_usage["output_tokens"] = response.usage_metadata.candidates_token_count
        
        raw = json.loads(response.text)
        
    else:
        # Fallback to the static JSON if no PRD is provided
        raw = json.loads(_DEFAULT_REQUIREMENTS.read_text(encoding="utf-8"))

    # Map the parsed JSON back to the required Requirement objects
    return [Requirement(id=item["id"], section=item["section"], text=item["text"]) for item in raw]
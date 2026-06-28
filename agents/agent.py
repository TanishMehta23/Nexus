from llm.gemini import ask_gemini
from tools.registry import TOOLS


def process_request(prompt: str):

    prompt_lower = prompt.lower()

    if prompt_lower.startswith("open "):

        app = prompt_lower.replace("open ", "").strip()

        return TOOLS["open_application"](app)

    return ask_gemini(prompt)
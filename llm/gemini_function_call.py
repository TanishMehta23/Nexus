from google import genai
from google.genai import types

from config.settings import GEMINI_API_KEY
from prompts.system_prompt import SYSTEM_PROMPT
from memory.conversation import get_history

client = genai.Client(api_key=GEMINI_API_KEY)


function = types.FunctionDeclaration(
    name="open_application",
    description="Open any installed Windows application.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "app_name": {
                "type": "string",
                "description": "Application name"
            }
        },
        "required": ["app_name"]
    },
)

tool = types.Tool(
    function_declarations=[function]
)


def get_function_call(user_prompt: str):

    history = get_history()

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{history}

User:
{user_prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",

        contents=prompt,

        config=types.GenerateContentConfig(
            tools=[tool]
        ),
    )

    return response


def generate_final_response(
    user_prompt: str,
    tool_result: str,
):

    history = get_history()

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{history}

User Request:
{user_prompt}

Tool Result:
{tool_result}

Respond naturally to the user.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
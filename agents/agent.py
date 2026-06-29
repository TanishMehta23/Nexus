from llm.gemini_function_call import (
    get_function_call,
    generate_final_response,
)

from tools.executor import execute_tool


def process_request(user_prompt: str):

    response = get_function_call(user_prompt)

    part = response.candidates[0].content.parts[0]

    # Normal Chat
    if not part.function_call:
        return response.text

    # Function Calling
    tool_name = part.function_call.name

    args = dict(part.function_call.args)

    tool_result = execute_tool(
        tool_name,
        **args
    )

    return generate_final_response(
        user_prompt,
        tool_result,
    )
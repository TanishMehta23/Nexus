from tools.registry import TOOLS


def execute_tool(tool_name: str, **kwargs):

    function = TOOLS.get(tool_name)

    if function is None:
        return f"Tool '{tool_name}' not found."

    return function(**kwargs)
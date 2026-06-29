from tools.registry import TOOLS


def get_tool_schemas():

    schemas = []

    for tool in TOOLS.values():

        schema = {
            "name": tool["name"],
            "description": tool["description"],
            "parameters": tool["parameters"]
        }

        schemas.append(schema)

    return schemas
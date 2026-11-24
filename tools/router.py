from tools.tools import open_app, search, screenshot, get_clipboard, set_clipboard, set_volume, mute, type_text

TOOLS = {
    "open_app": open_app,
    "search": search,
    "screenshot": screenshot,
    "get_clipboard": get_clipboard,
    "set_clipboard": set_clipboard,
    "set_volume": set_volume,
    "mute": mute,
    "type_text": type_text
}
def handle_tool(response):
    lines = response.split("\n")

    if lines[0].strip() == "TOOL":
        tool_name = lines[1].strip()

        if tool_name in TOOLS:
            if tool_name == "get_clipboard" or tool_name == "mute" or tool_name == "screenshot":
                return TOOLS[tool_name]()
            else:
                arg = lines[2].strip()
                return TOOLS[tool_name](arg)
    return None
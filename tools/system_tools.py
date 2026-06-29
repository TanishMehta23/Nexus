import subprocess
import os

from tools.app_finder import find_application


def open_application(app_name: str) -> str:
    """
    Open an installed Windows application.

    Args:
        app_name: Name of the application.

    Returns:
        Status message.
    """

    if app_name.lower() == "spotify":
        os.startfile("spotify:")
        return "Spotify opened successfully."

    path = find_application(app_name)

    if path is None:
        return f"Couldn't find '{app_name}'."

    subprocess.Popen(path)

    return f"{app_name} opened successfully."
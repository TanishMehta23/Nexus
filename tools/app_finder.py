import os

SEARCH_DIRECTORIES = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expandvars(r"%LOCALAPPDATA%\Programs"),
    os.path.expandvars(r"%APPDATA%"),
]

IGNORE_KEYWORDS = [
    "uninstall",
    "update",
    "updater",
    "installer",
    "setup",
    "crash",
    "helper",
    "launcher",
    "service",
    "migration",
    "migrator",
    "save-to",
]


def find_application(app_name: str):

    app_name = app_name.lower()

    exact_match = None
    partial_matches = []

    for directory in SEARCH_DIRECTORIES:

        if not os.path.exists(directory):
            continue

        for root, dirs, files in os.walk(directory):

            for file in files:

                if not file.lower().endswith(".exe"):
                    continue

                exe_name = file[:-4].lower()

                # Ignore helper executables
                if any(word in exe_name for word in IGNORE_KEYWORDS):
                    continue

                full_path = os.path.join(root, file)

                # Highest priority -> exact executable name
                if exe_name == app_name:
                    return full_path

                # Medium priority -> executable contains app name
                if app_name in exe_name:
                    partial_matches.append(full_path)

    if partial_matches:
        partial_matches.sort(key=len)
        return partial_matches[0]

    return None
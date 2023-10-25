import colours

data = None

def reload() -> None:
    """Reload the save file. (mainly used for debugging)"""
    data.load()
    print(f"{colours.OKGREEN}Data successfully reloaded!{colours.ENDC}")

def load(savedata) -> None:
    global data
    data = savedata

import inspect
import sys

import colours

data = None
plugins = {}

def help() -> None:
    """Describe what each command does"""
    print(f"{colours.HEADER}HELP{colours.ENDC}")
    for plugin in plugins.values():
        print(f"\n{colours.UNDERLINE}{plugin.__name__}{colours.ENDC}")
        for name, value in inspect.getmembers(plugin, inspect.isfunction):
            if name != "load":
                args = inspect.getfullargspec(value)[0]
                if not args:
                    print(f"{colours.BOLD}• {name}:{colours.ENDC}",
                          f"{inspect.getdoc(value)}")
                else:
                    args = " ".join((f"[{a}]" for a in args))
                    print(f"{colours.BOLD}• {name} {args}:{colours.ENDC}",
                          f"{inspect.getdoc(value)}")

def reload() -> None:
    """Reload the save file. (mainly used for debugging)"""
    data.load()
    print(f"{colours.OKGREEN}Data successfully reloaded!{colours.ENDC}")

def quit() -> None:
    """Exit the game :("""
    sys.exit()

def load(savedata, extensions) -> None:
    global data, plugins
    data = savedata
    plugins = extensions

"""Commands for miscellaneous purposes."""

import inspect
import sys

import colours

data = None
plugins = {}

def help() -> None:
    """Describe what each command does"""
    print(f"{colours.HEADER}HELP{colours.ENDC}")
    for p_name, plugin in plugins.items():
        print(f"\n{colours.UNDERLINE}{p_name} -",
              f"{plugin['_docstring']}{colours.ENDC}")
        for f_name, value in plugin.items():
            if f_name == "_docstring": continue
            args = value["args"]
            docstring = value["docstring"].splitlines()[0]
            if not args:
                print(f"{colours.BOLD}• {f_name}:{colours.ENDC}",
                      f"{docstring}")
            else:
                args_str = ""
                for arg, default in args:
                    if default is not None:
                        if default == "":
                            args_str += f"[{arg}: ''] "
                        else:
                            args_str += f"[{arg}: {default}] "
                    else:
                        args_str += f"[{arg}] "
                args_str = args_str.strip()
                print(f"{colours.BOLD}• {f_name} {args_str}:{colours.ENDC}",
                      f"{docstring}")

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
    for plugin in extensions.values():
        plugins[plugin.__name__] = {"_docstring": inspect.getdoc(plugin)}
        for name, value in inspect.getmembers(plugin, inspect.isfunction):
            if name != "load":
                fullargspec = inspect.getfullargspec(value)
                args = fullargspec[0]
                defaults = fullargspec[3] or []
                argslen = len(args)
                plugins[plugin.__name__][name] = {
                    "args": [],
                    "docstring": inspect.getdoc(value)
                }
                if args:
                    while len(defaults) < len(args):
                        defaults.append(None)
                    for arg, default in zip(reversed(args), defaults):
                        plugins[plugin.__name__][name]["args"].insert(0, (arg, default))

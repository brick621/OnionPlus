"""Commands for miscellaneous purposes."""

import inspect
import sys

import colours

data = None
plugins = {}

# TODO: generate a dictionary with all the plugins and commands outside
#  the help command (basically fix up the help command)

def help() -> None:
    """Describe what each command does"""
    print(f"{colours.HEADER}HELP{colours.ENDC}")
    for plugin in plugins.values():
        print(f"\n{colours.UNDERLINE}{plugin.__name__} -",
              f"{inspect.getdoc(plugin)}{colours.ENDC}")
        for name, value in inspect.getmembers(plugin, inspect.isfunction):
            if name != "load":
                fullargspec = inspect.getfullargspec(value)
                args = fullargspec[0]
                defaults = fullargspec[3] or ()
                argslen = len(args)
                if not args:
                    # TODO: add support for multi line docstrings
                    print(f"{colours.BOLD}• {name}:{colours.ENDC}",
                          f"{inspect.getdoc(value)}")
                else:
                    # TODO: come up with a better name than "args_str_list"
                    args_str_list = []
                    for i, a in enumerate(args):
                        if (argslen-i) <= len(defaults):
                            args_str_list.append(f"[{a}: '{defaults[(argslen-i) - 1]}]'")
                        else:
                            args_str_list.append(f"[{a}]")
                    args = " ".join(args_str_list)
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

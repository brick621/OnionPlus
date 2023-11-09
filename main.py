import datetime
import importlib
import inspect
import json
import os
from pathlib import Path

import colours
import utils

print(f"{colours.HEADER}Welcome to Onion+!{colours.ENDC}")

savefolder = Path("savefolder/")
if not savefolder.exists():
    os.mkdir("savefolder")
savefilespath = tuple(savefolder.iterdir())
savefiles = []
for savefile in savefilespath:
    savefiles.append(savefile.name.removesuffix(".json"))
load = False
if savefiles:
    load = input("Would you like to load a savefile? (Y/n) ").lower() != "n"

if load:
    print("Current savefiles:")
    print("\n".join(savefiles))
    name = ""
    while name not in savefiles:
        name = input("Enter the name of the save: ")
else:
    name = utils.get_name(savefiles)
data = utils.SaveData(name, not load)

plugins = {
    "simplegain": importlib.import_module("simplegain"),
    "see": importlib.import_module("see"),
    "interact": importlib.import_module("interact"),
    "misc": importlib.import_module("misc"),
}
# Get every command in each plugin
commands = {}
for plugin in plugins.values():
    if plugin.__name__ != "misc":
        plugin.load(data)
    else:
        plugin.load(data, plugins)
    for name, value in inspect.getmembers(plugin, inspect.isfunction):
        if name != "load":
            commands[name] = value

while True:
    prompt = input(f"{colours.BOLD}> {colours.ENDC}").split(" ")
    if not prompt:
        continue
    command = prompt[0]
    if command in commands:
        fullargspec = inspect.getfullargspec(commands[command])
        args = fullargspec[0]
        defaults = fullargspec[3] or ()
        required_args = len(args) - len(defaults)
        if len(prompt) >= 1 + required_args:
            commands[command](*prompt[1 : 1 + len(args)])

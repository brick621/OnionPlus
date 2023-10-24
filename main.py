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
    "see": importlib.import_module("see")
}
for plugin in plugins.values():
    # Make the data global in each plugin
    plugin.load(data)
commands = {
    "beg": plugins["simplegain"].beg,
    "cash": plugins["see"].cash
}

while True:
    prompt = input(f"{colours.BOLD}> {colours.ENDC}").split(" ")
    if not prompt:
        continue
    command = prompt[0]
    if command in commands:
        args = inspect.getfullargspec(commands[command])[0]
        if len(prompt) >= 1 + len(args):
            commands[command](*prompt[1:1+len(args)])

import datetime
import importlib
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
    "cash": plugins["see"].cash,
    "gear": plugins["see"].gear
}

while True:
    command = input(f"{colours.BOLD}> {colours.ENDC}")
    if command in commands:
        commands[command]()

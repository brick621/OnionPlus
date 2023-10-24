"""Contains various classes and functions to be used in other modules"""

import json
import os.path
import random
from shutil import copy
import time
import typing

class SaveData:
    """User save data for the game."""

    def __init__(self, name: str, new: bool = False) -> None:
        """Load a user's data.

        Arguments:
        name -- name of the file (excluding file extension)
        new -- if it should create/overwrite a file
        """
        self.name = name
        if not new:
            with open(os.path.join("savefolder", f"{name}.json")) as f:
                self._from_dict(json.load(f))
        else:
            self._from_dict({"savedata": {}, "metadata": {}})

    def save(self) -> None:
        """Saves this savedata to {self.name}.json in savefolder"""
        with open(os.path.join("savefolder", f"{self.name}.json"), "w") as f:
            json.dump(self._to_dict(), f, indent=4)

    def _to_dict(self) -> dict:
        return {
            "savedata": {
                "money": self.money,
                "inventory": self.inventory
            },
            "metadata": {
                "created": self.created,
                "modified": int(time.time())
            }
        }

    def _from_dict(self, values: dict) -> None:
        self.money = values["savedata"].get("money", 100)
        self.inventory = values["savedata"].get("inventory", [])

        self.created = values["metadata"].get("created", int(time.time()))


def choice(name: str) -> str:
    """Given the name of a file in resources, pick a random line.

    Arguments:
    name -- name of the file that is in resources

    Returns the line that was chosen at random
    """
    with open(os.path.join("resources", name)) as f:
        return random.choice(f.readlines()).strip()

def get_name(savefiles: typing.Iterable) -> str:
    """Get the user to input a name for a savefile.

    Arguments:
    savefiles -- list of currently existing savefile names

    Returns the name the user chose
    """
    validname = False
    while not validname:
        validname = True
        name = input("What would you like the savefile to be called: ")
        if not name:
            validname = False
            print("Please enter a name!")
        if name in savefiles:
            prompt = input(("There is already a savefile called '{name}'."
                            " would you like to overwrite it? N/y "))
            validname = prompt.lower() == "y"

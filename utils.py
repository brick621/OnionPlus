"""Contains various classes and functions to be used in other modules"""

import json
import os.path
import random
from shutil import copy
import time
import typing

import colours

_STARTING_MONEY = 100
_STARTING_INVENTORY = []
_STARTING_GEAR = {
    "hat": None,
    "back": "knapsack",
    "waist": None,
    "ring-l": None,
    "ring-r": None,
}

with open(os.path.join("resources", "items.json")) as f:
    ITEMS = json.load(f)


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
            self.load()
        else:
            self._from_dict({"savedata": {}, "metadata": {}})

    def add_item(self, item: str) -> bool:
        """Add an item to inventory.

        Arguments:
        item -- the item to add

        Returns True if successful, False otherwise.
        """
        if len(self.inventory) == self.max_inventory:
            return False
        else:
            self.inventory.append(item)
            return True

    def save(self) -> None:
        """Saves this savedata to {self.name}.json in savefolder"""
        with open(os.path.join("savefolder", f"{self.name}.json"), "w") as f:
            json.dump(self._to_dict(), f, indent=4)

    def load(self) -> None:
        with open(os.path.join("savefolder", f"{self.name}.json")) as f:
            self._from_dict(json.load(f))

    def _to_dict(self) -> dict:
        return {
            "savedata": {
                "money": self.money,
                "inventory": self.inventory,
                "max_inventory": self.max_inventory,
                "gear": {
                    "hat": self.gear["hat"],
                    "back": self.gear["back"],
                    "waist": self.gear["waist"],
                    "ring-l": self.gear["ring-l"],
                    "ring-r": self.gear["ring-r"],
                },
            },
            "metadata": {"created": self.created, "modified": int(time.time())},
        }

    def _from_dict(self, values: dict) -> None:
        self.money = values["savedata"].get("money", _STARTING_MONEY)
        self.inventory = values["savedata"].get("inventory", _STARTING_INVENTORY)
        self.max_inventory = values["savedata"].get("max_inventory", 5)
        self.gear = values["savedata"].get("gear", _STARTING_GEAR)
        # Add any new gear slots that may have been added in updates
        for slot, value in _STARTING_GEAR.items():
            if slot not in self.gear:
                self.gear[slot] = value

        self.created = values["metadata"].get("created", int(time.time()))


def money(money: int, colour: str = "") -> str:
    """Return a formated currency.

    Arguments:
    money -- the money to format
    colour -- ANSI escape sequence
    """
    if colour:
        return f"{colour}${money / 100:,.2f}{colours.ENDC}"
    else:
        return f"${money / 100:,.2f}"


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
            prompt = input(
                f"There is already a savefile called '{name}'. would you like to overwrite it? (y/N) "
            )
            validname = prompt.lower() == "y"
    return name

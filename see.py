"""Commands for seeing your items and money etc."""

import colours
import utils

data = None


def cash() -> None:
    """See the amount of cash you have."""
    print(utils.money(data.money))


def gear() -> None:
    """See what gear you currently have equiped."""
    for slot, value in data.gear.items():
        print(f"{colours.BOLD}{slot.capitalize()}: {colours.ENDC}{value}")


def inventory(arg: str = "") -> None:
    """See what is in your inventory.

    Enter with argument "detailed" to see more info on the items.
    """
    if not data.inventory:
        print(f"{colours.WARNING}You don't have any items!{colours.ENDC}")
    for item in set(data.inventory):
        print(f"{data.inventory.count(item)} {colours.HEADER}{item}{colours.ENDC}")
        if arg == "detailed":
            print(f"{colours.OKBLUE}{utils.ITEMS[item]['description']}{colours.ENDC}")


def load(savedata) -> None:
    global data
    data = savedata

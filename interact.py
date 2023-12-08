"""Commands for interacting with items."""

import colours
import utils

data = None


def equip(gear: str) -> None:
    """Equip a piece of gear."""
    gear = gear.lower()
    if gear not in utils.ITEMS:
        print(f"{colours.FAIL}That isn't a real item!{colours.ENDC}")
        return
    if utils.ITEMS[gear]["type"] != "gear":
        print(f"{colours.FAIL}That item is not a piece of gear!{colours.ENDC}")
        return
    if gear not in data.inventory:
        print(f"{colours.FAIL}You don't have this gear!{colours.ENDC}")
        return

    unequipped = None
    if data.gear[utils.ITEMS[gear]["slot"]]:
        unequipped = data.gear[utils.ITEMS[gear]["slot"]]
    data.gear[utils.ITEMS[gear]["slot"]] = gear
    data.inventory.remove(gear)
    if unequipped:
        data.add_item(unequipped)

    for attr, effect in utils.ITEMS[gear]["modifier"].items():
        # Set the new value of each effect
        current_value = getattr(data, attr, 0)
        setattr(data, attr, current_value + effect)
    data.save()
    print(f"{colours.OKGREEN}{gear} successfully equiped!{colours.ENDC}")


def unequip(gear: str) -> None:
    """Unequip a piece of gear."""
    gear = gear.lower()
    if gear not in utils.ITEMS:
        print(f"{colours.FAIL}That isn't a real item!{colours.ENDC}")
        return
    if utils.ITEMS[gear]["type"] != "gear":
        print(f"{colours.FAIL}That item is not a piece of gear!{colours.ENDC}")
        return
    for slot, value in data.gear.items():
        if value == gear:
            data.gear[slot] = None
            break
    else:
        print(f"{colours.FAIL}You don't have that gear equiped!{colours.ENDC}")
        return
    for attr, effect in utils.ITEMS[gear]["modifier"].items():
        current_value = getattr(data, attr, 0)
        setattr(data, attr, current_value - effect)
    if data.add_item(gear):
        data.save()
        print(f"{colours.OKGREEN}{gear} successfully unequiped!{colours.ENDC}")
    else:
        data.load()
        print(
            f"{colours.FAIL}This piece of gear is critical for max inventory!{colours.ENDC}"
        )


def load(savedata) -> None:
    global data
    data = savedata

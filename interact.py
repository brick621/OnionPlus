import colours

data = None

def equip(gear: str) -> None:
    """Equip a piece of gear."""
    gear = gear.lower()
    if gear not in data.inventory:
        print(f"{colours.FAIL}You don't have this gear!{colours.ENDC}")
        return
    data.gear["back"] = gear # temporary
    data.inventory.remove(gear)
    data.save()
    print(f"{colours.OKGREEN}{gear} successfully equiped!{colours.ENDC}")

def load(savedata) -> None:
    global data
    data = savedata
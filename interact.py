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

def unequip(gear: str) -> None:
    """unequip a piece of gear"""
    gear = gear.lower()
    for slot, value in data.gear.items():
        if value == gear:
            data.gear[slot] = None
            break
    else:
        print(f"{colours.FAIL}You don't have that gear equiped!{colour.ENDC}")
        return
    data.inventory.append(gear)
    data.save()
    print(f"{colours.OKGREEN}{gear} successfully unequiped!{colours.ENDC}")

def load(savedata) -> None:
    global data
    data = savedata
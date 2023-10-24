import colours

data = None

def cash() -> None:
    """See the amount of cash you have."""
    print(f"${data.money}")

def gear() -> None:
    """See what gear you currently have equiped."""
    for slot, value in data.gear.items():
        print(f"{colours.BOLD}{slot.capitalize()}: {colours.ENDC}{value}")

def load(savedata) -> None:
    global data
    data = savedata
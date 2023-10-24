data = None

def cash() -> None:
    """See the amount of cash you have."""
    print(f"${data.money}")

def load(savedata) -> None:
    global data
    data = savedata
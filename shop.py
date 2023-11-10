data = None


def sell(item: str, quantity: int) -> None:
    """Sell your goods to the market for some cash.

    Arguments:
    item -- the item you want to sell
    quantity -- how much of the item
    """
    print(item, quantity)


def load(savedata) -> None:
    global data
    data = savedata


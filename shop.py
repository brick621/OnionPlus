"""Commands for dealing with selling and buying items."""

data = None


def sell(item: str, quantity: int = 1) -> None:
    """Sell your goods to the market for some cash.

    Arguments:
    item -- the item you want to sell
    quantity -- how much of the item
    """
    print(item, type(quantity))


def load(savedata) -> None:
    global data
    data = savedata


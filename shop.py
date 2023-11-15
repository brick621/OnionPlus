"""Commands for dealing with selling and buying items."""

import colours
import utils

data = None


def sell(item: str, quantity: int = 1) -> None:
    """Sell your goods to the market for some cash.

    Arguments:
    item -- the item you want to sell
    quantity -- the amount of items (any number higher than what you have will sell all).
    """
    global data

    if item not in utils.ITEMS:
        print(f"{colours.FAIL}That is not an item! Make sure to replace any spaces with hyphens ('-'){colours.ENDC}")
        return
    
    if item not in data.inventory:
        print(f"{colours.FAIL}You do not have that item")
        return

    if quantity <= 0:
        print(f"{colours.FAIL}You have to have a positive quantity{colours.ENDC}")
        return

    if quantity > data.inventory.count(item):
        quantity = data.inventory.count(item)

    money_earned = utils.ITEMS[item]["sell-price"] * quantity
    for _ in range(quantity):
        data.inventory.remove(item)
    data.money += money_earned
    data.save()

    print(f"{colours.OKGREEN}You earned {utils.money(money_earned, colours.OKBLUE)}{colours.OKGREEN}!{colours.ENDC}")


def load(savedata) -> None:
    global data
    data = savedata


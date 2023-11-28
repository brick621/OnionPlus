"""Commands for dealing with selling and buying items."""

import json

import colours
import utils

data = None
with open("resources/shop.json") as f:
    market = json.load(f)


def sell(item: str, quantity: int = 1) -> None:
    """Sell your goods to the market for some cash.

    Arguments:
    item -- the item you want to sell
    quantity -- the amount of items (any number higher than what you have will sell all)
    """
    global data

    if item not in utils.ITEMS:
        print(f"{colours.FAIL}That is not an item! Make sure to replace any spaces with hyphens ('-'){colours.ENDC}")
        return
    
    if item not in data.inventory:
        print(f"{colours.FAIL}You do not have that item")
        return

    if quantity <= 0:
        print(f"{colours.FAIL}You have to give a positive quantity{colours.ENDC}")
        return

    if quantity > data.inventory.count(item):
        quantity = data.inventory.count(item)

    money_earned = utils.ITEMS[item]["sell-price"] * quantity
    for _ in range(quantity):
        data.inventory.remove(item)
    data.money += money_earned
    data.save()

    print(f"{colours.OKGREEN}You earned {utils.money(money_earned, colours.OKBLUE)}{colours.OKGREEN}!{colours.ENDC}")


def buy(item: str, quantity: int = 1) -> None:
    """Recieve some items in exchange for some cash.

    Arguments:
    item -- the item you want to buy
    quantity -- the amount of the chosen item
    """
    global data

    if quantity <= 0:
        print(f"{colours.FAIL}You have to give a positive quantity!{colours.ENDC}")
        return

    if not any([item in category for category in market.values()]):
        print(f"{colours.FAIL}That item either doesn't exist or isn't for sale{colours.ENDC}")
        return

    item_data = utils.ITEMS[item]
    price = item_data["buy-price"] * quantity
    if price > data.money:
        print(f"{colours.FAIL}You can't afford this purchase!{colours.ENDC}")
        return

    if data.max_inventory - len(data.inventory) < quantity:
        print(f"{colours.FAIL}You don't have enough inventory space to make this purchase{colours.ENDC}")
        return

    data.money -= price
    data.add_item(item, quantity)
    data.save()

    print(f"{colours.OKGREEN}Purchase success!{colours.ENDC}")


def shop(category: str = "") -> None:
    """View the items for sale.

    Arguments:
    category -- what you would like to see.
    """

    for category, items in market.items():
        print(f"{colours.UNDERLINE}{category}{colours.ENDC}")
        for item in items:
            print(f"{item}, {utils.money(utils.ITEMS[item]['buy-price'])} -- {utils.ITEMS[item]['description']}")
        print()


def load(savedata) -> None:
    global data
    data = savedata


"""Commands for simple methods of getting money and items."""

import random

import utils

data = None

def beg() -> None:
    """Quick and simple (if demeaning) method of gaining a small amount of money."""
    global data
    if random.random() <= 0.2:
        # Success
        given_money = random.randint(1, 5)
        data.money += given_money
        data.save()
        print('"' + utils.choice("yesbeg").format(given_money) + '"')
    else:
        # No money :(
        print('"' + utils.choice("nobeg") + '"')

def search() -> None:
    """Look around town for some goodies, including money or items!"""
    global data
    # Nummbers are cash.
    goodies = (1, 2, 5, "stick", "flint", "aluminium-can", "glass-bottle",
               "plastic-bottle")
    weights = 20, 10, 5, 50, 1, 30, 20, 35
    money_got = 0
    items_got = []
    won_goodies = random.choices(goodies, weights, k=random.randint(0, 3))
    for goody in won_goodies:
        if isinstance(goody, int):
            money_got += goody
        else:
            items_got.append(goody)
    for i, item in enumerate(items_got):
        if not data.add_item(item):
            # Remove the items that could not fit.
            items_got = items_got[:i]
            break
    data.money += money_got
    data.save()
    print(money_got, items_got)

def load(savedata) -> None:
    global data
    data = savedata
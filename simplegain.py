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

def load(savedata) -> None:
    global data
    data = savedata
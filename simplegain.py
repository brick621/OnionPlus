"""Commands for simple methods of getting money and items."""

import random

import colours
import utils

data = None

def beg() -> None:
    """Quick and simple (if demeaning) method of gaining a small amount of money."""
    global data
    if random.random() <= 0.2:
        # Success
        pool = 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000
        weights = 1, 1, 2, 5, 5, 10, 20, 15, 10, 1
        given_money = random.choices(pool, weights)[0]
        data.money += given_money
        data.save()
        print('"' + utils.choice("yesbeg").format(utils.money(given_money, colours.OKBLUE)) + '"')
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
    lost_items = 0
    for i, item in enumerate(items_got):
        if not data.add_item(item):
            # Remove the items that could not fit.
            lost_items = len(items_got[i:])
            items_got = items_got[:i]
            break
    data.money += money_got
    data.save()

    message_parts = []
    if money_got:
        message_parts.append(f"{utils.money(money_got, colours.OKBLUE)}")
    if items_got:
        item_count = {}
        for item in items_got:
            if item not in item_count:
                item_count[item] = items_got.count(item)
        articles = "a", "2", "3"
        items_received = []
        for item, count in item_count.items():
            # Substract 1 to account for 0-based lists
            items_received.append(f"{articles[count - 1]} "
                                  f"{colours.OKBLUE}{item}{colours.ENDC}")
        message_parts += items_received
    if lost_items:
        if lost_items == 1:
            message_parts.append(colours.WARNING
                                 + "an item that wasn't picked up because "
                                 + "your inventory was full"
                                 + colours.ENDC)
        else:
            message_parts.append(colours.WARNING
                                 + "some items that weren't picked up because "
                                 + "your inventory was full"
                                 + colours.ENDC)
    if not message_parts:
        message_parts.append(f"{colours.BOLD}NOTHING!{colours.ENDC}")

    if len(message_parts) == 1:
        print("You found", message_parts[0])
    else:
        print("You found",
              ", ".join(message_parts[:-1]),
              "and" if message_parts[:-1] else "",
              message_parts[-1])

def load(savedata) -> None:
    global data
    data = savedata

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": "$0"
}


def compare_money(money, drink):
    return round(money - MENU[drink]["cost"])


def compare_resources(drink_ing):
    enough_resources = True
    for item in drink_ing:
        if drink_ing[item] <= resources[item]:
            resources[item] -= drink_ing[item]
        else:
            print(f"Sorry there is not enough {item}")
            enough_resources = False
    return enough_resources


def show_report():
    print(resources)


def make_beverage(drink):
    return compare_resources(MENU[drink]["ingredients"])


def calculate_inserted_amount(coins):
    return coins["quarters"]*0.25 + coins["dimes"]*0.1 + coins["nickles"] *0.05 + coins["pennies"] * 0.01


machine_on = True

while machine_on:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ")
    if user_drink == 'report':
        show_report()
    elif user_drink == 'off':
        machine_on = False
    else:
        if make_beverage(user_drink):
            print("Please input coins: ")
            coins = {"quarters": int(input("How many quarters?: ")), "dimes": int(input("How many dimes?: ")),
                     "nickles": int(input("How many nickles?: ")), "pennies": int(input("How many pennies?: "))}
            paid_amount = calculate_inserted_amount(coins)
            change = compare_money(paid_amount, user_drink)
            if change >= 0:
                print(f"Here is ${change} in change")
                print(f"Here is your {user_drink}. Enjoy!")
            else:
                print("Sorry that is not enough money, money refunded")
        else:
            continue

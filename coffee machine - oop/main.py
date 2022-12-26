from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True


while machine_on:
    options = menu.get_items()
    user_drink = input(f"What would you like? ({options}): ")
    if user_drink == 'off':
        machine_on = False
    elif user_drink == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        ingredients = menu.find_drink(user_drink)
        resource_is_sufficient = coffee_machine.is_resource_sufficient(ingredients)
        if resource_is_sufficient:
            if money_machine.make_payment(ingredients.cost):
                coffee_machine.make_coffee(ingredients)


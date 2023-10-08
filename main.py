from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True



while is_on:
    options = menu.get_items()
    users_choice = input(f"What would you like? ({options}): ")
    if users_choice == "off":
        is_on = False
    elif users_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_drink = menu.find_drink(users_choice)
        if coffee_maker.is_resource_sufficient(user_drink) and money_machine.make_payment(user_drink.cost):
            coffee_maker.make_coffee(user_drink)


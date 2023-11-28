from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turned_on = True

menu = Menu()
coffee_masina = CoffeeMaker()
money_masina = MoneyMachine()

while turned_on:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        turned_on = False
    # When the user enters “report” to the prompt, a report should be generated
    elif request == "report":
        coffee_masina.report()
        money_masina.report()
    # Validation for valid drink name
    elif menu.find_drink(request) is None:
        continue
    # Check what is required for chosen drink
    else:
        menu_item = menu.find_drink(request)
        if coffee_masina.is_resource_sufficient(menu_item):
            if money_masina.make_payment(menu_item.cost):
                coffee_masina.make_coffee(menu_item)
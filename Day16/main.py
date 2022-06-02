from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    customer_order = input(f"\nWhat would you like? ({menu.get_items()}").lower()

    if customer_order == "off":
        machine_on = False
        print("Machine turning off.")
    elif customer_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(customer_order)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
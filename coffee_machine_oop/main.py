from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def vending_machine_order():
    cont = True
    while cont:
        order = input(f"What would you like? {machine_menu.get_items()}: ").lower()
        if order == 'report':
            coffee_maker.report()
            money_machine.report()
        elif order == 'off':
            cont = False
        else:
            order_item = machine_menu.find_drink(order)
            if order_item != None:
                if coffee_maker.is_resource_sufficient(order_item):
                    print(f"The price of this item is ${order_item.cost}")
                    money_machine.make_payment(order_item.cost)
                    coffee_maker.make_coffee(order_item)

vending_machine_order()

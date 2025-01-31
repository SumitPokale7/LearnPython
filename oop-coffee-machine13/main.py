from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_On = True
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


while is_On:
    choice_Coffee = input(f"What would you like? {menu.get_items()}: ")

    if choice_Coffee == "off":
        is_On = False
    elif choice_Coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice_Coffee)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

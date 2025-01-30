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
}


is_On = True
profit = 0


def is_resource_sufficient(order_Ingredients):
    """Returns true when order can be made, False if ingredients are insufficient."""
    for item in order_Ingredients:
        if order_Ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_Coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recived, drink_cost):
    """Returns True when the payment is accepted, or false if money is insufficient."""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_Coffee(drink_Name, order_Ingredients):
    """Dedut the required ingredients from the resources."""
    for item in order_Ingredients:
        resources[item] -= order_Ingredients[item]
    print(f"Here is your {drink_Name} ☕")


while is_On:
    choice_Coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if choice_Coffee == "off":
        is_On = False
    elif choice_Coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice_Coffee]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_Coins()
            if is_transaction_successful(payment, drink['cost']):
                make_Coffee(choice_Coffee, drink['ingredients'])

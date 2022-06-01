from art import machine
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def count_money():
    """Counts the money received."""
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .1
    total += int(input("How many nickles? ")) *.05
    total += int(input("How many pennies? ")) *.01
    return total

def transaction_successful(money_received, drink_cost):
    """Return True when payment is successful, otherwise return False"""
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True

def print_report():
    """Prints the resources left in the machine."""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

def check_resources(ingredients):
    """Gathers inputs for coffee type and checks if there's enough resources."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True

def adjust_resources(drink_name, ingredients):
    """Deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here's your {drink_name}. Enjoy!")

def make_drink(choice):
    """Takes the coffee type, checks resources and makes the coffee if there's enough resources."""
    drink_choice = MENU[choice]
    enough_resources = check_resources(drink_choice["ingredients"])
    
    if enough_resources:
        coffee_cost = drink_choice['cost']
        print(f"The cost is ${coffee_cost}")
        payment = count_money()
        enough_money = transaction_successful(payment, coffee_cost)

        if enough_money:
            adjust_resources(choice, drink_choice["ingredients"])
            
            

machine_on = True
while machine_on:
    print(machine)
    prompt = input("\nWhat would you like? (espresso/latte/cappuccino) ").lower()
    
    if prompt == "off":
        machine_on = False
        print("Machine turning off.")
    elif prompt == "report":
        print_report()
    else:
        make_drink(prompt)
import os
def clear_screen():
    os.system("cls|clear")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}

def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(request):
    resource_lack = 0
    for item in ['water','milk','coffee']:
        if resources[item] < MENU[request]['ingredients'][item]:
            print(f"There is not enough {item}.")
            resource_lack += 1
    if resource_lack == 0:
        return True
    else:
        return False

def money_check(type):
    unit_check = True
    while unit_check:
        amount = input(f"How many {type}s?: ")
        if amount.isdigit():
            amount = int(amount)
            unit_check = False
        else:
            print("Please enter a whole number.")
    return amount
    
def calculate_input_amount(type, amount):
    total_payment = 0    
    if type == 'quarter':
        total_payment += amount * 0.25
    elif type == 'dime':
        total_payment += amount * 0.10
    elif type == 'nickle':
        total_payment += amount * 0.05
    else:
        total_payment += amount * 0.01
    return total_payment

def resource_deduction(request):
    for item in ['water','milk','coffee']:
        resources[item] = resources[item] - MENU[request]['ingredients'][item]

clear_screen()

money = 0
cont = True
while cont:
    # clear_screen()
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == 'report':
        print_resources()
    elif request == 'off':
        cont = False
    elif request in ["espresso","latte", "cappuccino"]:
        if check_resources(request):
            print("Please insert coins.")
            quarter_amount = money_check('quarter')
            dime_amount = money_check('dime')
            nickle_amount = money_check('nickle')
            penny_amount = money_check('pennie')
            total_payment = (calculate_input_amount('quarter',quarter_amount)
                             + calculate_input_amount('dime', dime_amount)
                             + calculate_input_amount('nickle',nickle_amount) 
                             + calculate_input_amount('penny',penny_amount)
                             )
            change = round(total_payment - MENU[request]['cost'],2)
            if change >= 0:
                print(f"Here is ${change} in change.")
                print(f"Here is your {request} ☕. Enjoy!")
                money += MENU[request]['cost']
                resource_deduction(request)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("You entered an invalid response. Please try again!")

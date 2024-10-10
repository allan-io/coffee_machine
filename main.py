from data import menu, resources

def check_if_enough_resources(bev):
    has_enough_resources = True
    missing_resources = []
    for key in bev["ingredients"]:
        if bev["ingredients"][key] > resources[key]:
            has_enough_resources = False
            missing_resources.append(key)
    return {
        "has_enough_resources": has_enough_resources,
        "missing_resources": missing_resources,
    }

def calc_coin_input(bev):
    coin_value = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    print(f"Please insert ${bev["cost"]:.2f} in coins.")
    coin_value["quarters"] *= int(input("How many quarters: "))
    coin_value["dimes"] *= int(input("How many dimes: "))
    coin_value["nickels"] *= int(input("How many nickels: "))
    coin_value["pennies"] *= int(input("How many pennies: "))

    return sum(coin_value.values())

def use_resources(bev_ingredients):
    resources_copy = {}
    for key in bev_ingredients:
        resources_copy[key] = resources[key] - bev_ingredients[key]
    return resources_copy

def run_machine():
    global resources
    machine_on = True
    initial_bank = 20
    money = 0
    profit = money - initial_bank
    # beverage = {}
    selection = input("Please make a selection: \ntype 'espresso' or 'cappuccino' or 'latte\n")

    while machine_on:
        if selection == "latte" or selection == "espresso" or selection == "cappuccino":
            beverage = menu[selection]
            enough_resources = check_if_enough_resources(beverage)
        elif selection == "off":
            machine_on = False
        elif selection == "report":
            print(f'''
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: {money:.2f}''')
        else:
            print("Invalid Selection")

        if selection != "report" and not enough_resources["has_enough_resources"]:
            print(f"Not enough {enough_resources["missing_resources"][0]}")
        if selection != "report" and enough_resources:
            total_inserted = calc_coin_input(beverage)
            if total_inserted < beverage["cost"]:
                print("not enough money. Your money has been refunded.")
            else:
                if total_inserted > beverage["cost"]:
                    print(f"Here is your change: ${(total_inserted - beverage["cost"]):.2f}")
                print(f"Here is your {selection}! Enjoy ☕️")
                new_resources = use_resources(beverage["ingredients"])
                resources = new_resources
                money += beverage["cost"]
            selection = input("Please make a selection: \ntype 'espresso' or 'cappuccino' or 'latte\n")
        else:
            run_machine()
run_machine()

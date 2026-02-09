logo = """
                                                                                     
  ,ad8888ba,                  ad88     ad88                                          
 d8"'    `"8b                d8"      d8"                                            
d8'                          88       88                                             
88              ,adPPYba,  MM88MMM  MM88MMM  ,adPPYba,   ,adPPYba,                   
88             a8"     "8a   88       88    a8P_____88  a8P_____88                   
Y8,            8b       d8   88       88    8PP"""""""  8PP"""""""                   
 Y8a.    .a8P  "8a,   ,a8"   88       88    "8b,   ,aa  "8b,   ,aa                   
  `"Y8888Y"'    `"YbbdP"'    88       88     `"Ybbd8"'   `"Ybbd8"'                   
                                                                                     
                                                                                     
                                                                                     
88b           d88                          88           88                           
888b         d888                          88           ""                           
88`8b       d8'88                          88                                        
88 `8b     d8' 88  ,adPPYYba,   ,adPPYba,  88,dPPYba,   88  8b,dPPYba,    ,adPPYba,  
88  `8b   d8'  88  ""     `Y8  a8"     ""  88P'    "8a  88  88P'   `"8a  a8P_____88  
88   `8b d8'   88  ,adPPPPP88  8b          88       88  88  88       88  8PP"""""""  
88    `888'    88  88,    ,88  "8a,   ,aa  88       88  88  88       88  "8b,   ,aa  
88     `8'     88  `"8bbdP"Y8   `"Ybbd8"'  88       88  88  88       88   `"Ybbd8"'  
                                                                                     
                                                                                      """


print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3,
    }
}

RESOURCES = {
    "water": 1000,
    "coffee": 100,
    "milk": 1000,
    "money": 0
}
def purchase(order):
    if MENU[order]['ingredients']['water'] > RESOURCES['water']:
            print("Sorry there is not enough water to complete your order")
            return
    elif MENU[order]['ingredients']['milk'] > RESOURCES['milk']:
        print("Sorry there is not enough milk to complete your order")
        return
    elif MENU[order]['ingredients']['coffee'] > RESOURCES['coffee']:
        print("Sorry there is not enough coffee to complete your order")
        return
    print(f'Cost: {MENU[order]['cost']}')
    print("Insert Coins")
    quarters = int(input("How much quarters would you use? "))
    dimes = int(input("How much dimes would you use? "))
    nickles = int(input("How much nickles would you use? "))
    pennies = int(input("How much pennies would you use? "))
    sum = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01) 
    sum = round(sum,2)
    print(f'Total inserted {sum}')
    if(sum < MENU[order]['cost']):
         print("It is not enough, refunding your money...")
         return
    else:
        change = sum - MENU[order]['cost']
        change = round(change,2)
        RESOURCES["money"] = sum + RESOURCES["money"]
        print(f'Your change: {change}')
        money = RESOURCES["money"]
        total = money - change
        total = round(total,2)
        RESOURCES["money"] = total
    RESOURCES["water"] = int(RESOURCES["water"]) - int(MENU[order]['ingredients']['water'])
    RESOURCES["milk"] = int(RESOURCES["milk"]) - int(MENU[order]['ingredients']['milk'])
    RESOURCES["coffee"] = int(RESOURCES["coffee"]) - int(MENU[order]['ingredients']['coffee'])
    print(f'Enjoy your coffee!')

def report():
    print("Resources Report")
    print(f'Water: {RESOURCES["water"]}')
    print(f'Milk: {RESOURCES["milk"]}')
    print(f'coffee: {RESOURCES["coffee"]}')
    return

def refill(order):
    if (order == "coffee"):
        amount = int(input("How many grams of coffee would you like to add? "))
        RESOURCES[order] = amount + RESOURCES[order]
        return
    else:
        amount = int(input(f"How many ml of {order} would you like to add? "))
        RESOURCES[order] = amount + RESOURCES[order]
        return
while True:
    #Secret Commands report, refill
    order = input("What would you like? Espresso, Latte, Cappuccino, Exit (Type the option) ").lower()
    if (order == "espresso" or order == "latte" or order == "cappuccino"):
        purchase(order)
    elif(order == "exit"):
         print("Thanks! have a good day!")
         break
    elif(order == "report"):
         report()
         print(f'money: {RESOURCES["money"]}')
    elif(order == "refill"):
        while True:
            report()
            order = input("What do you want to fill? Water, Milk, Coffee, Exit (Type the option) ").lower()
            if (order == "water" or order == "milk" or order == "coffee"):
                 refill(order)
            elif(order == "exit"):
                break
            else:
                print("Select a valid option")
            
    else:
        print("Select a valid option")


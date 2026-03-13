from data_center import coins
from data_center import coffe_menu 
from data_center import tank
machine_working = True
def tank_refill(tank):
    tank["water"] += float(input("How much water are you going to add? "))
    tank["coffe"] += float(input("How much coffe are you going to add? "))
    tank["milk"] += float(input("How much milk are you going to add? "))
    tank["bank"] += float(input("How much money are you going to add? "))

def prepare_coffe(order,tank,menu):
    selected_drink = None
    for drink in menu:
        if drink["type"].lower() == order:
            selected_drink = drink
            break
    if selected_drink == None:
            print("choose a valid option")
            return 
    if tank["water"]< selected_drink["water"]:
        print("There isn't enought water")
        fill_it = input("Do you want to fill the tank? 'y' or 'n' ?").lower()
        if fill_it == "y":
            tank["water"] += float(input("How much water do you want to add? "))
        else:
             return
    if tank["coffe"]< selected_drink["coffe"]:
        print("There isn't enought coffe")
        fill_it = input("Do you want to fill the tank? 'y' or 'n' ?").lower()
        if fill_it == "y":
            tank["coffe"] += float(input("How much coffe do you want to add? "))
        else:
             return
    if tank["milk"]< selected_drink["milk"]:
        print("There isn't enought milk")
        fill_it = input("Do you want to fill the tank? 'y' or 'n' ?").lower()
        if fill_it == "y":
            tank["milk"] += float(input("How much milk do you want to add? "))
        else:
             return
    tank["water"] -= selected_drink["water"]
    tank["coffe"] -= selected_drink["coffe"]
    tank["milk"] -= selected_drink["milk"]

    print(tank)

user_order=input("What would you like to order?\n" 
                "Espresso/Latte or Cappuccino?").lower()
prepare_coffe(user_order,tank,coffe_menu)

# Treasure Island

print("-----Welcome to Treasure Island game-----")
#printing treasure shape
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
******************************************************************************* 
 ''')


choice1 = input("You are at a cross road, where do you want to go? Type 'left' or 'right': ").lower().strip()
if choice1 == "right":
    print("You have come to a lake. There is an island in the middle of the lake.")
    choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower().strip()
    if choice2 == "wait":
        print("A mysterious boatman appears. He offers two boats.")
        choice_boat = input("Type 'gold' to take the gold boat. Type 'silver' to take the silver boat: ").lower().strip()
        if choice_boat == "silver":
            print("The silver boat carries you safely to a house. There is a door in the house.")
            choice3 = input("Type 'red' to open the red door. Type 'blue' to open the blue door. Type 'yellow' to open the yellow door: ").lower().strip()
            if choice3 == "yellow":
                print("You have found the treasure! You Win!")
            elif choice3 == "blue":
                print("You have been eaten by beasts. Game Over.")
            else:
                print("You are burned by fire. Game Over.")
        else:
            print("The gold boat is too heavy and sinks. Game Over.")
    else:
        print("You are attacked by a giant trout while swimming. Game Over.")
elif choice1 == "left":
    print("You find yourself at the entrance of a dark, narrow bridge.")
    choice_bridge = input("Type 'cross' to walk across the bridge. Type 'search' to look for another way: ").lower().strip()
    if choice_bridge == "search":
        print("You find a hidden tunnel that leads straight to the treasure room! You Win!")
    else:
        print("The bridge collapses under your weight. Game Over.")
else:
    print("You wandered off the path and fell into a hole. Game Over.")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

number_to_check = int(input("Enter a number: "))

if number_to_check % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("-----Welcome to roller coaster-----")
height = int(input("Enter your height in cm: "))
    
if height >= 120:
    print("You can ride the roller coaster.")

    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print(f"Your total is {bill}. without photo")
    elif age < 18:
        bill = 7
        print(f"Your total is {bill}. without photo")
    elif age > 18 and age < 55:
        bill = 12
        print(f"Your total is {bill}. without photo")
    elif age >= 55:
        print("You are not safe to ride the roller coaster.")
    
    photo = input("Do you want a photo? Type 'Y' or 'N': ")
    if photo.lower() == "y":
        bill += 3
        print(f"Your total is {bill}. with photo")
    else:
        print(f"Your total is {bill}. without photo")
else:
    print("You cannot ride the roller coaster.")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print('-----Welcome to python pizza delivery-----')
size = input("What size of pizza do you want? S, M or L: ").lower().strip()
paperoni = input("Do you want paperoni? Type 'Y' or 'N': ").lower().strip()
extra_cheese = input("Do you want extra cheese? Type 'Y' or 'N': ").lower().strip()

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_medium_large = 3
extra_cheese_price = 1

bill = 0
if size == "s" and paperoni == "y" and extra_cheese == "y":
    bill += small_pizza + pepperoni_small + extra_cheese_price
elif size == "s" and paperoni == "y" and extra_cheese == "n":
    bill += small_pizza + pepperoni_small
elif size == "s" and paperoni == "n" and extra_cheese == "y":
    bill += small_pizza + extra_cheese_price
elif size == "s" and paperoni == "n" and extra_cheese == "n":
    bill += small_pizza
elif size == "m" and paperoni == "y" and extra_cheese == "y":
    bill += medium_pizza + pepperoni_medium_large + extra_cheese_price
elif size == "m" and paperoni == "y" and extra_cheese == "n":
    bill += medium_pizza + pepperoni_medium_large
elif size == "m" and paperoni == "n" and extra_cheese == "y":
    bill += medium_pizza + extra_cheese_price
elif size == "m" and paperoni == "n" and extra_cheese == "n":
    bill += medium_pizza
elif size == "l" and paperoni == "y" and extra_cheese == "y":
    bill += large_pizza + pepperoni_medium_large + extra_cheese_price
elif size == "l" and paperoni == "y" and extra_cheese == "n":
    bill += large_pizza + pepperoni_medium_large
elif size == "l" and paperoni == "n" and extra_cheese == "y":
    bill += large_pizza + extra_cheese_price
else:
    bill += large_pizza
    
# if size == "s":
#     bill += small_pizza
# elif size == "m":
#     bill += medium_pizza
# else:
#     bill += large_pizza

# if paperoni == "y":
#     if size == "s":
#         bill += pepperoni_small
#     elif size == "m" or size == "l":
#         bill += pepperoni_medium_large

# if extra_cheese == "y":
#     bill += extra_cheese_price

# print(f"Your total is {bill}")


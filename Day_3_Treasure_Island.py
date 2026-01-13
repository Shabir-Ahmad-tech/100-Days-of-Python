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


# End of Treasure Island game
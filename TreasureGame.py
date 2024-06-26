print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choice1 = input("You\'re near the ocean. Do you want to wait for the boat or want to swim? Enter 'wait' for wait and 'swim' for swim.\n")
if choice1 == 'wait':
    print("Your boat is ready to go.")
    choice2 = input("Do you want to bring the weapons with you? Write yes or no.\n")
    choice3 = input("Do you want to bring the map with you? Write yes or no.\n")
    print("Your map is kept")
    choice4 = input("The pirates are attacking on you in middle of the sea. Would you like to fight or move\n")
    if choice4 == 'fight':
        if choice2 == 'yes':
            print("Your weapon are kept in secret box of the boat.")
            print("You are ready to defend your side.")
            print("You won the fight. Keep it up")
        elif choice4 == 'move':
            if choice3 == 'no':
                print("Oh my God, you are lost, you don't have the map. Game over!")
            else:
                print("You are safe now, you can move ahead using map.")
                print("You have seen the island.")
                choice5 = input("Write to go or move to next.\n")
                if choice5 == 'go':
                    print("Yeh! you have done it, you have found the treasure.")
                    print("You won the game :-)")
        else:
            print("I am sorry your game is over, you have no weapon to defend you, they will bombard on you.")
else:
    print("Game over, sea animal eat you.")
    
    
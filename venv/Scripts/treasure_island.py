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
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure...")

direction = input("You're at a crossroad. Where do you want to go?, type 'left or 'right: ".lower())

if direction != "left" and  direction != 'right':
    print("Game Over")

elif direction == 'right':
    print("FALL INTO THE HOLE....GAME OVER..")

else:
    lake = input(
    """
    You've come to a lake. There is an island in the middle of it.
    Type 'Wait' to wait for a boat or 'Swim' to swim across: 
    """).lower()

    if lake != 'wait' and lake != 'swim':
        print("Game Over")
    
    elif lake == "swim":
        print("ATTACKED BY TROUT, GAME OVER...")
    
    else:
        house = input(
    """
    You're arrived at the island uncharmed. There's a house with three
    doors. One red, one yellow, and one blue. Which color do you
    choose?: 
    """).lower()
                
        if house == "red":
            print("BURNED BY FIRE...GAME OVER")
        
        elif house == 'blue':
            print("EATEN BY BEASTS...GAME OVER")
        
        elif house == "yellow":
            print("CONGRATS....YOU WIN....")
        
        else:
            print("YOU'VE CHOSEN A DOOT THAT DOESN'T EXISTS...GAME OVER")

#  CREATE YOUR OWN GAME....


    


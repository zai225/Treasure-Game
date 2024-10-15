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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("........Welcome to treasure Island........")
print("...Your mission is to find the treasure...\n....There are exciting twist and turns coming on the way....\n................All the Best...............")

first_option = input("You're at a cross road. Where do you want to go?\nType 'left' or 'right' \n ")
if first_option == "left":
    print("You have come to a lake. There is a Island in the middle.")


    second_option = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n ")
    if second_option == "wait":
        print("A boat come through and led you to a mystery room")

        third_option = input("Wecome the mystery room my Friend!!!\nNow there are three doors in the mystery room which one would you pick??\n'blue', 'red' or 'yellow': ")
        if third_option == "blue":
            print("OOops!!! There were lots of beasts in this room and you were eaten\n'Game Over'")
        elif third_option == "red":
            print("OOopsss!! This door was full of fire and you were burned\n'Game Over'")
        elif third_option == "yellow":
            print("WOOHOOO!!! YOU WON\nCongratulation my friend you have succsessfully found the treasure")
        else:
            print("OOPSS! You entered wrong input\n'Game Over'")



    elif second_option == "swim":
        print("OOPS! There were a lots of crocodiles in the lake and you were attacked. 'Game Over'")
    else:
        print("OOPSS! You entered wrong input\n'Game Over'")

elif first_option == "right":
    print("You fall into a hole. 'Game Over")
else:
    print("OOPSS! You entered wrong input\n'Game Over'")
fail = '''
                                 _____  _____
                                <     `/     |
                                 >          (
                                |   _     _  |
                                |  |_) | |_) |
                                |  | \ | |   |
                                |            |
                 ______.______%_|            |__________  _____
               _/                                       \|     |
              |                                                <
              |_____.-._________              ____/|___________|
                                |            |
                                |            |
                                |            |
                                |            |
                                |   _        <
                                |__/         |
                                 / `--.      |
                               %|            |%
                           |/.%%|          -< @%%%
                           `\%`@|     v      |@@%@%%    - mfj
                         .%%%@@@|%    |    % @@@%%@%%%%
                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%'''

win = '''
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
'''
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print('You come to a fork in the path.')
choice = input('\tDo you want to go "left" or "right"? ')

if choice[0].lower() != 'l':
    print('\nYou fall into a pit of snakes.')
    print(fail)
else:
    print('\nYou come across a rushing river in the rain.')
    choice = input('\tDo you want to "wait" out the rain or "swim"? ')
    if choice[0].lower() != 'w':
        print("""\nYou're swepted off by the current and drown.""")
        print(fail)
    else:
        print('\nYou find a large buiiding in the woods with three doors:')
        print('a "red" door, a "blue" door, and a "yellow" doror.')
        choice = input('\tWhich door would you like to go into? ')
        if choice[0].lower() == 'r':
            print("\nFlame erupts out from behind the door and you're burned to ashes.")
            print(fail)
        elif choice[0].lower() == 'b':
            print("\nA hungry lion ponces on you and you join the circle of life.")
            print(fail)
        elif choice[0].lower() == 'y':
            print("\nYou find the treasure! You win!")
            print(win)
        else:
            print("\nYou wonder away from the building and get lost.")
            print(fail)

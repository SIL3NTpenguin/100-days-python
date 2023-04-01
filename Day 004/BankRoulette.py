# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

names_len = len(names)

randomPosition = random.randint(0,names_len-1)

randomName = names[randomPosition]

print(f'{randomName} is going to buy the meal today!')
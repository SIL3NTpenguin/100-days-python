#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to the tip calculator!')
check_amount = float(input("How much was the check? "))
tip_percent = float(input("What percentage tip would you like to give? "))/100
split_num = int(input("How many people are splitting the total bill? "))

tip_amount = round(check_amount * tip_percent,2)
check_total = round(check_amount + tip_amount,2)
split_amount = round(check_total/split_num,2)

print('\n')
print(f"The tip amount is ${tip_amount:.2f}, bringing the bill total up to ${check_total:.2f}.")
print(f"This bill split between {split_num} people will be ${split_amount:.2f} per person.")
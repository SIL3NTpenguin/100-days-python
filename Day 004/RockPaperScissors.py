import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handIdentify = ['r', 'p', 's']
handImages = [rock, paper, scissors]
handWin = [2, 0, 1]

#Write your code below this line 👇

if __name__ == '__main__':
    print('Get ready to rumble!')
    playerChoice = input('What do you choose? Rock, Paper, or Scissors? ')
    
    playerChoice = playerChoice[0].lower()
    playerChoice = handIdentify.index(playerChoice)
    computerChoice = random.randint(0,2)

    print(handImages[playerChoice])
    print('Computer chose:')
    print(handImages[computerChoice])

    if playerChoice == computerChoice:
        print('You tied')
    elif handWin[playerChoice] == computerChoice:
        print('You win!!!')
    else:
        print('You lose...')

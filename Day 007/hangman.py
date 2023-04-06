import random
import art

#Select a word
word_list = ['ballon', 'pillow', 'banana', 'motorcycle', 'cheesecake', 'sleep', 'python']
random.shuffle(word_list)
chosen_word = word_list.pop().lower()

#Defining player variables
player_guesses = ''
valid_inputs = 'abcdefghijklmnopqrstuvwxyz'
lives = 6

#Take player input and validate
def request_guess():
    global player_guesses
    player_input = input('Guess a letter: ').lower()
    if player_input not in valid_inputs or len(player_input) != 1:
        print('Please provide a single letter input')
        request_guess()
    elif player_input in player_guesses:
        print(f'Already guessed the letter {player_input}. Please try a new letter.')
        request_guess()
    else:
        player_guesses += player_input
        return player_input
    
def create_word_display(word):
    word_display = []
    for letter in word:
        word_display.append('_')
    print(' '.join(word_display))
    return word_display

def update_game(word, guess, word_display):
    global lives
    
    matched = False
    for position in range(len(word)):
        if guess == word[position]:
            word_display[position] = guess
            matched = True   
    if not matched:
        lives -= 1
    display(word_display,lives)

def display(word_display, lives):
    print(' '.join(word_display))
    print(art.stages[lives])

def check_game_state(lives, word_display, chosen_word):
    if lives == 0:
        print(f'Word was {chosen_word}')
        print('Game Lost')
        return False
    if '_' not in word_display:
        print('Game Won')
        return False
    else:
        return True

    
### For testing only ###
# print(f'pssst, the solution is {chosen_word}')
### For testing only ###

word_display = create_word_display(chosen_word)

game_on = True

while game_on:
    guess = request_guess()
    guess_result = update_game(chosen_word,guess,word_display)
    game_on = check_game_state(lives, word_display, chosen_word)
    

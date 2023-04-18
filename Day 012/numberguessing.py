import random
import os
import art


def pick_num():
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)


def set_difficulty():
    _attempts = {"easy": 10, "hard": 5}
    _choice = input("Choose a difficulty. type 'easy' or 'hard': ")
    if _choice.lower() not in ("easy", "hard"):
        print("Only acceptable inputs are 'easy' or 'hard'. Please try again.")
        return set_difficulty()
    else:
        return _attempts[_choice.lower()]


def win(answer):
    print(f"You got it! The answer was {answer}")


def lose(answer):
    print("You've run out of guesses, you lose.")
    print(f"\n The correct answer was {answer}")


def guess_num(target_num, attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts -= 1
    _guess = input("Make a guess: ")
    _guess = int(_guess)
    if _guess == target_num:
        win(target_num)
    elif attempts == 0:
        lose(target_num)
    elif _guess > target_num:
        print("Too high.")
    else:
        print("Too low.")
    return _guess, attempts


def clear():
    # for windows
    if os.name == "nt":
        _ = os.system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system("clear")


def game():
    print(art.logo)
    print("Welcome to the Guessing Game!")
    answer = pick_num()
    attempts = set_difficulty()
    guess = 0
    while guess != answer and attempts != 0:
        guess, attempts = guess_num(answer, attempts)
    replay = input("Do you want to play again? 'y' or 'n': ")
    if replay == "y":
        clear()
        game()
    else:
        exit()


if __name__ == "__main__":
    clear()
    game()

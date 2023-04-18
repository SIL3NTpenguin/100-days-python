"""
Main module for Higher Lower game.
"""

import os
from random import randint

import art
import game_data


def clear():
    """
    Clears console
    """
    # for windows
    if os.name == "nt":
        _ = os.system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system("clear")


def celebrity_selection(pre_sel=""):
    choice = randint(0, len(game_data.data) - 1)
    choice = game_data.data[choice]
    if choice["name"] == pre_sel:
        return celebrity_selection(pre_sel)
    else:
        return choice


def celeb_details(celeb: dict):
    c = celeb
    return f"{c['name']}, a {c['desc']}, from {c['country']}"


def new_round(last_celeb=None, score=None):
    if last_celeb is None:
        last_celeb = celebrity_selection()
    a = last_celeb
    b = celebrity_selection(a["name"])
    clear()
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {celeb_details(a)}")
    print(art.vs)
    print(f"Against B: {celeb_details(b)}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    new_score = 0
    if choice.lower() == "a" and a["follower_count"] > b["follower_count"]:
        new_score += 1
    elif choice.lower() == "b" and a["follower_count"] < b["follower_count"]:
        new_score += 1
    return new_score, b


def lose(score):
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    return False


def higherlower():
    last_celeb = None
    score = 0
    game_on = True
    while game_on:
        score_add, last_celeb = new_round(last_celeb, score)
        if score_add == 1:
            score += score_add
        else:
            game_on = lose(score)
        print(score)


if __name__ == "__main__":
    higherlower()

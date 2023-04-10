import art
import os

auction = {}

def add_bid():
    name = input("What is your name? ")
    name = name.title()
    name = ' '.join(name.split())
    bid = input("What's your bid? ")
    try: 
        bid = float(bid)
    except:
        print("Only number is accepted as bid. Please try again.")
        add_bid()
    clear()
    auction[name] = bid

def find_highest_bid():
    highest_bid = ['',0]
    for name in auction:
        if auction[name] > highest_bid[1]:
            highest_bid = [name, auction[name]]
    return highest_bid

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


if __name__ == '__main__':
    bidding = 'y'
    
    print(art.gavel)
    while bidding[0].lower() == 'y':
        add_bid()
        bidding = input("Does anyone else want to bid? (Y/N) ")
        clear()
    winner = find_highest_bid()
    print(f"{winner[0]} won the auction by bidding ${winner[1]:.2f}!!")
    
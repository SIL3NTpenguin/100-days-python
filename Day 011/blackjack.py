import art
import random
import os

suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
values = {
    'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
    , 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9
    , 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10
    }

def _card_values():
    _card_values = {}
    for suit in suits:
        for face in values:
            _card_values[f'{face} of {suit}'] = values[face]
    return _card_values

def create_deck():
    deck = []
    for suit in suits:
        for face in values:
            deck.append(f'{face} of {suit}')
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def draw_card(hand: list, deck: list):
    drawn_card = deck.pop()
    hand.append({drawn_card: card_values[drawn_card]})
    return hand

def display_hand(hand):
    _value = 0
    _hand = []
    for card in hand:
        _name = list(card.keys())[0]
        _total = card[_name]
        if _total != 11:
            _hand.append(_name)
            _value += _total
    for card in hand:
        _name = list(card.keys())[0]
        _total = card[_name]
        if _total == 11:
            _hand.append(_name)
            _value += _total
            if _value > 21:
                _value -= 10
    return (_hand,_value)

def deal_new():
    player = []
    dealer = []
    turn_order = [player,dealer]
    deck = create_deck()
    shuffle_deck(deck)
    for num in range(2):
        for person in turn_order:
            person = draw_card(person, deck)
    return deck, player, dealer

def blackjack():
    print(art.logo)
    deck, player, dealer = deal_new()
    handPlayer, valuePlayer = display_hand(player)
    handDealer, valueDealer = display_hand(dealer)
    print(f'    Your cards:{handPlayer}, current score: {valuePlayer}')
    print(f'    Dealer\'s first card: {handDealer[0]}')
    if valueDealer == 21:
        handPlayer, playerValue = display_hand(player)
        handDealer, dealerValue = display_hand(dealer)
        print(f"    Your final cards:{handPlayer}, final score: {playerValue}")
        print(f"    Dealer's final hand: {handDealer}, final score {dealerValue}")
        print("Dealer has BLACKJACK!!")
        print('You lose')
        game_on()
    hit = 'y'
    while True:
        if hit == 'y':
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            hit = hit.lower()[0]
        if hit == 'y':
            player = draw_card(player, deck)
            handPlayer, valuePlayer = display_hand(player)
            print(f'    Your cards:{handPlayer}, current score: {valuePlayer}')
            print(f'    Dealer\'s first card: {handDealer[0]}')
        check_state(player, dealer, hit)
        handDealer, valueDealer, dealer = dealer_turn(dealer, deck)
        check_state(player, dealer, hit)

def game_on():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    choice = choice.lower()[0]
    if choice == 'y':
        clear()
        blackjack()
    else:
        exit()
        
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
            
def dealer_turn(dealer: list, deck: list):
    hand, value = display_hand(dealer)
    if value <= 16:
        dealer = draw_card(dealer, deck)
    hand, value = display_hand(dealer)
    return hand, value, dealer

def check_state(player, dealer, playerHit):
    handPlayer, playerValue = display_hand(player)
    handDealer, dealerValue = display_hand(dealer)
    final_hands = f"    Your final cards:{handPlayer}, final score: {playerValue}\n    Dealer's final hand: {handDealer}, final score {dealerValue}"
    if playerValue > 21:
        print(final_hands)
        print('You busted!')
        return player_lose()
    elif dealerValue > 21:
        print(final_hands)
        print('Dealer busted!')
        return player_win()
    elif playerHit == 'y' or dealerValue < 17:
        return False
    elif playerValue > dealerValue:
        print(final_hands)
        return player_win()
    elif playerValue < dealerValue:
        print(final_hands)
        return player_lose()
    else:
        print(final_hands)
        print('Tied! Push!')
        return True
    
def player_lose():
    print("You lose")
    game_on()

def player_win():
    print("You win")
    game_on()

card_values = _card_values()

if __name__ == '__main__':
    game_on()

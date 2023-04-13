import art
import random

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

def draw_card(deck):
    return deck.pop()

def display_hand(hand, dealer= False):
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
        print(num)
        for person in turn_order:
            drawn_card = draw_card(deck)
            person.append({drawn_card: card_values[drawn_card]})
    return deck, player, dealer

def blackjack():
    game_on = 'y'
    while game_on == 'y':
        deck, player, dealer = deal_new()
        print(player)
        print(len(player))
        print(display_hand(player))
        game_on = 'n'
        


card_values = _card_values()

# creating a new dictionary
my_dict ={"Java":100, "Python":112, "C":11}

# one-liner
print("One line Code Key value: ", list(my_dict.keys())[list(my_dict.values()).index(100)])


if __name__ == '__main__':
    blackjack()

"""
This is a module for simulating drawing cards. I stole it from a guy named Dave on the internet
"""
# import randint from random
from random import randint

# Define Suits as dictionary
suits = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}

# Define cards as dictionary
cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}


def draw_cards(num_of_cards, list_dealt=[]):
    for z in range(num_of_cards):
        x = randint(0, 3)  # random integer 0 to 3 to pick suit
        y = randint(0, 12)  # random integer 0 to 12 to pick card
        mycard = "{0} of {1}".format(cards[y], suits[x])
        if mycard not in list_dealt:
            list_dealt.append(mycard)
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards, list_dealt)

    return list_dealt


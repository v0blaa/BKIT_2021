from card import Card

clubs_suit = 'Пики'
diamonds_suit = 'Буби'
hearts_suit = 'Черви'
spades_suit = 'Крести'

suits = [clubs_suit, diamonds_suit, hearts_suit, spades_suit]

a_number = 'Туз'
second_number = '2'
third_number = '3'
fourth_number = '4'
fifth_number = '5'
sixth_number = '6'
seventh_number = '7'
eleventh_number = '8'
nineth_number = '9'
tenth_number = '10'
king_number = 'Король'
lady_number = 'Дама'
jack_number = 'Валет'

numbers = [a_number,
           second_number,
           third_number,
           fourth_number,
           fifth_number,
           sixth_number,
           seventh_number,
           eleventh_number,
           nineth_number,
           tenth_number,
           king_number,
           lady_number,
           jack_number]

weights = {
    a_number: 11,
    second_number: 2,
    third_number: 3,
    fourth_number: 4,
    fifth_number: 5,
    sixth_number: 6,
    seventh_number: 7,
    eleventh_number: 8,
    nineth_number: 9,
    tenth_number: 10,
    king_number: 6,
    lady_number: 4,
    jack_number: 2
}

def create_cards():
    cards = {}
    for suit in suits:
        for number in numbers:
            card = Card(suit, number, weights[number])
            cards[card.id] = card
    return cards

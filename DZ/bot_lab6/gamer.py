MAX_CARD_COUNT = 5

class Gamer:
    def __init__(self):
        self.cards = []

    def print_cards(self):
        string = ''
        number = 0
        for card in self.cards:
            number += 1
            string += str(number) + ": " + card.print_card_name() + "\n"
        return string

    def add_new_card(self, card):
        self.cards.append(card)

    def sum(self):
        sum = 0
        for card in self.cards:
            sum += card.weight
        return sum

#bot = Gamer()
#client = Gamer()

#bot.add_new_card()
#client.add_new_card(Card(clubs_suit, a_number, weights[a_number]))
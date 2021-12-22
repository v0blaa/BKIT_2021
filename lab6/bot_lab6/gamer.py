MAX_CARD_COUNT = 5

class Gamer:
    def __init__(self):
        self.cards = []

    def print_cards(self, **args):
        string = ''
        number = 0
        mode = args.get('first_card')
        if mode:
            string += "1: " + self.cards[0].print_card_name() + "\n"
            return string
        for card in self.cards:
            number += 1
            string += str(number) + ": " + card.print_card_name() + "\n"
        return string
        # dirs = []
        # for card in self.cards:
        #     dirs.append(card.dir_to_card_picture())
        # return dirs

    def add_new_card(self, card):
        if self.count_cards() < 5:
            self.cards.append(card)

    def sum(self):
        sum = 0
        for card in self.cards:
            sum += card.weight
        return sum

    def count_cards(self):
        return len(self.cards)

#bot = Gamer()
#client = Gamer()

#bot.add_new_card()
#client.add_new_card(Card(clubs_suit, a_number, weights[a_number]))
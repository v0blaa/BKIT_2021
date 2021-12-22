from gamer import Gamer
from create_cards import create_cards
import random

class Game:
    def __init__(self):
        self.all_cards = create_cards()
        self.bot = Gamer()
        self.client = Gamer()
        self.init_first_cards()

    def get_available_cards(self):
        cards_map = self.all_cards.copy()
        for card in self.bot.cards:
            del cards_map[card.id]
        for card in self.client.cards:
            del cards_map[card.id]
        return cards_map


    def init_first_cards(self):
        for i in range(0, 2):
            available_cards = self.get_available_cards()
            available_cards_keys = list(available_cards.keys())
            rand_id = random.choice(available_cards_keys)
            self.bot.add_new_card(available_cards[rand_id])

        for i in range(0, 2):
            available_cards = self.get_available_cards()
            available_cards_keys = list(available_cards.keys())
            rand_id = random.choice(available_cards_keys)
            self.client.add_new_card(available_cards[rand_id])

    def add_new_cards_to_bot(self):
        available_cards = self.get_available_cards()
        available_cards_keys = list(available_cards.keys())
        rand_id = random.choice(available_cards_keys)
        self.bot.add_new_card(available_cards[rand_id])

    def add_new_cards_to_client(self):
        available_cards = self.get_available_cards()
        available_cards_keys = list(available_cards.keys())
        rand_id = random.choice(available_cards_keys)
        self.client.add_new_card(available_cards[rand_id])


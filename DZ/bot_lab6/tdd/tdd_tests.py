import unittest
from gamer import Gamer
from card import Card
from tdd.check_for_testing import check_finish


class TestStreetsAndHouses(unittest.TestCase):

    def test_add_new_card(self):
        gamer_for_tests = Gamer()
        gamer_for_tests.add_new_card(Card("Clubs", "king", 6))
        expected_result = "1: Clubs king\n"
        self.assertEqual(expected_result,gamer_for_tests.print_cards())

    def test_count_sum(self):
        gamer_for_tests = Gamer()
        gamer_for_tests.add_new_card(Card("Clubs", "king", 6))
        gamer_for_tests.add_new_card(Card("Diamonds", "king", 6))
        gamer_for_tests.add_new_card(Card("Hearts", "king", 6))
        expected_result = 18
        self.assertEqual(expected_result, gamer_for_tests.sum())


    def test_check_finish_with_winner(self):
        player1 = Gamer()
        player2 = Gamer()

        player1.add_new_card(Card("Clubs", "a", 11))
        player1.add_new_card(Card("Hearts", "10", 10))

        player2.add_new_card(Card("Hearts", "2", 2))
        player2.add_new_card(Card("Diamonds", "king", 6))
        expected_result = 'player1'
        self.assertEqual(expected_result, check_finish(player1, player2))


    def test_check_finish_no_winner(self):
        player1 = Gamer()
        player2 = Gamer()

        player1.add_new_card(Card("Clubs", "2", 2))
        player1.add_new_card(Card("Hearts", "10", 10))

        player2.add_new_card(Card("Hearts", "2", 2))
        player2.add_new_card(Card("Diamonds", "king", 6))
        expected_result = None
        self.assertEqual(expected_result, check_finish(player1, player2))


if __name__ == "__main__":
    unittest.main()


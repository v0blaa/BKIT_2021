from behave import *
from gamer import Gamer
from card import Card
from tdd.check_for_testing import check_finish

@given('player1 cards: 2 clubs, 10 hearts; player2 cards: 2 hearts, king diamonds')
def step_impl(context):
    context.player1 = Gamer()
    context.player2 = Gamer()

    context.player1.add_new_card(Card("Clubs", "2", 2))
    context.player1.add_new_card(Card("Hearts", "10", 10))

    context.player2.add_new_card(Card("Hearts", "2", 2))
    context.player2.add_new_card(Card("Diamonds", "king", 6))
    pass

@when('check_finish run')
def step_impl(context):
    context.winner = check_finish(context.player1, context.player2)
    pass

@then('there is no winner')
def step_impl(context):
    assert context.winner == None




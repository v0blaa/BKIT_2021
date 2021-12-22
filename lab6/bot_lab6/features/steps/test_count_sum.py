from behave import *
from gamer import Gamer
from card import Card

@given('gamer has no cards_')
def step_impl(context):
    context.gamer = Gamer()
    pass

@when('gamer gets clubs king, diamonds king, hearts king')
def step_impl(context):
    context.gamer.add_new_card(Card("Clubs", "king", 6))
    context.gamer.add_new_card(Card("Diamonds", "king", 6))
    context.gamer.add_new_card(Card("Hearts", "king", 6))
    pass

@then('the sum is 18')
def step_impl(context):
    assert context.gamer.sum() == 18




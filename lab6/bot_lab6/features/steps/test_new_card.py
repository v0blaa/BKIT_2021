from behave import *
from gamer import Gamer
from card import Card

@given('gamer has no cards')
def step_impl(context):
    context.gamer = Gamer()
    pass

@when('gamer gets clubs king')
def step_impl(context):
    context.gamer.add_new_card(Card("Clubs", "king", 6))
    pass

@then('gamers cards are: clubs king')
def step_impl(context):
    assert context.gamer.print_cards() == "1: Clubs king\n"




from behave import *
from get_roots import get_roots

@given('A = 1, B = 2, C = 3')
def step_impl(context):
    context.A = 1
    context.B = 2
    context.C = 3
    pass

@when('get_roots run')
def step_impl(context):
    context.array_len = len(get_roots(context.A, context.B, context.C))
    pass

@then('roots array is empty')
def step_impl(context):
    assert context.array_len is 0




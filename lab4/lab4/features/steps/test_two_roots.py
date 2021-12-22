from behave import *
from get_roots import get_roots

@given('A = 1, B = -2, C = -8')
def step_impl(context):
    context.A = 1
    context.B = -2
    context.C = -8
    pass

@when('get_roots execute2')
def step_impl(context):
    context.roots = get_roots(context.A, context.B, context.C)
    pass

@then('roots are [-2, 2]')
def step_impl(context):
    assert len(context.roots) == 2
    assert -2 in context.roots
    assert 2 in context.roots
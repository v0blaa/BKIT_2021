from behave import *
from get_roots import get_roots

@given('A = 4, B = -5, C = 1')
def step_impl(context):
    context.A = 4
    context.B = -5
    context.C = 1
    pass

@when('get_roots execute4')
def step_impl(context):
    context.roots = get_roots(context.A, context.B, context.C)
    pass

@then('roots are [-1, 1, 0.5, -0,5]')
def step_impl(context):
    assert len(context.roots) == 4
    assert -1 in context.roots
    assert 1 in context.roots
    assert 0.5 in context.roots
    assert -0.5 in context.roots

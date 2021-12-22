from behave import *
from get_roots import get_roots

@given('A = 1, B = -1, C = 0')
def step_impl(context):
    context.A = 1
    context.B = -1
    context.C = 0
    pass

@when('get_roots execute3')
def step_impl(context):
    context.roots = get_roots(context.A, context.B, context.C)
    pass

@then('roots are [-1, 0, 1]')
def step_impl(context):
    assert len(context.roots) == 3
    assert -1 in context.roots
    assert 0 in context.roots
    assert 1 in context.roots
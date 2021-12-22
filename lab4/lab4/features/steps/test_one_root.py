from behave import *
from get_roots import get_roots

@given('A = 1, B = 1, C = 0')
def step_impl(context):
    context.A = 1
    context.B = 1
    context.C = 0
    pass

@when('get_roots execute1')
def step_impl(context):
    context.roots = get_roots(context.A, context.B, context.C)
    pass

@then('roots is [0]')
def step_impl(context):
    assert len(context.roots) == 1
    assert context.roots[0] == 0
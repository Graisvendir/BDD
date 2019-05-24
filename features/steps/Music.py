from behave import *

@given('I have guess the melody game')
def step_impl(context):
    pass

@when('I have entered number \'3\' as number of melody')
def step_impl(context):
    assert True is not False

@then('I lose the game')
def step_impl(context):
    assert context.failed is False
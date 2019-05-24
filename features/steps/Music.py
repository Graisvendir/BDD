from behave import *
from pool import Pool

pool = None
choice = None


@given('I have guess the music game')
def step_impl(context):
    global pool
    pool = Pool()

@given('I have one music in variants')
def step_impl(context):
    global pool
    pool.add_variant('AC/DC - Back In Black')

@when('I have entered number \'3\' as number of melody')
def step_impl(context):
    global choice
    choice = 3

@then('I lose the game')
def step_impl(context):
    global pool
    global choice
    assert pool.check_choice(choice) is 0
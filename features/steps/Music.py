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

@given('I have current music')
def step_impl(context):
    global pool
    pool.set_random_current_music()

@when('I have entered number \'3\' as number of melody')
def step_impl(context):
    global choice
    choice = 3

@when('I have entered number \'1\' as number of melody')
def step_impl(context):
    global choice
    choice = 1

@then('I lose the game')
def step_impl(context):
    global pool
    global choice
    assert pool.check_choice(choice) is 0

@then('I win the game')
def step_impl(context):
    global pool
    global choice
    assert pool.check_choice(choice) is 1
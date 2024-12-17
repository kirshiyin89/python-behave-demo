from behave import given, when, then
from assertpy import assert_that
from password_reset_system import PasswordResetSystem  # Importing the real class

# Initialize the system instance
system = PasswordResetSystem()

@given('the user is on the "Forgot Password" page')
def step_given_user_on_forgot_password_page(context):
    # In a real test, this might interact with a web page.
    context.page = "Forgot Password"
    context.system = system  # Assign the system object to context for use in other steps

@when('the user submits a valid email "{email}"')
def step_when_user_submits_valid_email(context, email):
    context.response = context.system.reset_password(email)

@when('the user submits an invalid email "{email}"')
def step_when_user_submits_invalid_email(context, email):
    context.response = context.system.reset_password(email)

@then('the system sends a password reset link to "{email}"')
def step_then_system_sends_reset_link(context, email):
    assert_that(context.response).is_equal_to(f"Password reset link sent to {email}")

@then('the system shows an error message "{message}"')
def step_then_system_shows_error_message(context, message):
    assert_that(context.response).is_equal_to(message)

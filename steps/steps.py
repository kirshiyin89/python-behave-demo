from behave import given, when, then
from password_reset_system import PasswordResetSystem  # Importing the real class

# Initialize the system instance
system = PasswordResetSystem()

@given('the user is on the "Forgot Password" page')
def step_given_user_on_forgot_password_page(context):
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
    assert context.response == f"Password reset link sent to {email}", f"Expected reset link for {email}, got {context.response}"

@then('the system shows an error message "{message}"')
def step_then_system_shows_error_message(context, message):
    assert context.response == message, f"Expected error message '{message}', got {context.response}"

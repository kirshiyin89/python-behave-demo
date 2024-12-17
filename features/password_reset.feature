Feature: Password Reset

  In order to regain access to my account
  As a registered user
  I want to be able to reset my password via email

  Scenario: User submits a valid email for password reset
    Given the user is on the "Forgot Password" page
    When the user submits a valid email "user@example.com"
    Then the system sends a password reset link to "user@example.com"

  Scenario: User submits an invalid email for password reset
    Given the user is on the "Forgot Password" page
    When the user submits an invalid email "invalid_email"
    Then the system shows an error message "Please enter a valid email address"

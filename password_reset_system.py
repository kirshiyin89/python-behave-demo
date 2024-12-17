class PasswordResetSystem:
    def __init__(self):
        self.valid_emails = []  # Store valid emails for testing purposes
    
    def add_valid_email(self, email):
        """Method to add valid email addresses."""
        if self.is_valid_email(email):
            self.valid_emails.append(email)
        else:
            raise ValueError(f"Invalid email format: {email}")

    def reset_password(self, email):
        """Simulate the password reset request."""
        if self.is_valid_email(email):
            return f"Password reset link sent to {email}"
        else:
            return "Please enter a valid email address"

    def is_valid_email(self, email):
        """Helper method to check if email is in valid format."""
        return "@" in email and "." in email  # Very basic email validation

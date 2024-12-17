from password_reset_system import PasswordResetSystem

def main():
    # Create an instance of the PasswordResetSystem
    system = PasswordResetSystem()

    # Example of adding a valid email (you can simulate this)
    try:
        system.add_valid_email("user@example.com")
        print("Valid email added!")
    except ValueError as e:
        print(e)

    # Simulate a password reset request with a valid email
    response = system.reset_password("user@example.com")
    print(response)  # Output: Password reset link sent to user@example.com

    # Simulate a password reset request with an invalid email
    response = system.reset_password("invalid_email")
    print(response)  # Output: Please enter a valid email address

if __name__ == "__main__":
    main()

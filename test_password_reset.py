import unittest
from password_reset_system import PasswordResetSystem  # Assuming the class is in this file

class TestPasswordResetSystem(unittest.TestCase):
    def setUp(self):
        """Setup before each test."""
        self.system = PasswordResetSystem()

    def test_valid_email(self):
        """Test valid email for password reset."""
        result = self.system.reset_password("user@example.com")
        self.assertEqual(result, "Password reset link sent to user@example.com")

    def test_invalid_email(self):
        """Test invalid email for password reset."""
        result = self.system.reset_password("invalid_email")
        self.assertEqual(result, "Please enter a valid email address")

    def test_add_valid_email(self):
        """Test adding a valid email."""
        self.system.add_valid_email("newuser@example.com")
        self.assertIn("newuser@example.com", self.system.valid_emails)

    def test_add_invalid_email(self):
        """Test adding an invalid email."""
        with self.assertRaises(ValueError):
            self.system.add_valid_email("invalid_email")

if __name__ == "__main__":
    unittest.main()


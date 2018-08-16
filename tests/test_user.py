import json
from tests.base import BaseTestCase

class TestUserAuth(BaseTestCase):

    def test_if_json_data(self):
        """
            Test for json data
        """
        with self.client:
            response = self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.assertTrue(response.content_type == 'application/json')

    def test_successful_signup(self):
        """
            Test for successful user signup
        """
        with self.client:
            response = self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.assertEqual(response.status_code, 201)

    def test_signup_with_esisting_email(self):
        """
            Tests if User is Registering with an already used email
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.register_user("boolean", "sue@gmail.com", "bootcamp12")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "Email already in use")
            
    def test_existing_user(self):
        """
            Tests for no duplicate user
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "User already exists")

    def test_valid_email(self):
        """
            Test for valid email entry
        """
        with self.client:
            self.assertRaises(
                ValueError, lambda: self.register_user("sue", "suegmail.com", "Bootcamp11")
            )
    def test_empty_email_field(self):
        """
            Test for empty email field
        """
        with self.client:
            self.assertRaises(
                Exception, lambda: self.register_user("sue", "", "Bootcamp11")
            )
    def test_invalid_password(self):
        """
            Test for valid password
        """
        with self.client:
            self.assertRaises(
                Exception, lambda: self.register_user("sue", "sue@gmail.com", "boo")
            )
    
    def test_empty_password_field(self):
        """
            Test for password not provided
        """
        with self.client:
            self.assertRaises(
                Exception, lambda: self.register_user("sue", "sue@gmail.com", "")
            )
    
    def test_invalid_user_name_length(self):
        """
            Test for invalid name length
        """
        with self.client:
            self.assertRaises(
                Exception, lambda: self.register_user("su", "sue@gmail.com", "Bootcamp11")
            )
    
    def test_invalid_name(self):
        """
            Test for invalid characters 
            in the neme after compilation
        """
        with self.client:
            self.assertRaises(
                ValueError, lambda: self.register_user("!@#", "sue@gmail.com", "Bootcamp11")
            )

    def test_empty_user_name_field(self):
        """
            Test for empty username field
        """
        with self.client:
            self.assertRaises(
                Exception, lambda: self.register_user("", "sue@gmail.com", "Bootcamp11")
            )

import sys
import unittest

from user import User


class Usertest(unittest.TestCase):
    """
        Class containing all the test in class user
    """

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newUser = User()

    def test_create_account(self):
        """defining method to test for creating user account"""
        self.newUser.users = {}
        current_count = len(self.newUser.users)
        result = self.newUser.register( 'eunice@gmail.com', 'eunice', 'pass', 'pass')
        self.assertEqual(7, result, "User succesfully created")   

    def test_register_null_name(self):
        """defining method to test for creating user account with an empty name field"""
        output=self.newUser.register('eunice@gmail.com', '', 'pass','pass')
        self.assertEqual(8, output, "Please fill your name")

    def test_register_null_username(self):
        """defining method to test for created user account with an empty username field"""
        output=self.newUser.register('eunice@gmail.com', '', 'pass','pass')    
        self.assertEqual(8, output, "Username is empty")

    def test_register_null_email(self):
        """defining method to test for creating user account with an empty email"""
        output=self.newUser.register('', 'eunice','pass','pass')
        self.assertEqual(6, output, "Email is Empty ")    
        
    def test_null_password(self):
        """ defining method to test for creating user account with an empty passsword field"""
        output=self.newUser.register('eunice@gmail.com','eunice',  '','pass')
        self.assertEqual(6, output, "Please the password filed") 
 
    def test_cpassword_is_password(self):
        """defining method to test for created user's password is equal to confirm password"""
        output=self.newUser.register('eunice@gmail.com', 'eunice', 'pass','pas')    
        self.assertEqual(3, output, "password mismatch")

    def test_existing_useremail(self):
        """defining method to test for an existing user email """
        self.newUser.users = {}
        self.newUser.register('eunice@gmail.com','eunice', 'pass','pass')
        result = self.newUser.register('eunice@gmail.com', 'eunice', 'pass','pass')
        self.assertEqual(7, result, "Email already registered")

    def test_wrong_login_password(self):
        """defining method to test if login password is equal to register passsword"""
        self.newUser.users = {}
        self.newUser.register( 'eunice@gmail.com', 'eunice', 'pass','pass')
        result = self.newUser.login('eunice@gmail.com', 'w3lc0m3')
        self.assertEqual(3, result,"Wrong login credentials") 

    def test_wrong_login_email(self):
        """defining method to test if login email is equal to register email"""
        self.newUser.users = {}
        self.newUser.register('eunice@gmail.com', 'eunice', 'pass','pass')
        result = self.newUser.login('eunicewoth@gmail.com', 'pass')
        self.assertEqual(3, result, "wrong login credentials") 

    def test_login_null_email(self):
        """defining method to test for null login email"""
        result = self.newUser.login('', 'pass')
        self.assertEqual(4, result, "Please fill the email field")   

    def test_login_null_password(self):
        """defining method to test for null login password"""
        result = self.newUser.login('eunice@gmail.com', '')
        self.assertEqual(4, result, "Please fill the password field") 
    
		
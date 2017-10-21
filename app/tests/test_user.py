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

    
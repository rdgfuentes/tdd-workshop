import unittest
from src.user import User
from src.spotipy import Spotipy
from src.custom_exceptions.not_available_email import NotAvailableEmail


class UserRegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.__spotipy = Spotipy()

        user_email = "jose_perez@gmail.com"
        user_first_name = "Jose"
        user_last_name = "Perez"

        self.__new_user_pepe = User(user_email, user_first_name, user_last_name)

    def test_user_without_account_signup_with_available_email(self):
        self.__spotipy.register_user(self.__new_user_pepe)
        response = self.__spotipy.is_registered(self.__new_user_pepe)

        self.assertTrue(response)

    def test_register_user_with_non_available_email_throws_exception(self):
        self.__spotipy.register_user(self.__new_user_pepe)
        user_registration = lambda: self.__spotipy.register_user(self.__new_user_pepe)
        self.assertRaises( NotAvailableEmail, user_registration )


if __name__ == "__main__":
    unittest.main()

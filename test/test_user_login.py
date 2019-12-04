import unittest
from src.user import User
from src.spotipy import Spotipy


class UserLoginTestCase(unittest.TestCase):

    def setUp(self):
        self.__spotipy = Spotipy()

        user_email = "jose_perez@gmail.com"
        user_first_name = "Jose"
        user_last_name = "Perez"
        user_password = "12345678"

        self.__valid_user = User(user_email, user_first_name, user_last_name, user_password,)
        self.__spotipy.register_user(self.__valid_user)

    def test_user_login_successfully(self):
        response = self.__spotipy.user_login(self.__valid_user.email, self.__valid_user.password)
        self.assertTrue(response)

    def test_unregistered_user_can_not_login(self):
        response = self.__spotipy.user_login("john@doe.com", self.__valid_user.password)
        self.assertFalse(response)

    def test_registered_user_with_indalid_password_can_not_login(self):
        response = self.__spotipy.user_login(self.__valid_user.email, "qwerty")
        self.assertFalse(response)
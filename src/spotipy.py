from src.custom_exceptions.not_available_email import NotAvailableEmail

class Spotipy:

    def __init__(self):
        self.__users = []

    def register_user(self, user):
        if self.__is_available_email(user.email):
            self.__users.append(user)
        else:
            raise NotAvailableEmail
    
    def __get_users_by_email(self, email):
        return list(filter(lambda u: u.email == email, self.__users))

    def __is_available_email(self, email):
        existing = self.__get_users_by_email(email)
        return len(existing) == 0

    def is_registered(self, user):
        return not self.__is_available_email(user.email)

    def user_login(self, email, password):
        users = self.__get_users_by_email(email)
        if len(users) == 0:
            return False
        
        return users[0].is_valid_password(password)




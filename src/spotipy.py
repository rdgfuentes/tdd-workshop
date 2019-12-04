from src.custom_exceptions.not_available_email import NotAvailableEmail

class Spotipy:

    def __init__(self):
        self.__users = []

    def register_user(self, user):
        if self.__is_available_email(user.email):
            self.__users.append(user)
        else:
            raise NotAvailableEmail
    
    def __is_available_email(self, email):
        existing =  list(filter(lambda u: u.email == email, self.__users))
        return len(existing) == 0

    def is_registered(self, user):
        return not self.__is_available_email(user.email)




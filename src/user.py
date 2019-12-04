

class User(object):

    def __init__(self, email, first_name, last_name, password=None):
        #  store them as private variables
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name
        
    def is_valid_password(self, password):
        return password == self.__password


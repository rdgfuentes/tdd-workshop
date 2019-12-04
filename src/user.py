

class User(object):

    def __init__(self, email, first_name, last_name):
        #  store them as private variables
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name
        



import requests


class User:
    def __init__(self, f="", i="", l="", p=""):
        self.__data = requests.get(
            "https://api.randomdatatools.ru/").json()
        self.imya = self.__data["FirstName"] if not i else i
        self.familiya = ["LastName"] if not f else f
        self.login = ["Login"] if not l else l
        self.__password = ["Password"] if not p else p

    def log_in(self):
        if self.login == i and self.__password == p:
            return True

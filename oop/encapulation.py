
class Account:
    def __init__(self, name, account_number):
        self.__name = name
        self._account_number = account_number
    
    @property
    def name(self):
        return self.__namep

    def give_name(self):
        return self.__name

nibl = Account("tEST", "123-344-56")
print(nibl.give_name())
print(nibl.name)
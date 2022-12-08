class RejestrKont():
    konta_osobiste = []

    @classmethod
    def addUser(cls, user):
        cls.konta_osobiste.insert(0, user)

    @classmethod
    def searchUserbyPesel(cls, pesel):
        for user in cls.konta_osobiste:
            if user.pesel == pesel:
                return user
        return None

    @classmethod
    def usersCount(cls):
        return len(cls.konta_osobiste)

    @classmethod
    def updateUser(cls, pesel, data_to_update):
        for key in data_to_update:
            if key == "pesel":
                return "You cannot change pesel!"
        if cls.searchUserbyPesel(pesel) != None:
            user_to_update = cls.searchUserbyPesel(pesel)
            for konto in cls.konta_osobiste:
                if user_to_update == konto:
                    for key in data_to_update:
                        if key == "imie":
                            konto.imie = data_to_update[key]
                        if key == "nazwisko":
                            konto.nazwisko = data_to_update[key]
                        if key == "saldo":
                            konto.saldo = data_to_update[key]
                    return konto
        else:
            return None

    @classmethod
    def deleteUser(cls, pesel):
        if cls.searchUserbyPesel(pesel) != None:
            for user in cls.konta_osobiste:
                if user.pesel == pesel:
                    cls.konta_osobiste.remove(user)
                    return "User has been deleted"
        else:
            return None

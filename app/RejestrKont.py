class RejestrKont():
    konta_osobiste = []

    @classmethod
    def addUser(cls, user):
        cls.konta_osobiste.insert(0, user)

    @classmethod
    def searchUserbyPesel(cls, pesel):
        user = filter(lambda x: x.pesel == pesel, cls.konta_osobiste)
        return user

    @classmethod
    def usersCount(cls):
        return len(cls.konta_osobiste)

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

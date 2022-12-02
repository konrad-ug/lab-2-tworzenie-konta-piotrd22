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
        if cls.searchUserbyPesel(pesel) != None:
            for key in data_to_update:
                if key == "pesel":
                    return "You cannot update PESEL"
            user_to_update = cls.searchUserbyPesel(pesel)
            for user in cls.konta_osobiste:
                if user_to_update == user:
                    for key in data_to_update:
                        user_to_update.key = data_to_update[key]
                    return user_to_update
        else:
            return None

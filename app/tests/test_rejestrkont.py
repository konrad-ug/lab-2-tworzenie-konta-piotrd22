import unittest
from app.KontoOsobiste import KontoOsobiste
from app.RejestrKont import RejestrKont


class TestRegister(unittest.TestCase):

    name = "Marek"
    surname = "Papszun"
    pesel = "02225432100"

    @classmethod
    def setUpClass(cls):
        user = KontoOsobiste(cls.name, cls.surname, cls.pesel)
        RejestrKont.addUser(user)

    def test_1_add_first_user(self):
        self.assertEqual(RejestrKont.usersCount(), 1)

    def test_2_add_second_user(self):
        user = KontoOsobiste(self.name + "as", self.surname, "03225432100")
        RejestrKont.addUser(user)
        self.assertEqual(RejestrKont.usersCount(), 2)

    def test_searchUserbyPesel(self):
        self.assertEqual(RejestrKont.searchUserbyPesel(
            "02225432100").imie, "Marek")
        self.assertEqual(RejestrKont.searchUserbyPesel(
            "03225432100").imie, "Marekas")
        self.assertEqual(RejestrKont.searchUserbyPesel("1234567890"), None)

    def test_updateUser(self):
        body_to_update = {
            "imie": "anakin",
            "nazwisko": "skywalker",
            "saldo": 1
        }

        wrong_body = {
            "pesel": "0212345678"
        }

        self.assertEqual(RejestrKont.updateUser(
            self.pesel, body_to_update).imie, RejestrKont.searchUserbyPesel(self.pesel).imie)
        self.assertEqual(RejestrKont.updateUser(
            self.pesel, body_to_update).nazwisko, RejestrKont.searchUserbyPesel(self.pesel).nazwisko)
        self.assertEqual(RejestrKont.updateUser(
            self.pesel, body_to_update).saldo, RejestrKont.searchUserbyPesel(self.pesel).saldo)
        self.assertEqual(RejestrKont.updateUser(
            "1234567890", body_to_update), RejestrKont.searchUserbyPesel("1234567890"))  # NONE
        self.assertEqual(RejestrKont.updateUser(
            self.pesel, wrong_body), "You cannot change pesel!")

    def test_deleteUser(self):
        user = KontoOsobiste(self.name + "po", self.surname, "03225432101")
        RejestrKont.addUser(user)

        length = RejestrKont.usersCount()

        self.assertEqual(RejestrKont.deleteUser(
            "03225432101"), "User has been deleted")
        self.assertEqual(RejestrKont.usersCount(), length - 1)
        self.assertEqual(RejestrKont.deleteUser("1234567890"), None)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta_osobiste = []

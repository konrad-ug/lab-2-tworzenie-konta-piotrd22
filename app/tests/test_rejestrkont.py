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

    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta_osobiste = []

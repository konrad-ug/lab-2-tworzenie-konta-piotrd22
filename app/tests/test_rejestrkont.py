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
        user = KontoOsobiste(self.name, self.surname, self.pesel)
        RejestrKont.addUser(user)
        self.assertEqual(RejestrKont.usersCount(), 2)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta_osobiste = []

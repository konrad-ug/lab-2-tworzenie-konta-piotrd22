import unittest

from app.Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678900")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "12345678900", "PESEL nie został zapisany")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprwany pesel")

        # drugie_konto = Konto("Marek", "Papszun", "98765432100", "PROM_XYZ")
        # self.assertEqual(drugie_konto.saldo, 50, "Niepoprwany kod promocyjny")


    #tutaj proszę dodawać nowe testy
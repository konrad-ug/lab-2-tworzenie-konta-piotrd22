import unittest

from app.Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678900")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")

        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        #PESEL testing
        self.assertEqual(pierwsze_konto.pesel, "12345678900", "PESEL nie został zapisany")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprwany pesel")

        #Checking if valid promo code add 50 to saldo
        drugie_konto = Konto("Marek", "Papszun", "98765432100", "PROM_xyz")
        self.assertEqual(drugie_konto.saldo, 50, "Niepoprwany kod promocyjny")

        #Checking if invalid promo code add nothing
        trzecie_konto = Konto("Marek", "Papszun", "98765678910", "PORN_xyz")
        self.assertEqual(trzecie_konto.saldo, 0, "Niepoprwany kod promocyjny")
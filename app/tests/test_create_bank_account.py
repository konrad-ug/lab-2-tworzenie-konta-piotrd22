import unittest

from app.Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12225678900")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")

        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        #valid PESEL testing
        self.assertEqual(pierwsze_konto.pesel, "12225678900", "PESEL nie został zapisany")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprwany pesel")

        #invalid PESEL testing
        szoste_konto = Konto("Dariusz", "Januszewski", "122256789ab")
        self.assertEqual(szoste_konto.pesel, "Niepoprawny pesel!", "Pesel nie ma wartości \"Niepoprawny pesel!"" jeżeli jest zły")

        #Checking if valid promo code add 50 to saldo
        drugie_konto = Konto("Marek", "Papszun", "98265432100", "PROM_xyz")
        self.assertEqual(drugie_konto.saldo, 50, "Niepoprawny kod promocyjny")

        #Checking if invalid promo code add nothing
        trzecie_konto = Konto("Marek", "Papszun", "98265678910", "PORN_xyz")
        self.assertEqual(trzecie_konto.saldo, 0, "Saldo powinno równać się 0 po zaaplikowaniu złego kodu")

        #Checking valid promo code for too old person
        czwarte_konto = Konto("Marek", "Papszun", "59025432100", "PROM_xyz")
        self.assertEqual(czwarte_konto.saldo, 0, "Kod nie powinien być ważny dla osób przed 1960r.!")

        #Checking valid promo code to valid person
        piate_konto = Konto("Marek", "Papszun", "02225432100", "PROM_xyz")
        self.assertEqual(piate_konto.saldo, 50, "Kod powinien być ważny dla osób po 1960r.!")

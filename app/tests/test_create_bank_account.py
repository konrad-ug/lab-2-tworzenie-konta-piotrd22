import unittest

from app.KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste("Dariusz", "Januszewski", "12225678900")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")

        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_valid_PESEL(self):
        pierwsze_konto = KontoOsobiste("Dariusz", "Januszewski", "12225678900")
        self.assertEqual(pierwsze_konto.pesel, "12225678900", "PESEL nie został zapisany")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprwany pesel")

    def test_invalid_PESEL(self):
        szoste_konto = KontoOsobiste("Dariusz", "Januszewski", "122256789ab")
        self.assertEqual(szoste_konto.pesel, "Niepoprawny pesel!", "Pesel nie ma wartości \"Niepoprawny pesel!"" jeżeli jest zły")

    def test_if_valid_promocode_add50(self):
        drugie_konto = KontoOsobiste("Marek", "Papszun", "98265432100", "PROM_xyz")
        self.assertEqual(drugie_konto.saldo, 50, "Niepoprawny kod promocyjny")

    def test_if_invalid_promocode_addnothing(self):
        trzecie_konto = KontoOsobiste("Marek", "Papszun", "98265678910", "PORN_xyz")
        self.assertEqual(trzecie_konto.saldo, 0, "Saldo powinno równać się 0 po zaaplikowaniu złego kodu")

    def test_promocode_to_too_old_person(self):
        czwarte_konto = KontoOsobiste("Marek", "Papszun", "59025432100", "PROM_xyz")
        self.assertEqual(czwarte_konto.saldo, 0, "Kod nie powinien być ważny dla osób przed 1960r.!")

    def test_promocode_to_proper_person(self):
        piate_konto = KontoOsobiste("Marek", "Papszun", "02225432100", "PROM_xyz")
        self.assertEqual(piate_konto.saldo, 50, "Kod powinien być ważny dla osób po 1960r.!")
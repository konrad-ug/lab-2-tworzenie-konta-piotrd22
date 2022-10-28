import unittest

from app.KontoFirmowe import KontoFirmowe

class TestKotoFirmowe(unittest.TestCase):
    nazwa = "POLPLEX"
    NIP = "1234567890"
    invalid_nip = "123456789"
    invalid_nip2 = "123456789a"

    def test_creation(self):
        konto = KontoFirmowe(self.nazwa, self.NIP)
        self.assertEqual(konto.nazwa_firmy, self.nazwa, "Niepoprawna nazwa firmy!")
        self.assertEqual(konto.saldo, 0, "Saldo po zainicjowaniu != 0")
    
    def test_valid_nip(self):
        konto = KontoFirmowe(self.nazwa, self.NIP)
        self.assertEqual(konto.NIP, self.NIP, "Niepoprawnie zapisany NIP!")
    
    def test_invalid_nip(self):
        konto1 = KontoFirmowe(self.nazwa, self.invalid_nip)
        konto2 = KontoFirmowe(self.nazwa, self.invalid_nip2)
        self.assertEqual(konto1.NIP, "Niepoprawny NIP!", "Niepoprawny NIP przechodzi!")
        self.assertEqual(konto2.NIP, "Niepoprawny NIP!", "Niepoprawny NIP przechodzi!")

    def test_transfer_from(self):
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 400
        konto.transfer_from(100)
        self.assertEqual(konto.saldo, 400 + 100, "Niepoprawne księgowanie!")

    def test_transfer_to(self):
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 400
        konto.transfer_to(100)
        self.assertEqual(konto.saldo, 400 - 100, "Niepoprawne księgowanie!")
    
    def test_if_i_have_enough_money(self):
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 200
        konto.transfer_to(300)
        self.assertEqual(konto.saldo, 200, "Konto wykonuje przelew pomimo za małego balansu!")

import unittest

from app.KontoFirmowe import KontoFirmowe
from app.KontoOsobiste import KontoOsobiste

class TestHistory(unittest.TestCase):
    name = "Marek"
    surname = "Papszun"
    pesel = "02225432100"

    def test_combined_transfer(self):
        konto = KontoOsobiste(self.name, self.surname, self.pesel)
        konto.saldo = 400
        konto.transfer_from(100)
        konto.transfer_to(400)
        konto.transfer_to_fast(20)
        self.assertEqual(konto.historia, [-1, -20, -400, 100], "Niepoprawna historia przelewów!")
    
    nazwa = "POLPLEX"
    NIP = "1234567890"

    def test_combined_transfer_company(self):
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 400
        
        konto.transfer_from(100)
        konto.transfer_to(400)
        konto.transfer_to_fast(20)
        self.assertEqual(konto.historia, [-5, -20, -400, 100], "Niepoprawna historia przelewów!")
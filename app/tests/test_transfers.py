import unittest

from app.Konto import Konto

class TestTransfers(unittest.TestCase):
    name = "Marek"
    surname = "Papszun"
    pesel = "02225432100"

    def test_transfer_out(self):
        konto = Konto(self.name, self.surname, self.pesel)
        konto.saldo = 400
        konto.transfer_from(100)
        self.assertEqual(konto.saldo, 400 + 100, "Niepoprawne księgowanie!")

    def test_transfer_to(self):
        konto = Konto(self.name, self.surname, self.pesel)
        konto.saldo = 400
        konto.transfer_to(100)
        self.assertEqual(konto.saldo, 400 - 100, "Niepoprawne księgowanie!")
    
    def test_if_i_have_enough_money(self):
        konto = Konto(self.name, self.surname, self.pesel)
        konto.saldo = 200
        konto.transfer_to(300)
        self.assertEqual(konto.saldo, 200, "Konto wykonuje przelew pomimo za małego balansu!")
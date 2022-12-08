import unittest
from unittest.mock import patch

from app.KontoFirmowe import KontoFirmowe
from app.KontoOsobiste import KontoOsobiste


class TestFastTransfers(unittest.TestCase):
    name = "Marek"
    surname = "Papszun"
    pesel = "02225432100"

    def test_fast_transfer_o(self):
        konto = KontoOsobiste(self.name, self.surname, self.pesel)
        konto.saldo = 400
        konto.transfer_to_fast(100)
        self.assertEqual(konto.saldo, 400 - 100 - 1,
                         "Niepoprawne księgowanie!")

    def test_if_i_have_enough_money_to_fasttransfer_o(self):
        konto = KontoOsobiste(self.name, self.surname, self.pesel)
        konto.saldo = 200
        konto.transfer_to_fast(201)
        self.assertEqual(konto.saldo, 200,
                         "Konto wykonuje przelew pomimo za małego balansu!")

    nazwa = "POLPLEX"
    NIP = "1234567890"

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_real')
    def test_fast_transfer_to_company(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 400
        konto.transfer_to_fast(400)
        self.assertEqual(konto.saldo, 400 - 400 - 5,
                         "Niepoprawne księgowanie!")

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_real')
    def test_if_i_have_enough_money_to_fasttransfer_company(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 200
        konto.transfer_to_fast(201)
        self.assertEqual(konto.saldo, 200,
                         "Konto wykonuje przelew pomimo za małego balansu!")

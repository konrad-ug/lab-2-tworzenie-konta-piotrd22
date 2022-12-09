import unittest
from unittest.mock import patch, Mock

from app.KontoFirmowe import KontoFirmowe


class TestKotoFirmowe(unittest.TestCase):
    nazwa = "POLPLEX"
    NIP = "1234567890"

    def _mock_response(self, status):
        return Mock(status_code=status)

    @patch('requests.get')
    def test_invalid_nip(self, mock_get):
        mock_res = self._mock_response(status=400)
        mock_get.return_value = mock_res
        konto1 = KontoFirmowe(self.nazwa, self.NIP)
        self.assertEqual(konto1.NIP, "Niepoprawny NIP!",
                         "Niepoprawny NIP przechodzi!")

    @patch('requests.get')
    def test_valid_nip(self, mock_get):
        mock_res = self._mock_response(status=200)
        mock_get.return_value = mock_res
        konto = KontoFirmowe(self.nazwa, self.NIP)
        self.assertEqual(konto.NIP, self.NIP, "Niepoprawnie zapisany NIP!")

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_real')
    def test_creation(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe(self.nazwa, self.NIP)
        self.assertEqual(konto.nazwa_firmy, self.nazwa,
                         "Niepoprawna nazwa firmy!")
        self.assertEqual(konto.saldo, 0, "Saldo po zainicjowaniu != 0")

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

from app.KontoFirmowe import KontoFirmowe
from app.KontoOsobiste import KontoOsobiste
from ..SMTP import SMTPConnection


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
        self.assertEqual(
            konto.historia, [-1, -20, -400, 100], "Niepoprawna historia przelewów!")

    def test_success_sending_email_with_history(self):
        konto = KontoOsobiste(self.name, self.surname, self.pesel)
        konto.saldo = 1000

        konto.transfer_from(100)
        konto.transfer_to(400)
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value=True)
        status = konto.wyslij_historie_na_maila("osobiste@wp.pl", smtp)

        self.assertTrue(status)
        smtp.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "osobiste@wp.pl")

    def test_fail_sending_email_with_history(self):
        konto = KontoOsobiste(self.name, self.surname, self.pesel)
        konto.saldo = 1000

        konto.transfer_from(100)
        konto.transfer_to(400)
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value=False)
        status = konto.wyslij_historie_na_maila("osobiste@wp.pl", smtp)

        self.assertFalse(status)
        smtp.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "osobiste@wp.pl")

    nazwa = "POLPLEX"
    NIP = "1234567890"

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_real')
    def test_combined_transfer_company(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 400

        konto.transfer_from(100)
        konto.transfer_to(400)
        konto.transfer_to_fast(20)
        self.assertEqual(
            konto.historia, [-5, -20, -400, 100], "Niepoprawna historia przelewów!")

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_real')
    def test_success_sending_email_with_history_company(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 100

        konto.transfer_to(50)
        konto.transfer_from(50)
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value=True)
        status = konto.wyslij_historie_na_maila("firmowe@wp.pl", smtp)

        self.assertTrue(status)
        smtp.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "firmowe@wp.pl")

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_real')
    def test_fail_sending_email_with_history_company(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe(self.nazwa, self.NIP)
        konto.saldo = 100

        konto.transfer_to(50)
        konto.transfer_from(50)
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value=False)
        status = konto.wyslij_historie_na_maila("firmowe@wp.pl", smtp)

        self.assertFalse(status)
        smtp.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "firmowe@wp.pl")

import unittest
from parameterized import parameterized
from app.KontoFirmowe import KontoFirmowe


class TestCompanyLoan(unittest.TestCase):

    def setUp(self):
        self.konto = KontoFirmowe("POLPLEX", "1234567890")

    @parameterized.expand([
        ([-1775, 500, 100], 1000, 500, True, 1500),
        ([-100, 100], 1000, 500, False, 1000),
        ([100, -1775, 1775], 1001, 500, True, 1501),
        ([-1775], 999, 500, False, 999),
        ([500, 200], 12000, 500, False, 12000),
        ([-1775], 200, 500, False, 200)
    ])
    def test_company_loan(self, historia, saldo, suma, werdykt, saldo_po):
        self.konto.historia = historia
        self.konto.saldo = saldo
        is_loan = self.konto.zaciagnij_kredyt(suma)
        self.assertEqual(is_loan, werdykt)
        self.assertEqual(self.konto.saldo, saldo_po)

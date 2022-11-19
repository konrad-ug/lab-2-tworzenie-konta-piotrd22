import unittest
from parameterized import parameterized
from app.KontoOsobiste import KontoOsobiste


class TestLoan(unittest.TestCase):

    def setUp(self):
        self.konto = KontoOsobiste("Marek", "Papszun", "02225432100")

    @parameterized.expand([
        ([100, 100, 100, 400, 500], 500, True, 500),
        ([-100, 100, 100, -100], 500, False, 0),
        ([100, 100, 200, -100, 500], 500, True, 500),
        ([-100, 100, -100, 100, -500], 500, False, 0),
        ([500, 200], 500, False, 0),
        ([-100], 500, False, 0)
    ])
    def test_loan(self, historia, suma, werdykt, saldo):
        self.konto.historia = historia
        is_loan = self.konto.zaciagnij_kredyt(suma)
        self.assertEqual(is_loan, werdykt)
        self.assertEqual(self.konto.saldo, saldo)

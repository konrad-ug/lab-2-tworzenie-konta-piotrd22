from app.Konto import Konto
import requests
import os
from datetime import date


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.fast_t_cost = 5
        self.historia = []

        self.is_nip(NIP)

    def is_nip(self, NIP):
        if (len(NIP) == 10 and NIP.isdigit() and self.is_nip_real(NIP)):
            self.NIP = NIP
        else:
            self.NIP = "Niepoprawny NIP!"

    def is_nip_real(self, NIP):
        today_date = date.today()
        today = today_date.strftime("%Y-%m-%d")

        response = requests.get(
            f"${os.environ.get('BANK_APP_MF_URL')}/${NIP}?date=${today}"
        )

        if (response.status_code == 200):
            return True
        else:
            return False

    def check_balance_to_loan(self, suma):
        if (self.saldo >= 2 * suma):
            return True
        else:
            return False

    def check_history_to_loan(self):
        filtered_history = filter(lambda x: x == -1775, self.historia)
        if (len(list(filtered_history)) >= 1):
            return True
        else:
            return False

    def zaciagnij_kredyt(self, suma):
        if (self.check_history_to_loan() and self.check_balance_to_loan(suma)):
            self.saldo += suma
            return True
        else:
            return False

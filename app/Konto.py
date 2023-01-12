import datetime


class Konto:
    def transfer_to(self, sum):
        if (self.saldo - sum >= 0):
            self.saldo -= sum
            self.historia.insert(0, -sum)

    def transfer_from(self, sum):
        self.saldo += sum
        self.historia.insert(0, sum)

    def transfer_to_fast(self, sum):
        if (self.saldo - sum - self.fast_t_cost >= -self.fast_t_cost):
            self.saldo -= (sum + self.fast_t_cost)
            self.historia.insert(0, -sum)
            self.historia.insert(0, -self.fast_t_cost)

    def wyslij_historie_na_maila(self, adresat, smtp_connection):
        tresc = f"Twoja historia konta to: {self.historia}"
        temat = f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}"
        return smtp_connection.wyslij(temat, tresc, adresat)

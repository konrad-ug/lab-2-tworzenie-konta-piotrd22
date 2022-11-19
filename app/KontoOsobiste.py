from app.Konto import Konto


class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, kod_prom=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.fast_t_cost = 1
        self.historia = []

        self.is_pesel(pesel)
        self.is_promo(kod_prom)

    def is_pesel(self, pesel):
        if (len(pesel) == 11 and pesel.isdigit()):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def is_promo(self, kod_prom):
        if (kod_prom != None and kod_prom[:5] == "PROM_" and len(kod_prom) == 8):
            if (int(self.pesel[0:2]) > 60 or int(self.pesel[2:4]) > 20):
                self.saldo = 50
            else:
                self.saldo = 0

        else:
            self.saldo = 0

    def check_history_to_loan(self):
        if len(self.historia) < 3:
            return False
        else:
            ints = filter(lambda x: x > 0, self.historia[0:3])
            if (len(list(ints)) == 3):
                return True
            else:
                return False

    def check_sum_of_last5(self, suma):
        return len(self.historia) >= 5 and sum(self.historia[0:5]) > suma

    def zaciagnij_kredyt(self, suma):
        if (self.check_history_to_loan() and self.check_sum_of_last5(suma)):
            self.saldo += suma
            return True
        else:
            return False

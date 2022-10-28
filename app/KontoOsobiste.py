from app.Konto import Konto

class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, kod_prom = None):
        self.imie = imie
        self.nazwisko = nazwisko

        self.is_pesel(pesel)
        self.is_promo(kod_prom)
    
    def is_pesel(self, pesel):
        if(len(pesel) == 11 and pesel.isdigit()):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
    
    def is_promo(self, kod_prom):
        if(kod_prom != None and kod_prom[:5] == "PROM_" and len(kod_prom) == 8):
            if(int(self.pesel[0:2]) > 60 or int(self.pesel[2:4]) > 20):
                self.saldo = 50
            else:
                self.saldo = 0

        else:
            self.saldo = 0
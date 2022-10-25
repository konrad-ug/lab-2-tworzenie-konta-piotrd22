class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_prom = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.is_pesel(pesel)
        self.is_promo(kod_prom)
    
    def is_pesel(self, pesel):
        if(len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprwany pesel!"
    
    def is_promo(self, kod_prom):
        if(kod_prom != None and kod_prom[:5] == "PROM_" and len(kod_prom) == 8):
            self.saldo = 50

        else:
            self.saldo = 0

    
    

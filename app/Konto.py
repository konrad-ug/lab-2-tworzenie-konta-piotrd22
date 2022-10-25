class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_prom = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.is_pesel(pesel)

    
    def is_pesel(self, pesel):
        if(len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprwany pesel!"
    
    

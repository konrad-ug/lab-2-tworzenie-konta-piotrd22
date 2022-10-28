from app.Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0

        self.is_nip(NIP)
    
    
    def is_nip(self, NIP):
        if(len(NIP) == 10 and NIP.isdigit()):
            self.NIP = NIP
        else:
            self.NIP = "Niepoprawny NIP!"
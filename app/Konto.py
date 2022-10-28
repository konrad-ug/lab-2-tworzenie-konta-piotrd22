class Konto:
    def transfer_to(self, sum):
        if(self.saldo - sum >= 0):
            self.saldo -= sum
        else:
            self.saldo = self.saldo
    
    def transfer_from(self, sum):
        self.saldo += sum

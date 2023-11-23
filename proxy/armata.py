from batalion_proxy import BatalionProxy

class Armata:
    def _init_(self):
        self.batalioane = []

    def adauga_batalion(self, batalion):
        proxy = BatalionProxy(batalion)
        self.batalioane.append(proxy)

    def afiseaza_informatii_batalioane(self):
        for batalion in self.batalioane:
            print(batalion.afiseaza_informatii())
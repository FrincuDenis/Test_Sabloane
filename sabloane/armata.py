class Armata:
    def __init__(self):
        self.batalioane = []

    def adauga_batalion(self, batalion):
        self.batalioane.append(batalion)

    def elimina_batalion(self, batalion):
        self.batalioane.remove(batalion)

    def afiseaza_informatii_batalione(self):
            for batalion in self.batalioane:
                print(batalion.afiseaza_informatii())

    def __str__(self):
        return "Armata:\n" + "\n".join(str(batalion) for batalion in self.batalioane)
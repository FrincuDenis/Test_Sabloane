# Implementarea folosind pattern-ul Proxy

# Interfața Batalion
class Batalion:
    def afiseaza_informatii(self):
        pass

# Clase Concrete pentru diferite tipuri de batalioane
class BatalionGnomi(Batalion):
    def afiseaza_informatii(self):
        return "Batalion de Gnomi"

class BatalionElfi(Batalion):
    def afiseaza_informatii(self):
        return "Batalion de Elfi"

class BatalionEnti(Batalion):
    def afiseaza_informatii(self):
        return "Batalion de Enți"

class BatalionUmanoizi(Batalion):
    def afiseaza_informatii(self):
        return "Batalion de Umanoizi"

# Clasa BatalionProxy
class BatalionProxy(Batalion):
    def _init_(self, batalion_real):
        self.batalion_real = batalion_real

    def afiseaza_informatii(self):
        # Logica adițională sau controlul accesului poate fi adăugat aici
        return self.batalion_real.afiseaza_informatii()

# Clasa Armata
class Armata:
    def _init_(self):
        self.batalioane = []

    def adauga_batalion(self, batalion):
        proxy = BatalionProxy(batalion)
        self.batalioane.append(proxy)

    def afiseaza_informatii_batalioane(self):
        for batalion in self.batalioane:
            print(batalion.afiseaza_informatii())

# Exemplu de utilizare
armata = Armata()
armata.adauga_batalion(BatalionGnomi())
armata.adauga_batalion(BatalionElfi())
armata.adauga_batalion(BatalionEnti())
armata.adauga_batalion(BatalionUmanoizi())

# Afișarea informațiilor batalioanelor prin proxy-uri
armata.afiseaza_informatii_batalioane()
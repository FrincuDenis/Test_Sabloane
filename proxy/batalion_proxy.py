from batalioane import Batalion

class BatalionProxy(Batalion):
    def _init_(self, batalion_real):
        self.batalion_real = batalion_real

    def afiseaza_informatii(self):
        # Logica adițională sau controlul accesului poate fi adăugat aici
        return self.batalion_real.afiseaza_informatii()
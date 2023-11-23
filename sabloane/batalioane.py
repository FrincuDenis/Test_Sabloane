from creatura import Creatura

class Batalion:
    def __init__(self, tip):
        self.tip = tip
        self.creaturi = []

    def acceptelfi(self, visitor):
        visitor.visit_bat_elfi(self)

    def acceptenti(self, visitor):
        visitor.visit_bat_enti(self)

    def acceptgnomi(self, visitor):
        visitor.visit_bat_gnomi(self)


    def adauga_creatura(self, creatura):
        self.creaturi.append(Creatura)

    def elimina_creatura(self, creatura):
        self.creaturi.remove(Creatura)

    def __str__(self):
        return f"Batalion de {self.tip}: " + ", ".join(str(creatura) for creatura in self.creaturi)
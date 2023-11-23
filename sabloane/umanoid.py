class Umanoid:
    def __init__(self, nume, rang, abilitati):
        self.nume = nume
        self.rang = rang  # De exemplu, soldat, căpitan, rege etc.
        self.abilitati = abilitati  # Abilități sau caracteristici specifice umanoizilor (oamenilor)

    def acceptelfi(self, visitor):
        visitor.visit_elfi(self)

    def acceptgnomi(self, visitor):
        visitor.visit_gnomi(self)
    def __str__(self):
        return f"{self.nume} (Rang: {self.rang}, Abilități: {self.abilitati})"

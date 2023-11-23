from sabloane.armata import Armata
from sabloane.batalioane import Batalion
from sabloane.elfi import Elf
from sabloane.gnomi import Gnom
from sabloane.enti import Ent
from sabloane.visitor import ConcreteVisitorStats as visit

# SABLOANE FOLOSITE: Proxy, visitor, Single Responsibility Principle

armata = Armata()
lista_membri = []

# Crearea și adăugarea batalioanelor
batalion_gnomi = Batalion("Gnomi")
visit.nr_bat_gnomi += 1

batalion_elfi = Batalion("Elfi")
visit.nr_bat_elfi += 1

batalion_enti = Batalion("Enti")
visit.nr_bat_enti += 1

lista_membri.append(Gnom("Gimli", 120,"ma bate vantu in fata"))
lista_membri.append(Elf("Legolas", 150,"ma bate vantu in fata"))
lista_membri.append(Ent("Treebeard", 300))

for membru in lista_membri:
    if isinstance(membru,Gnom):
        batalion_gnomi.adauga_creatura(membru)
        visit.nr_gnomi += 1
    if isinstance(membru,Elf):
        batalion_elfi.adauga_creatura(membru)
        visit.nr_elfi += 1
    if isinstance(membru,Ent):
        batalion_enti.adauga_creatura(membru)
        visit.nr_elfi += 1
armata.adauga_batalion(batalion_gnomi)
armata.adauga_batalion(batalion_elfi)
armata.adauga_batalion(batalion_enti)

# Afișarea structurii armatei
print(armata)

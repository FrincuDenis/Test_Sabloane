from armata import Armata
from proxy.batalion_gnomi import BatalionGnomi
from proxy.elfi import BatalionElfi
from proxy.manu import BatalionEnti, BatalionUmanoizi

armata = Armata()
armata.adauga_batalion(BatalionGnomi())
armata.adauga_batalion(BatalionElfi())
armata.adauga_batalion(BatalionEnti())
armata.adauga_batalion(BatalionUmanoizi())

# Afișarea informațiilor batalioanelor prin proxy-uri
armata.afiseaza_informatii_batalioane()
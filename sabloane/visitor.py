
class Visitor:
    def visit_bat(self, batalion):
        pass
class ConcreteVisitorStats(Visitor):
    nr_elfi = 0
    nr_enti = 0
    nr_gnomi=  0
    nr_bat_elfi=0
    nr_bat_gnomi=0
    nr_bat_enti=0
    def visit_elfi(self, element_a):
        pass
    def visit_gnomi(self, element_b):
        pass
    def visit_enti(self, element_b):
        pass

    def visit_bat_elfi(self, element_b):
        pass

    def visit_bat_enti(self, element_b):
        pass

    def visit_bat_gnomi(self, element_b):
        pass

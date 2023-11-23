from creatura import Creatura

class Gnom(Creatura):
    def accept(self, visitor):
        visitor.visit_gnom(self)

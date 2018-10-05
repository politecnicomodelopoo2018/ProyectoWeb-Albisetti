from database import *

class publico_has_suveniers(object):

    idPublico = None
    idSuveniers = None
    cantidad_suveniers = None

    def __init__(self, idPublico = None, idSuveniers = None, cantidad_suveniers = None):

        self.idPublico = idPublico
        self.idSuveniers = idSuveniers
        self.cantidad_suveniers = cantidad_suveniers

    def alta(self):
         Database().run("INSERT INTO publico_has_suveniers VALUES(%s, %s, %s)" %(self.idPublico, self.idSuveniers,
                                                                                 self.cantidad_suveniers))
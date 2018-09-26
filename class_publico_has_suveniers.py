from database import *

class publico_has_suveniers(object):

    idPublico = None
    idSuveniers = None

    def __init__(self, idPublico = None, idSuveniers = None):

        self.idPublico = idPublico
        self.idSuveniers = idSuveniers

    def alta(self):

         Database().run("INSERT INTO publico_has_suveniers VALUES(%s, %s)" %(self.idPublico, self.idSuveniers))
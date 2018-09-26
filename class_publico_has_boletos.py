from database import *

class publico_has_boletos(object):

    idPublico = None
    idBoletos = None

    def __init__(self, idPublico = None, idBoletos = None):

        self.idPublico = idPublico
        self.idBoletos = idBoletos

    def alta(self):

        Database().run("INSERT INTO publico_has_boletos VALUES(%s, %s)"%(self.idPublico, self.idBoletos))
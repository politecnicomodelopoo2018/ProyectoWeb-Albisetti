from database import *

class publico_has_boletos(object):

    idPublico = None
    idBoletos = None
    cantidad_boletos = None

    def __init__(self, idPublico = None, idBoletos = None, cantidad_boletos = None):

        self.idPublico = idPublico
        self.idBoletos = idBoletos
        self.cantidad_boletos = cantidad_boletos

    def alta(self):

        Database().run("INSERT INTO publico_has_boletos VALUES(%s, %s, '%s')"%(self.idPublico, self.idBoletos,
                                                                               self.cantidad_boletos))
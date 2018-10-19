from database import *

class publico_has_boletos(object):

    idPublico = None
    idBoletos = None
    cantidad_boletos = None

    def __init__(self, idPublico = None, idBoletos = None, cantidad_boletos = None):

        self.idPublico = idPublico
        self.idBoletos = idBoletos
        self.cantidad_boletos = cantidad_boletos

    @staticmethod
    def cargar(idP, idB):
        info = Database().run("Select * FROM publico_has_boletos WHERE idPublico = %s AND idBoletos = %s" %(idP, idB))
        publico_boleto = publico_has_boletos()

        for item in info:
            publico_boleto.idPublico = item["idPublico"]
            publico_boleto.idBoletos = item["idBoletos"]
            publico_boleto.cantidad_boletos = item["cantidad_boletos"]


        return publico_boleto

    def alta(self):

        Database().run("INSERT INTO publico_has_boletos VALUES(%s, %s, '%s')"%(self.idPublico, self.idBoletos,
                                                                               self.cantidad_boletos))
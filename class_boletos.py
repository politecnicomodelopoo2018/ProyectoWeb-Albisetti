from database import *

class boletos(object):

    idBoletos = None
    dia_boleto = None
    costo_boleto = None

    @staticmethod
    def cargar(id):
        info = Database().run("Select * FROM boletos WHERE idBoletos = '%s'" % (id))
        boleto = boletos()

        for item in info:
            boleto.idBoletos = item["idBoletos"]
            boleto.dia_boleto = item["dia_boleto"]
            boleto.costo_boleto = item["costo_boleto"]

        return boleto
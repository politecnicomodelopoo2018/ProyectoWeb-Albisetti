from database import *

class suveniers(object):

    idSuveniers = None
    costo_camisa = None
    costo_etiquetas = None
    idPublico = None

    @staticmethod
    def cargar(id):

        info = Database().run("SELECT * FROM suveniers WHERE idSuveniers = '%s'" %(id))

        suvenier = suveniers()


        for item in info:
            suvenier.idSuveniers = item["idSuveniers"]
            suvenier.costo_camisa = item["costo_camisa"]
            suvenier.costo_etiquetas = item["costo_etiquetas"]
            suvenier.idPublico = item["idPublico"]

        return suvenier
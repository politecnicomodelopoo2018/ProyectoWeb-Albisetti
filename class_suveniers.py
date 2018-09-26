from database import *

class suveniers(object):

    idSuveniers = None
    descripcion_suvenier = None
    costo_suvenier = None

    @staticmethod
    def cargar(id):

        info = Database().run("SELECT * FROM suveniers WHERE idSuveniers = '%s'" %(id))

        suvenier = suveniers()


        for item in info:
            suvenier.idSuveniers = item["idSuveniers"]
            suvenier.descripcion_suvenier = item["descripcion_suvenier"]
            suvenier.costo_suvenier = item["costo_suvenier"]

        return suvenier
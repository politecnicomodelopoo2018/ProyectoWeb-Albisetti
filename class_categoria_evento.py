from database import *

class categoria_evento(object):

    idCategoria = None
    cat_evento = None
    icono = None


    @staticmethod
    def cargar(id):
        info = Database().run("Select * FROM categoria_evento")

        categoria = categoria_evento()

        for item in info:
            if id == item["idCategoria"]:
                categoria.idCategoria = item["iddCategoria"]
                categoria.cat_evento = item["cat_evento"]
                categoria.icono = item["icono"]

        return categoria


    def alta(self):

        Database().run("INSERT INTO categoria_evento Values (NULL, %s, '%s')" %(self.cat_evento, self.icono))


    def baja(self):

        infoAux = Database().run("Select idCategoria FROM categoria_evento WHERE idCategoria = %s" % self.idCategoria)

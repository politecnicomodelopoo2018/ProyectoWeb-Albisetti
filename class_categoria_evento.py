from database import *

class categoria_evento(object):

    idCategoria = None
    cat_evento = None

    @staticmethod
    def cargar(id):
        info = Database().run("Select * FROM categoria_evento WHERE idCategoria = '%s'" %(id))

        categoria = categoria_evento()

        for item in info:
            categoria.idCategoria = item["idCategoria"]
            categoria.cat_evento = item["cat_evento"]

        return categoria


    def alta(self):

        Database().run("INSERT INTO categoria_evento Values (NULL, '%s', '%s')" %(self.cat_evento, self.icono))


    def baja(self):

        Database().run("DELETE FROM eventos WHERE idCategoria = '%s'" %(self.idCategoria))

        Database().run("DELETE FROM categoria_evento WHERE idCategoria = '%s'" %(self.idCategoria))


    def modificacion(self):

        Database().run("UPDATE categoria_evento SET cat_evento = '%s', icono = '%s'"%(self.cat_evento, self.icono))
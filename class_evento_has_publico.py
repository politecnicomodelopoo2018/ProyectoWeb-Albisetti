from database import *

class evento_has_publico(object):

    idEvento = None
    idPublico = None

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM evento_has_publico")
        evento_publico = evento_has_publico()

        for item in info:
            evento_publico.idPublico = item["idPublico"]
            evento_publico.idEvento = item["idEvento"]


    def alta(self):

        Database().run("INSERT INTO evento_has_publico VALUES('%s','%s')" %(self.idEvento, self.idPublico))

    def borrar(self):

        Database().run("DELETE FROM evento_has_publico WHERE idPublico = '%s' AND idEvento = '%s'"%(self.idPublico,
                                                                                                    self.idEvento))
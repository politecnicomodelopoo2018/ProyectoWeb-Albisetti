from database import *

class evento_has_publico(object):

    idEvento = None
    idPublico = None

    def __init__(self, idEvento = None, idPublico = None):
        self.idEvento = idEvento
        self.idPublico = idPublico

    @staticmethod
    def cargar(idP, idE):

        info = Database().run("Select * FROM eventos_has_publico WHERE idPublico = %s AND idEvento = %s"%(idP, idE))
        evento_publico = evento_has_publico()

        for item in info:
            evento_publico.idPublico = item["idPublico"]
            evento_publico.idEvento = item["idEvento"]


    def alta(self):

        Database().run("INSERT INTO eventos_has_publico VALUES('%s','%s')" %(self.idEvento, self.idPublico))

    def borrar(self):

        Database().run("DELETE FROM eventos_has_publico WHERE idPublico = '%s' AND idEvento = '%s'"%(self.idPublico,
                                                                                                    self.idEvento))

    def bajaPublico(self):

        Database().run("DELETE FROM eventos_has_publico WHERE idPublico = '%s'" % (self.idPublico))
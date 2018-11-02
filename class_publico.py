from database import *
from class_publico_has_boletos import *
from class_publico_has_suveniers import *
from class_evento_has_publico import *

class publico(object):

    idPublico = None
    nombre_persona = None
    apellido_persona = None
    email = None
    regalo = None

    def __init__(self, idPublico = None, nombre_persona = None, apellido_persona = None, email = None, regalo = None):

        self.idPublico = idPublico
        self.nombre_persona = nombre_persona
        self.apellido_persona = apellido_persona
        self.email = email
        self.regalo = regalo

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM publico WHERE idPublico = '%s'" %(id))
        gente = publico()

        for item in info:
            gente.idPublico = item["idPublico"]
            gente.nombre_persona = item["nombre_persona"]
            gente.apellido_persona = item["apellido_persona"]
            gente.email = item["email"]
            gente.regalo = item["regalo"]

        return gente

    def alta(self):

        cosa = Database().run("INSERT INTO publico VALUES(NULL, '%s', '%s', '%s', '%s')" % (self.nombre_persona,
                                                                              self.apellido_persona,
                                                                              self.email,
                                                                              self.regalo))
        return cosa

    def baja(self):

        objetoPublicoBoletos = publico_has_boletos(self.idPublico)
        objetoPublicoSuveniers = publico_has_suveniers(self.idPublico)
        objetoEventoPublico = evento_has_publico(None, self.idPublico)

        objetoPublicoBoletos.bajaPublico()
        objetoPublicoSuveniers.bajaPublico()
        objetoEventoPublico.bajaPublico()

        Database().run("Delete From publico where idPublico = %s" % (self.idPublico))
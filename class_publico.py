from database import *

class publico(object):

    idPublico = None
    nombre_persona = None
    apellido_persona = None
    cant_pases_dia = None
    cant_pases_dos_dias = None
    cant_pases_tres_dias = None
    cant_camisas = None
    cant_etiquetas = None
    regalo = None

    def __init__(self):

    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM publico WHERE idPublico = '%s'" %(id))
        gente = publico()

        for item in info:
            gente.idPublico = item["idPublico"]
            gente.nombre_persona = item["nombre_persona"]
            gente.apellido_persona = item["apellido_persona"]
            gente.cant_pases_dia = item["cant_pases_dia"]
            gente.cant_pases_dos_dias = item["cant_pases_dos_dias"]
            gente.cant_pases_tres_dias = item["cant_pases_tres_dias"]
            gente.cant_camisas = item["cant_camisas"]
            gente.cant_etiquetas = item["cant_etiquetas"]
            gente.regalo = item["regalo"]

        return gente

    def alta(self):

        Database().run("INSERT INTO publico VALUES(NULL, '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s')"
                        % (self.nombre_persona, self.apellido_persona, self.cant_pases_dia, self.cant_pases_dos_dias,
                           self.cant_pases_tres_dias, self.cant_camisas, self.cant_etiquetas, self.regalo))
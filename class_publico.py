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
    monto_total = None


    @staticmethod
    def cargar(id):

        info = Database().run("Select * FROM publico")
        gente = publico()

        for item in info:
            if id == item["idEvento"]:
                gente.idPublico = item["idPublico"]
                gente.nombre_persona = item["nombre_persona"]
                gente.apellido_persona = item["apellido_persona"]
                gente.cant_pases_dia = item["cant_pases_dia"]
                gente.cant_pases_dos_dias = item["cant_pases_dos_dias"]
                gente.cant_pases_tres_dias = item["cant_pases_tres_dias"]
                gente.cant_camisas = item["cant_camisas"]
                gente.cant_etiquetas = item[""]

        return gente
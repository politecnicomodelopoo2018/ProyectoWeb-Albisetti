from database import *


class eventos(object):

    idEvento = None
    nombre_evento = None
    fecha_evento = None
    hora_evento = None
    clave = None
    idCategoria = None
    idInvitado = None


@staticmethod
def cargar(id):
    info = Database().run("Select * FROM eventos")

    evento = eventos()

    for item in info:
        if id == item["idEvento"]:
            evento.idInvitado = item["idEvento"]
            evento.nombre_invitado = item["nombre_evento"]
            evento.apellido_invitado = item["fecha_evento"]
            evento.descripcion = item["hora_evento"]
            evento.url_imagen = item["clave"]
            evento.idCategoria = item["idCategoria"]
            evento.idInvitado = item["idInvitado"]

    return evento
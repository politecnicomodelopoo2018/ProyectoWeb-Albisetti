from database import *

class invitados(object):

    idInvitado = None
    nombre_invitado = None
    apellido_invitado = None
    descripcion = None
    url_imagen = None

@staticmethod
def cargar(id):
    info = Database().run("Select * FROM invitados")

    invitado = invitados()

    for item in info:
        if id == item["idInvitado"]:
            invitado.idInvitado = item["idInvitado"]
            invitado.nombre_invitado = item["nombre_invitado"]
            invitado.apellido_invitado = item["apellido_invitado"]
            invitado.descripcion = item["descripcion"]
            invitado.url_imagen = item["url_imagen"]

    return invitado


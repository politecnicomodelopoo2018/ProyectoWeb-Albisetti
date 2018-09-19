from database import *

class invitados(object):

    idInvitado = None
    nombre_invitado = None
    apellido_invitado = None
    descripcion = None
    url_imagen = None

    @staticmethod
    def cargar(id):
        info = Database().run("Select * FROM invitados WHERE idInvitado = '%s'" %(id))

        invitado = invitados()

        for item in info:
            invitado.idInvitado = item["idInvitado"]
            invitado.nombre_invitado = item["nombre_invitado"]
            invitado.apellido_invitado = item["apellido_invitado"]
            invitado.descripcion = item["descripcion"]
            invitado.url_imagen = item["url_imagen"]

        return invitado

    def alta(self):

        Database().run("INSERT INTO invitados Values (NULL, %s, '%s', '%s', '%s')" % (self.nombre_invitado,
                                                                                      self.apellido_invitado,
                                                                                      self.descripcion,
                                                                                      self.url_imagen))

    def baja(self):

        Database().run("DELETE FROM eventos WHERE idInivitado = '%s'" %(self.idInvitado))

        Database().run("DELETE FROM invitados WHERE idInivitado = '%s'" %(self.idInvitado))

    def modificacion(self):

        Database().run("UPDATE invitados SET nombre_invitado = '%s', apellido_invitado = '%s', descripcion = '%s',"
                       "url_imagen = '%s'" %(self.nombre_invitado, self.apellido_invitado, self.descripcion,
                                             self.url_imagen))
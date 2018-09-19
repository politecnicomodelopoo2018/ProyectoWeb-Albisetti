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

        info = Database().run("Select * FROM eventos WHERE idEvento = '%s'" %(id))
        evento = eventos()

        for item in info:
            evento.idEvento = item["idEvento"]
            evento.nombre_evento = item["nombre_evento"]
            evento.fecha_evento = item["fecha_evento"]
            evento.hora_evento = item["hora_evento"]
            evento.clave = item["clave"]
            evento.idCategoria = item["idCategoria"]
            evento.idInvitado = item["idInvitado"]

        return evento

    def alta(self):

        Database().run("INSERT INTO eventos VALUES(NULL, '%s', '%s', '%s', '%s', '%s', '%s')" % (self.nombre_evento,
                                                                                                 self.fecha_evento,
                                                                                                 self.hora_evento,
                                                                                                 self.clave,
                                                                                                 self.idCategoria,
                                                                                                 self.idInvitado))

    def baja(self):

        Database().run("DELETE FROM eventos WHERE idEvento = '%s'" % (self.idEvento))

    def modificacion(self):

        Database().run(("UPDATE Categorias SET nombre_evento = '%s', fecha_evento = '%s', "
                        "hora_evento = '%s', clave = '%s', idCategoria = '%s', idInvitado = '%s' WHERE idEvento = '%s'"
                        % (self.nombre_evento, self.fecha_evento, self.hora_evento, self.clave, self.idCategoria,
                           self.idInvitado, self.idEvento)))

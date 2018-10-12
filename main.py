from pymysql import *
from flask import request, jsonify, render_template, Flask, redirect, session
from database import *
import hashlib
import base64
import uuid

from class_invitados import *
from class_boletos import *
from class_publico import *
from class_categoria_evento import *
from class_eventos import *
from class_evento_has_publico import *
from class_suveniers import *
from class_publico_has_suveniers import *
from class_publico_has_boletos import *

Data = Database()


Data.setConnection("127.0.0.1", "root", "alumno", "web")

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


invitado = Data.run("SELECT * FROM invitados")

password = "&Administrador200&"

listaInvitados = []

for item in invitado:
    invita = invitados.cargar(item["idInvitado"])
    listaInvitados.append(invita)

boleto = Data.run("SELECT * FROM boletos")

listaBoletos = []

for item in boleto:
    bolet = boletos.cargar(item["idBoletos"])
    listaBoletos.append(bolet)


suvenierL = Data.run("SELECT * FROM suveniers")

listaSuveniers = []

for item in suvenierL:
    suvenier = suveniers.cargar(item["idSuveniers"])
    listaSuveniers.append(suvenier)

eventoL = Data.run("SELECT * FROM eventos")

listaEventos = []
listaDias = []
diaAnterior = ""

for item in eventoL:
    evento = eventos.cargar(item["idEvento"])
    dia = evento.dia_evento
    if(dia != diaAnterior):
        diaAnterior = dia
        listaDias.append(diaAnterior)

    listaEventos.append(evento)

categoriaL = Data.run("SELECT * FROM categoria_evento")

listaCategorias = []

for item in categoriaL:
    categoria = categoria_evento.cargar(item["idCategoria"])
    listaCategorias.append(categoria)


@app.route("/")
def inicio():
    return render_template("index.html", listaInvitados = listaInvitados, listaBoletos = listaBoletos)



@app.route("/registro")
def registro():

    return render_template("registro.html", listaBoletos = listaBoletos, listaSuveniers = listaSuveniers,
                           listaEventos = listaEventos, listaCategorias = listaCategorias, listaDias = listaDias,
                           longitud = len(listaEventos))

@app.route("/registroCompleto", methods=["GET", "POST"])
def checkear():

    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    regalo = request.form.get("regalo")

    idInsertada = publico(None, nombre, apellido, email, regalo).alta().lastrowid

    for item in listaBoletos:
        cantidad_boleto = request.form.get(item.dia_boleto)
        if(cantidad_boleto):
            cantidad_boleto = int(cantidad_boleto)
            if(cantidad_boleto > 0 and cantidad_boleto != None):
                publico_has_boletos(idInsertada, item.idBoletos, cantidad_boleto).alta()

    for item in listaSuveniers:
        cantidad_suvenier = request.form.get(item.descripcion_suvenier)
        if(cantidad_suvenier):
            cantidad_suvenier = int(cantidad_suvenier)
            if(cantidad_suvenier > 0 and cantidad_suvenier != None):
                publico_has_suveniers(idInsertada, item.idSuveniers, cantidad_suvenier).alta()

    for item in listaEventos:
        eventoAsistido = request.form.get(item.nombre_evento)
        if(eventoAsistido):
            evento_has_publico(eventoAsistido, idInsertada).alta()


    return redirect("/")

@app.route("/adminLogin")
def adminLogin():

    return render_template("adminLogin.html")


@app.route("/adminCheck", methods=["GET", "POST"])
def adminCheck():
    nombreAdmin = request.form.get("nombre_admin")
    contraseña = request.form.get("contraseña")

    administradores = Data.run("SELECT * FROM admins")

    for item in administradores:
        if nombreAdmin == item["usuario_admin"] and hashlib.sha512(contraseña.encode('utf-8')).hexdigest() == item["password_admin"]:
            session["admin"] = item["idAdmin"]
            return redirect("/admin")



    return redirect("/")


@app.route("/admin")
def admin():
    if "admin" in session:
        return render_template("admin.html", listaSuveniers = listaSuveniers, listaEventos = listaEventos,
                               listaBoletos = listaBoletos, listaInvitados = listaInvitados)
    else:
        return redirect("/")

@app.route("/admin=post", methods=["GET", "POST"])
def adminPost():

    return render_template()

if __name__ == "__main__":
    app.run(debug=True)
from pymysql import *
from flask import request, jsonify, render_template, Flask, redirect
from database import *

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

invitado = Data.run("SELECT * FROM invitados")

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

for item in eventoL:
    evento = eventos.cargar(item["idEventos"])
    listaEventos.append(eventos)

@app.route("/")
def inicio():
    return render_template("index.html", listaInvitados = listaInvitados, listaBoletos = listaBoletos)



@app.route("/registro")
def registro():

    return render_template("registro.html", listaBoletos = listaBoletos, listaSuveniers = listaSuveniers,
                           listaEventos = listaEventos)

@app.route("/registroCompleto", methods=["GET", "POST"])
def checkear():

    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    regalo = request.form.get("regalo")

    idInsertada = publico(None, nombre, apellido, email, regalo).alta().lastrowid

    for item in listaBoletos:
        cantidad_boleto = request.form.get(item.dia_boleto)
        publico_has_boletos(idInsertada, item.idBoletos, int(cantidad_boleto)).alta()

    for item in listaSuveniers:
        cantidad_suvenier = request.form.get(item.descripcion_suvenier)
        publico_has_suveniers(idInsertada, item.idSuveniers, cantidad_suvenier).alta()

    return redirect("/")

@app.route("/calendario")
def calendario():

    return render_template("calendario.html")

@app.route("/admin")
def admin():

    return render_template()


@app.route("/admin=post", methods=["GET", "POST"])
def adminPost():

    return render_template()

if __name__ == "__main__":
    app.run(debug=True)
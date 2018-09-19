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

Data = Database()

Data.setConnection("127.0.0.1", "root", "alumno", "web")

app = Flask(__name__)

invitado = Data.run("SELECT * FROM invitados")
listaInvitados = []
for item in invitado:
    invita = invitados.cargar(item["idInvitado"])
    listaInvitados.append(invita)

@app.route("/")
def inicio():
    return render_template("index.html", invitado = listaInvitados)

@app.route("/registro")
def registro():

    return render_template("registro.html")

@app.route("/registroCompleto", methods=["GET", "POST"])
def checkear():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")

    cant_pases = request.form.get("pase_dia")
    cant_dos_dias = request.form.get("pase_dosdias")
    cant_tres_dias = request.form.get("pase_completo")

    camisas = request.form.get("camisa_evento")
    etiquetas = request.form.get("etiquetas")
    regalo = request.form.get("regalo")

    persona = publico(nombre, apellido, email, cant_pases, cant_dos_dias, cant_tres_dias, camisas, etiquetas, regalo)
    persona.alta()

    return redirect("/")

@app.route("/calendario")
def calendario():

    return render_template("calendario.html")

@app.route("/invitados")
def invitados():

    return render_template("invitados.html")

@app.route("/conferencia")
def conferencia():

    return render_template("conferencia.html")

if __name__ == "__main__":
    app.run(debug=True)
from pymysql import *
from flask import request, jsonify, render_template, Flask
from database import *

Data = Database()

Data.setConnection("127.0.0.1", "root", "alumno", "web")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("index.html")

@app.route("/registro")
def registro():

    return render_template("registro.html")

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
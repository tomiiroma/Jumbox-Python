from flask import Flask, render_template, request
from app.models.Sucursal import Sucursal
import app.conexion as db
from app.controller.sucursal_controlador import get_sucursal 

app = Flask(__name__)


@app.route("/",  methods=["GET", "POST"])
def hello_world():
    db.iniciar_db()
    message = ""
    sucursales = get_sucursal()
    if request.method == "POST":
        message = "Has iniciado sesión"

    return render_template("index.html", message=message, sucursales=sucursales)

    
    
@app.route("/login")
def formulario():
    return render_template('login.html')

    

if __name__ == "__main__":
    app.run(debug=True)

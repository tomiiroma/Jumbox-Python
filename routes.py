from flask import Flask, render_template, request
from app.models.Sucursal import Sucursal
from app.controller.categoria_controller import agregar_categoria


app = Flask(__name__)


@app.route("/",  methods=["GET", "POST"])
def hello_world():
    message = ""
    if request.method == "POST":
        message = "Has iniciado sesión"

    return render_template("index.html", message=message)


    
@app.route("/login")
def formulario():
    return render_template('login.html')


@app.route("/categoria/create",methods=["GET", "POST"])
def nueva_categoria():

    if request.method == "POST":
        nombre = request.form['nombre']
        estado = 1

        datos = agregar_categoria(nombre,estado)

        mensaje = "Categoria agregada correctamente."

        return render_template('categoria/create.html', mensaje=mensaje)

    return render_template('categoria/create.html')    


if __name__ == "__main__":
    app.run(debug=True)

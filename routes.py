from flask import Flask, render_template, request, session, flash
from app.models.Sucursal import Sucursal
from app.models.Categoria import Categoria
from app.controller.categoria_controller import agregar_categoria,mostrar_categorias
import app.conexion as db
from app.controller.sucursal_controlador import get_sucursal 
from app.controller.usuario_controlador import verificar_login


app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/",  methods=["GET", "POST"])
def hello_world():
    db.iniciar_db()
    success = "Inicio de Sesion Exitoso"
    error="Email o contraseña incorrectas"
    sucursales = get_sucursal()

    if request.method == "POST":
        email = request.form["email"]
        cont = request.form["cont"]

        if verificar_login(email, cont):
            session['usuario'] = email
            return render_template("index.html", success=success, sucursales=sucursales)
        else:
            return render_template('login.html', error=error)

        
    return render_template("index.html", sucursales=sucursales)

    
    
@app.route("/login")
def formulario():
    return render_template('login.html')

@app.route("/categoria/create", methods=["GET", "POST"])
def nueva_categoria():
    if request.method == "POST":
        nombre = request.form['nombre']
        estado = 1

        agregar_categoria(nombre, estado)

        mensaje = "Categoria agregada correctamente."

        return render_template('categoria/create.html', mensaje=mensaje)

    return render_template('categoria/create.html')

@app.route("/logout")
def logout():
    return "cerrar sesion"


@app.route("/categoria/index")
def index_categoria():


    categorias = mostrar_categorias()

    print(categorias)

    return render_template('categoria/index.html', categorias=categorias)


if __name__ == "__main__":
    app.run(debug=True)

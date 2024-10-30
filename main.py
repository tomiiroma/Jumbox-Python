from flask import Flask, render_template, request, session, redirect,url_for
from app.models.Sucursal import Sucursal
import app.conexion as db
from app.controller.sucursal_controlador import get_sucursal 
from app.controller.usuario_controlador import verificar_login

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/",  methods=["GET", "POST"])
def home():
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

@app.route("/logout")
def logout():
    session.pop('usuario')
    return redirect(url_for("home"))

@app.route("/pedidos")
def pedidos():
    if session:
        return render_template("pedidos.html")
    else:
        return redirect(url_for("error"))
    
@app.route("/error")
def error():
    return render_template("erroracceso.html")
    

if __name__ == "__main__":
    app.run(debug=True)

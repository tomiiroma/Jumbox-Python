from flask import Flask, render_template, request, session, flash, redirect, url_for
from app.models.Sucursal import Sucursal
from app.models.Categoria import Categoria
from app.controller.categoria_controller import agregar_categoria,mostrar_categorias,deshabilitar_categoria,filtrar_categoria,modificar_categoria,categorias_filtros_habilitadas,categorias_filtros_deshabilitadas
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


        flag = Categoria.validar_nombre(nombre)

        if flag:

            agregar_categoria(nombre, estado)

            mensaje = "Categoria agregada correctamente."

            flash(mensaje)

            return redirect(url_for('index_categoria'))

        else: 
            
            mensaje = "El nombre no es válido."

            return render_template('categoria/create.html')

    return render_template('categoria/create.html')

@app.route("/logout")
def logout():
    return "cerrar sesion"


@app.route("/categoria/index", methods=["GET", "POST"])
def index_categoria():

    categorias = mostrar_categorias()

    return render_template('categoria/index.html', categorias=categorias)


@app.route("/categoria/modificar", methods=["POST"])

def cambiar_estado_categoria():
    
    if request.method == "POST":

        id_categoria = request.form.get('id_categoria')

        mensaje = deshabilitar_categoria(id_categoria)

        flash(mensaje)

        return redirect(url_for('index_categoria'))

    else: return render_template('categoria/index.html')



@app.route("/categoria/edit/<int:id_categoria>", methods=["GET","POST"])

def form_categoria_nombre(id_categoria):

    if request.method == "POST":

        resultado = filtrar_categoria(id_categoria)
        
        if (resultado[0] is not None):
            
            categoria = resultado[0]

            return render_template('categoria/edit.html/', categoria = categoria)

        else:
            
            mensaje = resultado[1]

            return render_template('categoria/index.html', mensaje=mensaje)
        
    else: # En caso de entrar por metodo GET.

            mensaje = "NO"
        
            return render_template('categoria/index.html', mensaje=mensaje)

@app.route("/categoria/update",methods=["GET","POST"])

def update_categoria():

    if request.method == "POST":

        id_categoria = request.form.get('id_categoria')

        nombre = request.form.get('nombre')

        categoria_instancia = filtrar_categoria(id_categoria)

        categoria = categoria_instancia[0]

        flag = Categoria.validar_nombre(nombre)

        if flag:

            mensaje = modificar_categoria(id_categoria,nombre)
            flash(mensaje)

            return redirect(url_for('index_categoria'))            

            #return render_template('categoria/index.html', mensaje=mensaje)

        else:

            mensaje = "El nombre ingresado no es valido."
            return render_template('/categoria/edit.html', categoria=categoria, mensaje=mensaje)

@app.route("/categoria/visible", methods=["GET","POST"])
def categoria_visible():

    if request.method == "POST":

        resultado = categorias_filtros_habilitadas()

        if resultado[0] is not None:

            categorias = resultado[0]

            mensaje = resultado[1]

            flash(mensaje)

            return render_template('categoria/index.html', categorias=categorias)

        else:

            mensaje = resultado[1]

            flash(mensaje)

            return render_template("categoria/index.html",mensaje=mensaje)
    
    else:

            return redirect(url_for('index_categoria'))
    
@app.route("/categoria/novisible", methods=["GET","POST"])

def categoria_novisible():

    if request.method == "POST":

        resultado = categorias_filtros_deshabilitadas()

        if resultado[0] is not None:

            categorias = resultado[0]

            mensaje = resultado[1]

            flash(mensaje)

            return render_template('categoria/index.html', categorias=categorias)

        else:

            mensaje = resultado[1]

            flash(mensaje)

            return render_template('categoria/index.html', mensaje=mensaje)
    
    else:

            return redirect(url_for('index_categoria'))


if __name__ == "__main__":
    app.run(debug=True)

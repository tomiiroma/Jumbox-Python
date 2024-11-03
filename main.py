from flask import Flask, render_template, request, session, flash, redirect, url_for
from app.models.Sucursal import Sucursal
from app.models.Categoria import Categoria
from app.controller.categoria_controller import agregar_categoria,mostrar_categorias,deshabilitar_categoria,filtrar_categoria,modificar_categoria,categorias_filtros_habilitadas
import app.conexion as db
from app.controller.sucursal_controlador import get_sucursal, get_inventario_por_sucursal
from app.controller.usuario_controlador import verificar_login, get_nombresucursal_por_usuario
from app.controller.producto_controller import agregar_producto, deshabilitar_producto, mostrar_productos  # Importa funciones necesarias
from app.controller.provincia_controller import mostrar_provincias


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

        user = verificar_login(email, cont)

        if user:
            session['usuario'] = user
            flash("Inicio de Sesion Exitoso")
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error=error)

        
    return render_template("index.html", sucursales=sucursales)

    
@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    if session:
        usuario = session.get("usuario")
        sucursales = get_sucursal()


        id_sucursal_de_usuario = usuario[1]

        sucursaldelusuario = get_nombresucursal_por_usuario(id_sucursal_de_usuario)

        if request.method == "POST":
            sucursalelegida = request.form.get("sucursalelegida")

            if sucursalelegida == "vacio":
                errorsucursal = "Por favor, seleccione una sucursal valida"
                return render_template("pedidos.html", sucursales = sucursales, errorsucursal=errorsucursal) 
            
            elif int(sucursalelegida) == id_sucursal_de_usuario:
                 errorsucursal = "No puedes realizar pedidos a tu propia sucursal"
                 return render_template("pedidos.html", sucursales = sucursales ,sucursalelegida=sucursalelegida, errorsucursal=errorsucursal) 
            
            else:
                inventario = get_inventario_por_sucursal(sucursalelegida)
                return render_template("pedidos.html",sucursales = sucursales, sucursalelegida=sucursalelegida, inventario=inventario) 
        
        return render_template("pedidos.html", sucursales = sucursales, sucursaldelusuario = sucursaldelusuario)
    else:
        return redirect(url_for("error"))
    

#@app.route("/productosdesucursal")
#def pedidosNose():
    #if session:
        
   # else:
      #  return redirect(url_for("error"))




@app.route("/error")
def error():
    return render_template("erroracceso.html")
    
    



@app.route("/login")
def formulario():
    return render_template('login.html')



@app.route("/categoria/create", methods=["GET", "POST"])
def nueva_categoria():
    if session:
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

                return render_template('categoria/create.html', mensaje=mensaje)
        return render_template('categoria/create.html')
    else: return redirect(url_for("error"))

@app.route("/logout")
def logout():
    session.pop('usuario')
    flash("Se cerro sesion correctamente")
    return redirect(url_for('home'))


@app.route("/categoria/index", methods=["GET", "POST"])
def index_categoria():
    if session:
    

        categorias = mostrar_categorias()

        return render_template('categoria/index.html', categorias=categorias)

    else: 

        return redirect(url_for("error"))




@app.route("/categoria/modificar", methods=["POST"])

def cambiar_estado_categoria():
    
    if session:

        if request.method == "POST":

            id_categoria = request.form.get('id_categoria')

            mensaje = deshabilitar_categoria(id_categoria)

            flash(mensaje)

            return redirect(url_for('index_categoria'))

        else: return render_template('categoria/index.html')

    else: return redirect(url_for("error"))


@app.route("/productos/create", methods=["GET", "POST"])
def nuevo_producto():
    if request.method == "POST":
        nombre = request.form['nombre']
        precio = request.form['precio']
        marca = request.form['marca']
        estado = int(request.form['estado'])
        descripcion = request.form.get('descripcion', "")
        categoria_id = request.form['categoria']  
        cantidad = request.form['cantidad']

        agregar_producto(nombre, precio, marca, estado, descripcion, categoria_id, cantidad)

        mensaje = "Producto agregado correctamente."

        return render_template('productos/create.html', mensaje=mensaje)

    categorias = mostrar_categorias()
    return render_template('productos/create.html', categorias=categorias)


@app.route("/productos/index")
def index_producto():
    productos = mostrar_productos()  
    print(f"Productos recuperados: {productos}")  # Para verificar qué datos estás obteniendo
    return render_template('productos/index.html', productos=productos)



@app.route("/productos/modificar", methods=["POST"])
def cambiar_estado_productos():
    if request.method == "POST":
        id_producto = request.form.get('id_producto')
        
        if not id_producto:
            flash("No se recibió el ID del producto.")
            return redirect(url_for('index_producto'))

        mensaje = deshabilitar_producto(id_producto)
        print(mensaje)
        flash(mensaje)

        return redirect(url_for('index_producto'))


@app.route("/categoria/edit/<int:id_categoria>", methods=["GET","POST"])

def form_categoria_nombre(id_categoria):

    if session:

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

    else: return redirect(url_for("error"))

@app.route("/categoria/update",methods=["GET","POST"])

def update_categoria():

    if session:

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

            else:

                mensaje = "El nombre ingresado no es valido."
                return render_template('/categoria/edit.html', categoria=categoria, mensaje=mensaje)

        else: redirect(url_for('index_categoria'))

    else: return redirect(url_for("error"))

@app.route("/categoria/visible", methods=["GET","POST"])
def categoria_visible():

    if session:

        if request.method == "POST":

            resultado = categorias_filtros_habilitadas("habilitadas")

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
    
    else: return redirect(url_for("error"))


@app.route("/categoria/novisible", methods=["GET","POST"])

def categoria_novisible():


    if session:

        if request.method == "POST":

            resultado = categorias_filtros_habilitadas("deshabilitadas")

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
    
    else: return redirect(url_for("error"))




@app.route("/provincia/index", methods=["GET","POST"])

def index_provincias():
    
    if session:
   
        resultado = mostrar_provincias()

        provincias = resultado[0]

        mensaje = resultado[1]

        return render_template("/provincia/index.html", provincias = provincias, mensaje=mensaje)

    else: return redirect(url_for("error"))

if __name__ == "__main__":
    app.run(debug=True)

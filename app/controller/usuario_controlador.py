from app.conexion import obtener_conexion

conn = obtener_conexion()
cursor = conn.cursor()

def insertar_usuario(fk_sucursal,nombre,email, contraseña,rol):    

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, ?, ?, ?, ?)",(fk_sucursal, nombre, email, contraseña, rol))    
    conn.commit()


def verificar_login(email, cont):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM USUARIO WHERE email = ? AND contraseña = ?", (email, cont))
    user = cursor.fetchone()

    conn.close()

    if user:
        return user
    else:
        return None

def get_nombresucursal_por_usuario(usuarioid):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT sucursal.nombre_sucursal AS nombre_sucursal FROM usuario JOIN sucursal ON usuario.fk_sucursal = sucursal.id_sucursal WHERE usuario.id_usuario = ?", (usuarioid,))
    sucursal = cursor.fetchone()

    if sucursal:
        nombre_sucursal = sucursal[0]
        return nombre_sucursal
from conexion import obtener_conexion

conn = obtener_conexion()
cursor = conn.cursor()

def insertar_usuario(fk_sucursal,nombre,email, contraseña,rol):    

    cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, ?, ?, ?, ?)",(fk_sucursal, nombre, email, contraseña, rol))    
    conn.commit()

insertar_usuario(1,"jose", "jsoaaae@gmail.com", "contraseña", "usuario")
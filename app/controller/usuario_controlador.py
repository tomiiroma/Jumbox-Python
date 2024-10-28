import sqlite3


def insertar_usuario(fk_sucursal,nombre,email, contraseña,rol):
    
    conn = sqlite3.connect('database.db')

# Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, ?, ?, ?, ?)",
        (fk_sucursal, nombre, email, contraseña, rol))    
    conn.commit()

insertar_usuario(1,"jose", "jsoaaae@gmail.com", "contraseña", "usuario")
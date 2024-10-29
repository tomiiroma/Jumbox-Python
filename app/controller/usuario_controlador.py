from db.conexion import obtener_conexion
import sqlite3


def insertar_usuario(fk_sucursal, nombre, email, contraseña, rol):
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, ?, ?, ?, ?)",
            (fk_sucursal, nombre, email, contraseña, rol)
        )
        conn.commit()
        print("Usuario insertado con éxito.")
    except sqlite3.IntegrityError:
        print("Error: El email ya está registrado.")
    finally:
        conn.close()
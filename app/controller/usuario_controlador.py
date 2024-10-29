from db.conexion import obtener_conexion
import sqlite3

def insertar_usuario(fk_sucursal, nombre, email, contraseña, rol):
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    try:
        # Verifica si el correo ya existe
        cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
        if cursor.fetchone():  # Si se encuentra un registro
            print("Error: El email ya está registrado.")
            return  # Sale de la función sin hacer el insert
        
        # Procede a insertar el nuevo usuario
        cursor.execute(
            "INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, ?, ?, ?, ?)",
            (fk_sucursal, nombre, email, contraseña, rol)
        )
        conn.commit()
        print("Usuario insertado con éxito.")
    except sqlite3.IntegrityError:
        print("Error: El email ya está registrado.")  # Se imprimirá si aún se da un error
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Manejo de cualquier otro error
    finally:
        conn.close()

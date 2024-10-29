from ..db.conexion import obtener_conexion


def agregar_categoria(nombre,estado):
    
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    try:
        
        cursor.execute("SELECT * FROM categoria WHERE nombre = ?",(nombre,))

        if cursor.fetchone():
            print("El nombre de la categoria ya se encuentra registrada.")
            return
        else:
            cursor.execute("INSERT INTO categoria (nombre,visible) values (?,?)",(nombre,estado))
            conn.commit()
            print("Categoria agregada.")

    
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Manejo de cualquier otro error
    finally:
        conn.close()



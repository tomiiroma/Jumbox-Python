from app.conexion import obtener_conexion

def selec_inventario(fk_sucursal):
        
    conn = obtener_conexion()

    cursor = conn.cursor()

    try:

        cursor.execute("SELECT id_inventario from inventario where fk_sucursal = ?",(fk_sucursal))

        resultado = cursor.fetchone()

        if resultado:

            return resultado
        
        else: 

            return "La sucursal no tiene inventario."
    
    except Exception as error:

        return "Ocurrio un error"+str(error)

    finally:

        cursor.close()
        conn.close()


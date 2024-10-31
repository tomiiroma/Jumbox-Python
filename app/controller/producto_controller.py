from app.conexion import obtener_conexion
from ..models.Producto import Producto


def agregar_producto(nombre, precio, marca, estado, descripcion, categoria_id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    try:


        cursor.execute("SELECT * FROM producto WHERE nombre = ?", (nombre,))
        if cursor.fetchone():
            print("El producto ya existe en el sistema.")
            return
        else:
            cursor.execute(
                "INSERT INTO producto (nombre, precio, marca, estado, descripcion, fk_categoria) VALUES (?, ?, ?, ?, ?, ?)",
                (nombre, precio, marca, estado, descripcion, categoria_id)
            )
            conn.commit()
            print("Producto agregado correctamente.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        cursor.close()
        conn.close()



def mostrar_productos():
    conn = obtener_conexion()
    cursor = conn.cursor()

    try:
        lista_productos = []

        cursor.execute("SELECT * FROM producto")
        filas = cursor.fetchall()

        for columna in filas:
            producto = Producto(
                idProducto=columna[0],
                nombre=columna[2],
                precio=columna[3],
                marca=columna[4],
                estado=bool(columna[5]),
                descripcion=columna[6],
                categoria=columna[1]  
            )
            lista_productos.append(producto)

        return lista_productos if filas else []
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        cursor.close()
        conn.close()

    

def actualizar_producto(id_producto, nombre=None, precio=None, marca=None, estado=None, descripcion=None, categoria_id=None):
    conn = obtener_conexion()
    cursor = conn.cursor()

    try:
        # Crear una lista para almacenar los campos a actualizar
        campos = []
        valores = []

        if nombre:
            campos.append("nombre = ?")
            valores.append(nombre)
        if precio:
            campos.append("precio = ?")
            valores.append(precio)
        if marca:
            campos.append("marca = ?")
            valores.append(marca)
        if estado is not None:
            campos.append("estado = ?")
            valores.append(int(estado))  # Convertir el estado a entero
        if descripcion:
            campos.append("descripcion = ?")
            valores.append(descripcion)
        if categoria_id:
            campos.append("fk_categoria = ?")
            valores.append(categoria_id)

        if campos:
            valores.append(id_producto)
            cursor.execute(f"UPDATE producto SET {', '.join(campos)} WHERE id_producto = ?", valores)
            conn.commit()
            print("Producto actualizado correctamente.")
        else:
            print("No se proporcionaron campos para actualizar.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        cursor.close()
        conn.close()


def deshabilitar_producto(id_producto):
    conn = obtener_conexion()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT estado FROM producto WHERE id_producto = ?", (id_producto,))
        fila = cursor.fetchone()

        if fila is not None:
            nuevo_estado = 0 if fila[0] == 1 else 1
            cursor.execute("UPDATE producto SET estado = ? WHERE id_producto = ?", (nuevo_estado, id_producto))
            conn.commit()
            print("Producto deshabilitado." if nuevo_estado == 0 else "Producto habilitado.")
        else:
            print("Producto no encontrado.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        cursor.close()
        conn.close()




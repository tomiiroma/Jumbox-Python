from app.conexion import obtener_conexion
from ..models.Producto import Producto


def agregar_producto(nombre, precio, marca, estado, descripcion, categoria_id,cantidad, url_imagen):
    conn = obtener_conexion()
    cursor = conn.cursor()

    try:


        cursor.execute("SELECT * FROM producto WHERE nombre = ?", (nombre,))
        if cursor.fetchone():
            print("El producto ya existe en el sistema.")
            return
        else:
            cursor.execute(
                "INSERT INTO producto (nombre, precio, marca, estado, descripcion,url_imagen, fk_categoria, cantidad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (nombre, precio, marca, estado, descripcion,url_imagen, categoria_id, cantidad)
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
                precio=columna[4],
                marca=columna[3],
                estado=columna[7],
                descripcion=columna[5],
                url_imagen = columna[6],
                categoria=columna[1],  
                cantidad=columna[8]
            )
            lista_productos.append(producto)

        return lista_productos if filas else []
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        cursor.close()
        conn.close()

    

def actualizar_producto(id_producto, nombre=None, precio=None, marca=None, estado=None, descripcion=None, categoria_id=None,cantidad=None):
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
            valores.append(estado)  
        if descripcion:
            campos.append("descripcion = ?")
            valores.append(descripcion)
        if categoria_id:
            campos.append("fk_categoria = ?")
            valores.append(categoria_id)           
        if cantidad is not None:
            campos.append("cantidad = ?")
            valores.append(cantidad)             


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
        cursor.execute('SELECT estado FROM producto WHERE id_producto = ?', (id_producto))
        fila = cursor.fetchone()

        print(fila[0])
        if fila:
            # Cambiamos el estado
            if fila[0] == '1':  # Si el estado es 1 (habilitado)
                cursor.execute("UPDATE producto SET estado = '0' WHERE id_producto = ?", (id_producto))
                conn.commit()
                return "Producto deshabilitado."
            else:  # Si el estado es 0 (deshabilitado)
                cursor.execute("UPDATE producto SET estado = '1' WHERE id_producto = ?", (id_producto))
                conn.commit()
                return "Producto habilitado."
        else:
            return "Error: producto no encontrado."
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Asegúrate de imprimir el error para depuración
        return "Ocurrió un error al cambiar el estado del producto."
    
    finally:
        cursor.close()
        conn.close()




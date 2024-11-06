from app.conexion import obtener_conexion
from ..models.Producto import Producto

def filtrar_productos_sucursal(fk_inventario):

    conn = obtener_conexion()

    cursor = conn.cursor()

    try:

        list_productos = []

        if isinstance(fk_inventario, tuple):

            fk_inventario = fk_inventario[0]
            print("el inventario es: "+str(fk_inventario))


            cursor.execute("SELECT producto.id_producto, producto.nombre, producto.precio, producto.marca, producto.estado,producto.descripcion, producto.fk_categoria, producto.cantidad, stock FROM detalle_inventario JOIN producto ON fk_producto = id_producto where fk_inventario = ?", (fk_inventario,))

            productos = cursor.fetchall()

            if productos:

                for producto in productos:

                    obj_producto = Producto(
                        idProducto=producto[0],
                        nombre=producto[1],
                        precio=producto[2],
                        marca=producto[3],
                        estado=producto[4],
                        descripcion=producto[5],
                        categoria=producto[6],
                        cantidad=producto[7])
                
                    list_productos.append(obj_producto)
                

            

                return list_productos

            else:

                return "El inventario no posee productos."

    except Exception as error:

        return "Ocurrio un error"+str(error)
    
    finally:
        cursor.close()
        conn.close()


def agregar_a_inventario(idproducto, fk_inventario):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT cantidad FROM PRODUCTO WHERE id_producto = ?", (idproducto, ))
    cantidadstock = cursor.fetchone()

    cantidadstock = cantidadstock[0]

    cursor.execute("INSERT INTO detalle_inventario (fk_inventario,fk_producto,stock,fecha_modificacion) VALUES (?,?,?, datetime('now'))", (fk_inventario, idproducto, cantidadstock))
    conn.commit()
    conn.close()




from app.conexion import obtener_conexion
from app.models.Sucursal import Sucursal

def get_sucursal():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT sucursal.id_sucursal, sucursal.nombre_sucursal, sucursal.fk_provincia, sucursal.localidad, 
               sucursal.calle, sucursal.altura, sucursal.telefono, provincia.nombre 
        FROM sucursal 
        JOIN provincia ON sucursal.fk_provincia = provincia.id_provincia
    ''')
    sucursales_db = cursor.fetchall()
    conn.close()
    
    sucursales = []
    for sucursal in sucursales_db:
        sucursales.append({
            'id_sucursal': sucursal[0],
            'nombre_sucursal': sucursal[1],
            'nombre_provincia': sucursal[7],
            'localidad': sucursal[3],
            'calle': sucursal[4],
            'altura': sucursal[5],
            'telefono': sucursal[6],
        })
        
    return sucursales


def get_inventario_por_sucursal(idsucursal):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT detalle_inventario.*, producto.* FROM detalle_inventario JOIN inventario ON detalle_inventario.fk_inventario = inventario.id_inventario JOIN producto ON detalle_inventario.fk_producto = producto.id_producto WHERE inventario.fk_sucursal = ? AND producto.estado = 1;", (idsucursal,))
    inventariodb = cursor.fetchall()
    inventarios = []

    for inventario in inventariodb:
        inventarios.append({
            'id_detalle_inventario': inventario[0],
            'fk_inventario': inventario[1],             
            'fk_producto': inventario[2],                   
            'stock': inventario[3],      
            'fecha_modificacion': inventario[4],              
            'id_producto': inventario[5],         
            'fk_categoria': inventario[6],
            'nombre_producto': inventario[7],
            'marca': inventario[8],
            'precio': inventario[9],
            'estado': inventario[10],
            'descripcion': inventario[11]
        })
        
    
    return inventarios


def mostrar_sucursales():

    try:

        lista_sucursal = []

        sucursales = get_sucursal()

        if sucursales:

            for sucursal in sucursales:

                obj_sucursal = Sucursal(
                    id_sucursal=sucursal['id_sucursal'],
                    nombre_sucursal=sucursal['nombre_sucursal'],
                    provincia=sucursal['nombre_provincia'],
                    localidad=sucursal['localidad'],
                    calle=sucursal['calle'],
                    altura=sucursal['altura'],
                    telefono=sucursal['telefono']
                )   
                lista_sucursal.append(obj_sucursal)

            return lista_sucursal

        else:

            return "No hay sucursales disponibles"
    
    except Exception as error:

            return "error: "+str(error)


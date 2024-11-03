from app.conexion import obtener_conexion

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
    cursor.execute("SELECT detalle_inventario.*, producto.* FROM detalle_inventario JOIN inventario ON detalle_inventario.fk_inventario = inventario.id_inventario JOIN producto ON detalle_inventario.fk_producto = producto.id_producto WHERE inventario.fk_sucursal = ?;", (idsucursal,))
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
            'descripcion': inventario[10]
        })
        
    
    return inventarios
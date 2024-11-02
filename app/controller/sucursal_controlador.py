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

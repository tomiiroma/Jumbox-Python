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
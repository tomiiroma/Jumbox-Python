from app.conexion import obtener_conexion
from app.models.Provincia import Provincia

def mostrar_provincias():

    conn = obtener_conexion()

    cursor = conn.cursor()



    try:

        cursor.execute("SELECT * FROM provincia")

        provincias = cursor.fetchall()

        lista_provincia = []

        if len(provincias)!=0:

            for provincia in provincias:

                obj_provincia = Provincia(id_provincia=provincia[0] , nombre=provincia[1] , visible=provincia[2])

                lista_provincia.append(obj_provincia)

            return lista_provincia,True

    except Exception as error:

            return [],False,"Error "+ str(error)
    
    finally:

        cursor.close()

        conn.close()



from app.conexion import obtener_conexion
from ..models.Categoria import Categoria

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
        print(f"Ocurrió un error: {e}")  
    finally:
        cursor.close()
        conn.close()


def mostrar_categorias():

    conn = obtener_conexion()
    cursor = conn.cursor()

    try:
        
        lista_categorias = []

        cursor.execute("SELECT * FROM categoria")

        filas = cursor.fetchall()

        for columna in filas:

            categoria = Categoria(id_categoria=columna[0], nombre=columna[1], visible=columna[2])
            
            lista_categorias.append(categoria)

        if len(filas) != 0:
            return lista_categorias
        else:
            return []
      
    except Exception as e:
        print(f"Ocurrió un error: {e}")  

        

    finally:
        cursor.close()
        conn.close()


def deshabilitar_categoria(id_categoria):

    conn = obtener_conexion()

    cursor = conn.cursor()

    try:

        cursor.execute('SELECT visible FROM categoria WHERE id_categoria = ?',(id_categoria,))

        fila = cursor.fetchone()

        if fila:
        
            if fila[0] == 1:
            
                cursor.execute("UPDATE categoria SET visible=0 where id_categoria = ?",(id_categoria))

                conn.commit()

                return "Categoria deshabilitada."

            else:

                cursor.execute("UPDATE categoria SET visible=1 WHERE id_categoria = ?",(id_categoria))

                conn.commit()

                return "Categoria habilitada"
            
        else:

                return "Error usuario no encontrado"
    
    except Exception:

            print("Ocurrio un error"+ str(Exception))

            return "Ocurrop un error"
    
    finally:

        cursor.close()

        conn.close()


def modificar_categoria(id_categoria,nuevo_nombre):

    conn = obtener_conexion()

    cursor = conn.cursor()

    try:

        cursor.execute("SELECT * from categoria where id_categoria = ?",(id_categoria))

        resultado = cursor.fetchone()

        if len(resultado)!=0:

            cursor.execute("UPDATE categoria SET nombre = ? where id_categoria = ?",(nuevo_nombre,id_categoria,))

            conn.commit()

            return "Categoria modificada."

        else:

            return "Categoria no encontrada"
        
    except Exception as e:

            return "Ocurrio un error"+str(e)
    
    finally:

        cursor.close()
        conn.close()
    

def filtrar_categoria(id_categoria):

    conn = obtener_conexion()

    cursor = conn.cursor()

    try:
        
        
        cursor.execute("SELECT * FROM categoria where id_categoria = ?",(id_categoria,))

        categoria = cursor.fetchone()

        obj_categoria = Categoria(id_categoria=categoria[0],nombre=categoria[1],visible=categoria[2])

        if categoria:

            return obj_categoria, "Categoría encontrada"
        
        else:

            return None, "No se ha encontrado la categoria"

    
    except Exception as error:

        print("Ocurrio un error"+str(error))
        
        return None, "Ocurrió un error: " + str(error)

    finally:

        cursor.close()
        conn.close()


def categorias_filtros_habilitadas(mensaje):

    conn = obtener_conexion()

    cursor = conn.cursor()

    lista_categoria = []

    try:

        if mensaje == "habilitadas":

            cursor.execute("SELECT * FROM categoria where visible=1")

        else:  

             #Categorias deshabilitadas

             cursor.execute("SELECT * FROM categoria where visible=0") 
            

        categorias = cursor.fetchall()

        if len(categorias) > 0:

            for categoria in categorias:

                obj_categoria = Categoria(id_categoria=categoria[0],nombre=categoria[1],visible=categoria[2])

                lista_categoria.append(obj_categoria)

            return lista_categoria, f"Se han filtrado las categorias {mensaje}."

        else:

            return None,f"No hay categorias {mensaje}."

    except Exception as error:

            return None,"Ocurrio un error" + str(error)
    
    finally:

        cursor.close()
        conn.close()




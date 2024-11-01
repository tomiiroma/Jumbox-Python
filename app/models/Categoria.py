import re

class Categoria:

    def __init__(self,id_categoria,nombre,visible):
        self.__id_categoria = id_categoria
        self.__nombre = nombre
        self.__visible = visible

    def get_nombre_categoria(self):
        return self.__nombre
    
    def get_id_categoria(self):
        return self.__id_categoria
    
    def get_visible(self):
        return self.__visible
    
    def set_nombre_categoria(self,nombre):
        if len(nombre)>0:

            self.__nombre = nombre

        else:

            print("El nombre de la categoria no es valido.")

    
    def set_visible(self,estado):

        if self.__visible == True:
            self.__visible = False

        else:

            self.__visible = True


    @staticmethod
    def validar_nombre(nombre):

        patron = r'^[A-Za-z\s]+$'

        if  re.match(patron,nombre):

          verificar_espacios = nombre.replace(" ","")

          if verificar_espacios:
                
        
              return True

        else: return False


    
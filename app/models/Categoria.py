import re

class Categoria:

    def __init__(self,id_categoria,nombre,visible):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.visible = visible

    def get_nombre_categoria(self):
        return self.nombre
    
    def get_id_categoria(self):
        return self.id_categoria
    
    def get_visible(self):
        return self.visible
    
    def set_nombre_categoria(self,nombre):
        if len(nombre)>0:

            self.nombre = nombre

        else:

            print("El nombre de la categoria no es valido.")

    
    def set_visible(self,estado):

        if self.visible == True:
            self.visible = False

        else:

            self.visible = True

    def validar_nombre(self,nombre):

        patron = r'^[A-Za-z\s]+$'

        if  re.match(patron,nombre):

          verificar_espacios = nombre.replace(" ","")

          if verificar_espacios:
                
        
              return True

        else: return False


    


class Categoria:

    def __init__(self,id_categoria,nombre,visible):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.visible = True

    def get_nombre_categoria(self):
        return self.nombre
    
    def get_id_categoria(self):
        return self.id_categoria
    
    def get_visible(self):
        return f"Estado: {self.visible}"
    
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


    
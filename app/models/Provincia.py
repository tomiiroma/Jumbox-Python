

class Provincia():

    def __init__(self,id_provincia,nombre,visible):

        self.__id_provincia = id_provincia
        self.__nombre = nombre
        self.__visible = visible

    
    def get_id_provincia(self):
        return  self.__id_provincia


    def get_nombre_provincia(self):
        return self.__nombre
    
    def get_visible(self):
        return self.__visible



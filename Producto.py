from typing import Any


class Producto:

    def __init__(self, nombre, precio, marca, estado, descripcion, categoria):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.estado = estado
        self.descripcion = descripcion
        self.categoria = categoria

    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def get_estado(self):
        return self.estado
    
    def get_marca(self):
        return self.marca
    
    def get_categoria(self):
        return self.categoria

    def set_categoria(self,categoria):
        self.categoria = categoria
        
    
    def set_nombre(self,nombre):
        self.nombre = nombre
        
    def set_precio(self,precio):
        self.precio = precio

    def set_marca(self,marca):
        self.marca = marca

    def set_descripcion(self,descripcion):
        self.descripcion = descripcion

    def set_estado(self,estado):
        if estado != True and estado != False:
            print("El estado solo acepta valores booleanos")
        else:
            self.estado = estado
    
    def to_string(self):
    
        
        if self.estado == True:
            estado_mensaje = "Disponible"
        else:
            estado_mensaje = "No disponible"

        toString = "\n"+"Información del Producto"+"\nProducto: "+self.nombre+"\nCategoria: "+self.categoria +"\nMarca: "+self.marca+"\nPrecio: "+str(self.precio)+"\nDescripcion: "+self.descripcion+"\nEstado: "+estado_mensaje

        return toString

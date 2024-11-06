# Para ejecutar los test, se debe colocar en la terminal el comando (     python -m test.validar_nombre_categoria       ), desde el directorio raiz
# Ejemplo ( C:\Users\Usuario\Desktop\python\Jumbox-Python> python -m test.validar_nombre_categoria )

import unittest

from app.models.Categoria import Categoria

class test_nombre_categoria(unittest.TestCase):

    def test_nombre_valido(self):

        nombre = "Electrodomesticos" # Nuevo nombre

        validacion = Categoria.validar_nombre(nombre)  # A la variable validacion se le pasa el return del metodo categoria a traves del metodo estatico validar_nombre()
        print("Nombre validado")
        self.assertTrue(validacion) # Se comprueba el resultado. En este caso deberia retornar verdadero
        
    
    def test_nombre_numerico(self):


        nombre = "1234" # Nombre inválido no permite números.

        validacion = Categoria.validar_nombre(nombre) 
        print("Nombre numerico invalidado")

        self.assertFalse(validacion)


    def test_nombre_caracteres_especiales(self):

        nombre = "Electrodomesticos'@" # Nombre inválido con caracteres especiales
        print("Nombre inválidado con caracteres especiales")

        validacion = Categoria.validar_nombre(nombre)

        self.assertFalse(validacion)

    
    def test_nombre_solo_espacios(self):

        nombre = "      " # Nombre inválido con espacios en blanco

        validacion = Categoria.validar_nombre(nombre)
        print("Nombre inválidado con espacios en blanco")
        self.assertFalse(validacion)


if __name__ == '__main__':
    unittest.main()
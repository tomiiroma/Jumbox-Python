# Para ejecutar los test, se debe colocar en la terminal el comando (     python -m test.validar_nombre_categoria       ), desde el directorio raiz
# Ejemplo ( C:\Users\Usuario\Desktop\python\Jumbox-Python> python -m test.validar_nombre_categoria )

import unittest

from app.models.Categoria import Categoria

class test_nombre_categoria(unittest.TestCase):

    def test_nombre_valido(self):

        categoria_test = Categoria(100,"Electrodonesticos",True) #Categoria a la cual se le quiere modificar el nombre

        nombre = "Electrodomesticos" # Nuevo nombre

        validacion = categoria_test.validar_nombre(nombre)  # A la variable validacion se le pasa el return del metodo categoria a traves de la instancia categoria_test

        self.assertTrue(validacion) # Se comprueba el resultado. En este caso deberia retornar verdadero

    
    def test_nombre_numerico(self):

        categoria_test = Categoria(100,"Electrodomesticos",True)

        nombre = "1234" # Nombre inválido no permite números.

        validacion = categoria_test.validar_nombre(nombre) 

        self.assertFalse(validacion)


    def test_nombre_caracteres_especiales(self):

        categoria_test = Categoria(100,"Electrodomesticos",True)

        nombre = "Electrodomesticos'@" # Nombre inválido con caracteres especiales

        validacion = categoria_test.validar_nombre(nombre)

        self.assertFalse(validacion)

    
    def test_nombre_solo_espacios(self):

        categoria_test = Categoria(100,"Electrodomesticos",True)

        nombre = "      " # Nombre inválido con espacios en blanco

        validacion = categoria_test.validar_nombre(nombre)

        self.assertFalse(validacion)


if __name__ == '__main__':
    unittest.main()
from typing import Optional

class Producto:
    def __init__(self, idProducto: int, nombre: str, precio: float, marca: str, estado: int, descripcion: str, categoria: str, cantidad: int):
        self._idProducto = idProducto
        self._nombre = nombre
        self._precio = precio
        self._marca = marca
        self._estado = estado  # Cambiado a int (0 o 1)
        self._descripcion = descripcion
        self._categoria = categoria
        self.cantidad = cantidad

    @property
    def idProducto(self) -> int:
        return self._idProducto

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, precio: float):
        self._precio = precio

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, marca: str):
        self._marca = marca

    @property
    def estado(self) -> int:  # Cambiado a int
        return self._estado

    @estado.setter
    def estado(self, estado: int):  # Cambiado a int
        if estado in (0, 1):  # Aceptar solo 0 o 1
            self._estado = estado
        else:
            print("El estado solo acepta 0 (deshabilitado) o 1 (habilitado).")

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        self._descripcion = descripcion

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: str):
        self._categoria = categoria

    def to_string(self) -> str:
        estado_mensaje = "Disponible" if self._estado == 1 else "No disponible"  # Usar comparación con int
        return (f"\nInformación del Producto\n"
                f"Producto: {self._nombre}\n"
                f"Categoría: {self._categoria}\n"
                f"Marca: {self._marca}\n"
                f"Precio: ${self._precio}\n"
                f"Descripción: {self._descripcion}\n"
                f"Estado: {estado_mensaje}")

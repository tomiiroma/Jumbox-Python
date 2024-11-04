import Sucursal as sucursal

class Inventario:
    def __init__(self, id_inventario, sucursal):
        self.id_inventario = id_inventario
        self._sucursal = sucursal


    def get_id_inventario(self):
        return self.id_inventario

    def set_id_inventario(self, id_inventario):
        self.id_inventario = id_inventario

    def get_sucursal(self):
        return self._sucursal

    def set_sucursal(self, sucursal):
        self._sucursal = sucursal
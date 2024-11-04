import Inventario as inventario
import Producto as producto

class DetalleInventario:
    def __init__(self, id_detalle_inventario, inventario, producto, stock, fecha_modificacion):
        self.id_detalle_inventario = id_detalle_inventario
        self._inventario = inventario 
        self._producto = producto     
        self.stock = stock
        self.fecha_modificacion = fecha_modificacion

    # Getters
    def get_id_detalle_inventario(self):
        return self.id_detalle_inventario

    def get_inventario(self):
        return self._inventario

    def get_producto(self):
        return self._producto

    def get_stock(self):
        return self.stock

    def get_fecha_modificacion(self):
        return self.fecha_modificacion

    # Setters
    def set_id_detalle_inventario(self, id_detalle_inventario):
        self.id_detalle_inventario = id_detalle_inventario

    def set_inventario(self, inventario):
        self._inventario = inventario

    def set_producto(self, producto):
        self._producto = producto

    def set_stock(self, stock):
        self.stock = stock

    def set_fecha_modificacion(self, fecha_modificacion):
        self.fecha_modificacion = fecha_modificacion

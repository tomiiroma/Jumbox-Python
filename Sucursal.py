class Sucursal:

    def __init__(self, id_sucursal, nombre_sucursal, provincia, localidad, calle,
                 altura,telefono):
        self.id_sucursal = id_sucursal
        self.nombre_sucursal = nombre_sucursal
        self.provincia = provincia
        self.localidad = localidad
        self.calle = calle
        self.altura = altura
        self.telefono = telefono


    # Getters
    def get_id_sucursal(self):
        return self.id_sucursal

    def get_nombre_sucursal(self):
        return self.nombre_sucursal

    def get_provincia(self):
        return self.provincia

    def get_localidad(self):
        return self.localidad

    def get_calle(self):
        return self.calle

    def get_altura(self):
        return self.altura

    def get_telefono(self):
        return self.telefono

    # Setters
    def set_id_sucursal(self, value):
        self.id_sucursal = value

    def set_nombre_sucursal(self, value):
        self.nombre_sucursal = value

    def set_provincia(self, value):
        self.provincia = value

    def set_localidad(self, value):
        self.localidad = value

    def set_calle(self, value):
        self.calle = value

    def set_altura(self, value):
        self.altura = value

    def set_telefono(self, value):
        self.telefono = value


        
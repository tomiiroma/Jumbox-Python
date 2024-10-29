import sqlite3

def obtener_conexion():
    """Establece y devuelve una conexión a la base de datos."""
    return sqlite3.connect('database.db')

def inicializar_bd():
    """Inicializa la base de datos y crea las tablas necesarias con datos iniciales."""
    conn = obtener_conexion()
    try:
        cursor = conn.cursor()

        # Crear tablas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS provincia (
            id_provincia INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            visible INTEGER NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sucursal (
            id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_sucursal TEXT NOT NULL,
            fk_provincia INTEGER,
            localidad TEXT NOT NULL,
            calle TEXT NOT NULL,
            altura INTEGER NOT NULL,
            telefono TEXT,
            FOREIGN KEY (fk_provincia) REFERENCES provincia (id_provincia)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_sucursal INTEGER,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL,
            rol TEXT NOT NULL,
            FOREIGN KEY (fk_sucursal) REFERENCES sucursal (id_sucursal)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS categoria (
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            visible INTEGER NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS producto (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_categoria INTEGER,
            nombre TEXT NOT NULL,
            marca TEXT NOT NULL,
            precio REAL NOT NULL,
            descripcion TEXT,
            estado TEXT NOT NULL,
            FOREIGN KEY (fk_categoria) REFERENCES categoria (id_categoria)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_sucursal INTEGER,
            FOREIGN KEY (fk_sucursal) REFERENCES sucursal (id_sucursal)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS detalle_inventario (
            id_detalle_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_inventario INTEGER,
            fk_producto INTEGER,
            stock INTEGER NOT NULL,
            fecha_modificacion TEXT NOT NULL,
            FOREIGN KEY (fk_inventario) REFERENCES inventario (id_inventario),
            FOREIGN KEY (fk_producto) REFERENCES producto (id_producto)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedido (
            id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_sucursal_origen INTEGER,
            fk_sucursal_destino INTEGER,
            fk_usuario INTEGER,
            FOREIGN KEY (fk_sucursal_origen) REFERENCES sucursal (id_sucursal),
            FOREIGN KEY (fk_sucursal_destino) REFERENCES sucursal (id_sucursal),
            FOREIGN KEY (fk_usuario) REFERENCES usuario (id_usuario)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS informacion_pedido (
            id_informacion_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_producto INTEGER,
            fk_pedido INTEGER,
            cantidad INTEGER NOT NULL,
            FOREIGN KEY (fk_producto) REFERENCES producto (id_producto),
            FOREIGN KEY (fk_pedido) REFERENCES pedido (id_pedido)
        )
        ''')

        # Inserciones en la tabla provincia
        provincias = [
            ('Buenos Aires', 1),
            ('CABA', 1),
            ('Santa Fe', 1),
            ('Córdoba', 1),
            ('Mendoza', 1)
        ]
        cursor.executemany("INSERT INTO provincia (nombre, visible) VALUES (?, ?)", provincias)

        # Obtener los IDs de las provincias insertadas
        cursor.execute("SELECT id_provincia FROM provincia")
        provincias_ids = cursor.fetchall()

        # Inserciones en la tabla sucursal
        sucursales = [
            ('Sucursal Centro', provincias_ids[0][0], 'Centro', 'Calle 1', 100, '011-1234-5678'),
            ('Sucursal Norte', provincias_ids[0][0], 'San Martín', 'Calle 2', 200, '011-2345-6789'),
            ('Sucursal Sur', provincias_ids[0][0], 'Avellaneda', 'Calle 3', 300, '011-3456-7890'),
            ('Sucursal Córdoba', provincias_ids[3][0], 'Córdoba', 'Calle 4', 400, '0351-1234-5678'),
            ('Sucursal Mendoza', provincias_ids[4][0], 'Mendoza', 'Calle 5', 500, '0261-2345-6789')
        ]
        cursor.executemany("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES (?, ?, ?, ?, ?, ?)", sucursales)

        # Obtener los IDs de las sucursales insertadas
        cursor.execute("SELECT id_sucursal FROM sucursal")
        sucursales_ids = cursor.fetchall()

        # Inserciones en la tabla usuario
        usuarios = [
            (sucursales_ids[0][0], 'Juan Pérez', 'juan.perez@example.com', 'contraseña123', 'admin'),
            (sucursales_ids[1][0], 'María Gómez', 'maria.gomez@example.com', 'contraseña123', 'usuario'),
            (sucursales_ids[2][0], 'Luis Rodríguez', 'luis.rodriguez@example.com', 'contraseña123', 'usuario')
        ]
        cursor.executemany("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, ?, ?, ?, ?)", usuarios)

        # Inserciones en la tabla categoria
        categorias = [
            ('Lácteos', 1),
            ('Bebidas', 1),
            ('Snacks', 1)
        ]
        cursor.executemany("INSERT INTO categoria (nombre, visible) VALUES (?, ?)", categorias)

        # Obtener los IDs de las categorías insertadas
        cursor.execute("SELECT id_categoria FROM categoria")
        categorias_ids = cursor.fetchall()

        # Inserciones en la tabla producto
        productos = [
            (categorias_ids[0][0], 'Leche Entera', 'La Serenísima', 80.0, 'Leche entera de 1 litro', 'disponible'),
            (categorias_ids[1][0], 'Cerveza', 'Quilmes', 120.0, 'Cerveza rubia de 1 litro', 'disponible'),
            (categorias_ids[2][0], 'Galletitas', 'Pepito', 50.0, 'Galletitas dulces de 200 gramos', 'disponible')
        ]
        cursor.executemany("INSERT INTO producto (fk_categoria, nombre, marca, precio, descripcion, estado) VALUES (?, ?, ?, ?, ?, ?)", productos)

        # Inserciones en la tabla inventario
        inventarios = [(sucursales_ids[0][0],), (sucursales_ids[1][0],), (sucursales_ids[2][0],)]
        cursor.executemany("INSERT INTO inventario (fk_sucursal) VALUES (?)", inventarios)

        # Obtener los IDs de los inventarios insertados
        cursor.execute("SELECT id_inventario FROM inventario")
        inventarios_ids = cursor.fetchall()

        # Inserciones en la tabla detalle_inventario
        detalle_inventarios = [
            (inventarios_ids[0][0], productos[0][0], 50, '2024-01-01'),
            (inventarios_ids[1][0], productos[1][0], 30, '2024-01-02'),
            (inventarios_ids[2][0], productos[2][0], 20, '2024-01-03')
        ]
        cursor.executemany("INSERT INTO detalle_inventario (fk_inventario, fk_producto, stock, fecha_modificacion) VALUES (?, ?, ?, ?)", detalle_inventarios)

        # Inserciones en la tabla pedido
        pedidos = [
            (sucursales_ids[0][0], sucursales_ids[1][0], usuarios[0][0]),
            (sucursales_ids[1][0], sucursales_ids[2][0], usuarios[1][0])
        ]
        cursor.executemany("INSERT INTO pedido (fk_sucursal_origen, fk_sucursal_destino, fk_usuario) VALUES (?, ?, ?)", pedidos)

        # Inserciones en la tabla informacion_pedido
        informacion_pedidos = [
            (productos[0][0], 1, 10),
            (productos[1][0], 1, 5),
            (productos[2][0], 2, 2)
        ]
        cursor.executemany("INSERT INTO informacion_pedido (fk_producto, fk_pedido, cantidad) VALUES (?, ?, ?)", informacion_pedidos)

        # Guardar cambios
        conn.commit()

    except sqlite3.Error as e:
        print("Error al inicializar la base de datos:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    inicializar_bd()

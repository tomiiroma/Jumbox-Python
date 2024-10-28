import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('database.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear las tablas
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
cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Buenos Aires', 1)")
cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('CABA', 1)")
cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Santa Fe', 1)")
cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Córdoba', 1)")
cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Mendoza', 1)")

# Obtener los IDs de las provincias insertadas
cursor.execute("SELECT id_provincia FROM provincia")
provincias = cursor.fetchall()

# Inserciones en la tabla sucursal
cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Centro', ?, 'Centro', 'Calle 1', 100, '011-1234-5678')", (provincias[0][0],))
cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Norte', ?, 'San Martín', 'Calle 2', 200, '011-2345-6789')", (provincias[0][0],))
cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Sur', ?, 'Avellaneda', 'Calle 3', 300, '011-3456-7890')", (provincias[0][0],))
cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Córdoba', ?, 'Córdoba', 'Calle 4', 400, '0351-1234-5678')", (provincias[3][0],))
cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Mendoza', ?, 'Mendoza', 'Calle 5', 500, '0261-2345-6789')", (provincias[4][0],))

# Obtener los IDs de las sucursales insertadas
cursor.execute("SELECT id_sucursal FROM sucursal")
sucursales = cursor.fetchall()

# Inserciones en la tabla usuario
cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, 'Juan Pérez', 'juan.perez@example.com', 'contraseña123', 'admin')", (sucursales[0][0],))
cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, 'María Gómez', 'maria.gomez@example.com', 'contraseña123', 'usuario')", (sucursales[1][0],))
cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (?, 'Luis Rodríguez', 'luis.rodriguez@example.com', 'contraseña123', 'usuario')", (sucursales[2][0],))

# Inserciones en la tabla categoria
cursor.execute("INSERT INTO categoria (nombre, visible) VALUES ('Lácteos', 1)")
cursor.execute("INSERT INTO categoria (nombre, visible) VALUES ('Bebidas', 1)")
cursor.execute("INSERT INTO categoria (nombre, visible) VALUES ('Snacks', 1)")

# Obtener los IDs de las categorías insertadas
cursor.execute("SELECT id_categoria FROM categoria")
categorias = cursor.fetchall()

# Inserciones en la tabla producto
cursor.execute("INSERT INTO producto (fk_categoria, nombre, marca, precio, descripcion, estado) VALUES (?, 'Leche Entera', 'La Serenísima', 80.0, 'Leche entera de 1 litro', 'disponible')", (categorias[0][0],))
cursor.execute("INSERT INTO producto (fk_categoria, nombre, marca, precio, descripcion, estado) VALUES (?, 'Cerveza', 'Quilmes', 120.0, 'Cerveza rubia de 1 litro', 'disponible')", (categorias[1][0],))
cursor.execute("INSERT INTO producto (fk_categoria, nombre, marca, precio, descripcion, estado) VALUES (?, 'Galletitas', 'Pepito', 50.0, 'Galletitas dulces de 200 gramos', 'disponible')", (categorias[2][0],))

# Inserciones en la tabla inventario
cursor.execute("INSERT INTO inventario (fk_sucursal) VALUES (?)", (sucursales[0][0],))
cursor.execute("INSERT INTO inventario (fk_sucursal) VALUES (?)", (sucursales[1][0],))
cursor.execute("INSERT INTO inventario (fk_sucursal) VALUES (?)", (sucursales[2][0],))

# Obtener los IDs de los inventarios insertados
cursor.execute("SELECT id_inventario FROM inventario")
inventarios = cursor.fetchall()

# Inserciones en la tabla detalle_inventario
cursor.execute("INSERT INTO detalle_inventario (fk_inventario, fk_producto, stock, fecha_modificacion) VALUES (?, ?, 50, '2024-01-01')", (inventarios[0][0], categorias[0][0]))
cursor.execute("INSERT INTO detalle_inventario (fk_inventario, fk_producto, stock, fecha_modificacion) VALUES (?, ?, 30, '2024-01-02')", (inventarios[1][0], categorias[1][0]))
cursor.execute("INSERT INTO detalle_inventario (fk_inventario, fk_producto, stock, fecha_modificacion) VALUES (?, ?, 20, '2024-01-03')", (inventarios[2][0], categorias[2][0]))

# Inserciones en la tabla pedido
cursor.execute("INSERT INTO pedido (fk_sucursal_origen, fk_sucursal_destino, fk_usuario) VALUES (?, ?, ?)", (sucursales[0][0], sucursales[1][0], 1))
cursor.execute("INSERT INTO pedido (fk_sucursal_origen, fk_sucursal_destino, fk_usuario) VALUES (?, ?, ?)", (sucursales[1][0], sucursales[2][0], 2))

# Obtener los IDs de los pedidos insertados
cursor.execute("SELECT id_pedido FROM pedido")
pedidos = cursor.fetchall()

# Inserciones en la tabla informacion_pedido
cursor.execute("INSERT INTO informacion_pedido (fk_producto, fk_pedido, cantidad) VALUES (?, ?, 10)", (categorias[0][0], pedidos[0][0]))
cursor.execute("INSERT INTO informacion_pedido (fk_producto, fk_pedido, cantidad) VALUES (?, ?, 5)", (categorias[1][0], pedidos[1][0]))


# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Tablas creadas exitosamente.")

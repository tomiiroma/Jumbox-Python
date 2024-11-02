import sqlite3

# Conectar a la base de datos (se creará si no existe)
def obtener_conexion():
    conn = sqlite3.connect('jumbox.db')
    return conn

# Crear las tablas
def iniciar_db():
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Crear las tablas
    cursor.execute('''CREATE TABLE IF NOT EXISTS provincia (
        id_provincia INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        visible INTEGER NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sucursal (
        id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_sucursal TEXT NOT NULL,
        fk_provincia INTEGER,
        localidad TEXT NOT NULL,
        calle TEXT NOT NULL,
        altura INTEGER NOT NULL,
        telefono TEXT,
        FOREIGN KEY (fk_provincia) REFERENCES provincia (id_provincia)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_sucursal INTEGER,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        contraseña TEXT NOT NULL,
        rol TEXT NOT NULL,
        FOREIGN KEY (fk_sucursal) REFERENCES sucursal (id_sucursal)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        visible INTEGER NOT NULL
    )''')

    # Modificar la tabla producto para incluir la columna cantidad
    cursor.execute('''CREATE TABLE IF NOT EXISTS producto(
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_categoria INTEGER,
        nombre TEXT NOT NULL,
        marca TEXT NOT NULL,
        precio REAL NOT NULL,
        descripcion TEXT,
        estado TEXT NOT NULL,
        cantidad INTEGER NOT NULL,  -- Nueva columna
        FOREIGN KEY (fk_categoria) REFERENCES categoria (id_categoria)
    )''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS inventario (
        id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_sucursal INTEGER,
        FOREIGN KEY (fk_sucursal) REFERENCES sucursal (id_sucursal)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS detalle_inventario (
        id_detalle_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_inventario INTEGER,
        fk_producto INTEGER,
        stock INTEGER NOT NULL,
        fecha_modificacion TEXT NOT NULL,
        FOREIGN KEY (fk_inventario) REFERENCES inventario (id_inventario),
        FOREIGN KEY (fk_producto) REFERENCES producto (id_producto)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pedido (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_sucursal_origen INTEGER,
        fk_sucursal_destino INTEGER,
        fk_usuario INTEGER,
        FOREIGN KEY (fk_sucursal_origen) REFERENCES sucursal (id_sucursal),
        FOREIGN KEY (fk_sucursal_destino) REFERENCES sucursal (id_sucursal),
        FOREIGN KEY (fk_usuario) REFERENCES usuario (id_usuario)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS informacion_pedido (
        id_informacion_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_producto INTEGER,
        fk_pedido INTEGER,
        cantidad INTEGER NOT NULL,
        FOREIGN KEY (fk_producto) REFERENCES producto (id_producto),
        FOREIGN KEY (fk_pedido) REFERENCES pedido (id_pedido)
    )''')

    # Insertar datos iniciales si las tablas están vacías
    if cursor.execute("SELECT COUNT(*) FROM PROVINCIA").fetchone()[0] == 0:
        cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Buenos Aires', 1)")
        cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('CABA', 1)")
        cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Santa Fe', 1)")
        cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Córdoba', 1)")
        cursor.execute("INSERT INTO provincia (nombre, visible) VALUES ('Mendoza', 1)")

    if cursor.execute("SELECT COUNT(*) FROM SUCURSAL").fetchone()[0] == 0:
        cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Centro', 2, 'Centro', 'Calle 1', 100, '011-1234-5678')") 
        cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Norte', 3, 'San Martín', 'Calle 2', 200, '011-2345-6789')")
        cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Sur', 1, 'Avellaneda', 'Calle 3', 300, '011-3456-7890')") 
        cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Córdoba', 4, 'Córdoba', 'Calle 4', 400, '0351-1234-5678')")
        cursor.execute("INSERT INTO sucursal (nombre_sucursal, fk_provincia, localidad, calle, altura, telefono) VALUES ('Sucursal Mendoza', 5, 'Mendoza', 'Calle 5', 500, '0261-2345-6789')") 

    if cursor.execute("SELECT COUNT(*) FROM USUARIO").fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (1, 'Juan Pérez', 'juan.perez@example.com', 'contraseña123', 'admin')")
        cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (2, 'María Gómez', 'maria.gomez@example.com', 'contraseña123', 'usuario')")
        cursor.execute("INSERT INTO usuario (fk_sucursal, nombre, email, contraseña, rol) VALUES (3, 'Luis Rodríguez', 'luis.rodriguez@example.com', 'contraseña123', 'usuario')")

    # Guardar (commit) los cambios
    conn.commit()

    # Cerrar la conexión
    conn.close()

    print("Tablas creadas y modificadas exitosamente.")

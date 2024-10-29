from .conexion import obtener_conexion

def inicializar_bd():
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Crear tabla de usuario si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_sucursal INTEGER,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        contraseña TEXT NOT NULL,
        rol TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
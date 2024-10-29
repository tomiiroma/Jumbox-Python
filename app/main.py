from db.base_datos import inicializar_bd
from controller.usuario_controlador import insertar_usuario

if __name__ == '__main__':
    inicializar_bd()  # Inicializa la base de datos y crea las tablas

    # Ejemplo de insertar un usuario
    insertar_usuario(1, "Dani", "dani@davinci.com", "contraseña123", "admin")
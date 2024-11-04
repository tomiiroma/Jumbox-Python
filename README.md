# Jumbox - Plataforma de Gestión de Inventarios en Supermercados

### Descripción
**Jumbox** es un sistema de gestión diseñado para una cadena de supermercados. La plataforma permite administrar productos, categorías, inventario y gestionar pedidos y transferencias entre sucursales. Su objetivo principal es mejorar la comunicación entre sucursales, mantener el inventario actualizado y facilitar el manejo de pedidos de forma rápida y eficaz.

---


### Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **app/**: Contiene los controladores, modelos y la conexión a la base de datos (SQLite3).
- **static/**: Carpeta de estilos CSS para la aplicación.
- **templates/**: Contiene los archivos HTML utilizados en la interfaz de usuario.
- **tests/**: Contiene las pruebas unitarias del sistema.
- **main.py**: Archivo principal que se ejecuta para iniciar la aplicación; define todas las rutas del sistema.

---


### Funcionalidades Clave

1. **Gestión de productos**: Permite agregar, editar y eliminar productos, asociándolos a categorías específicas.
   
2. **Gestión de categorías**: Creación, modificación y eliminación de categorías de productos para su mejor organización.

3. **Inventario en tiempo real**: Visualización actualizada del inventario de cada sucursal para optimizar el control de stock.

4. **Transferencia de productos entre sucursales**: Comunicación y transferencia de productos entre tiendas, equilibrando la disponibilidad de inventario.

5. **Gestión de pedidos**: Creación, modificación, confirmación y cancelación de pedidos, con un historial para mejorar las operaciones de abastecimiento.

---

### Estado Actual del Proyecto

El proyecto está en fase de desarrollo del **MVP (Producto Mínimo Viable)**. Las carpetas y estructura iniciales están configuradas, y se ha implementado la conexión a la base de datos con SQLite3.

---

### Backlog de Tareas (Trello)

Actualmente, las tareas en proceso para completar el MVP son:

- **Login**
- **Registrar Usuario**
- **Agregar Producto**
- **Eliminar Producto**
- **Editar Producto**
- **Agregar Categoría**
- **Eliminar Categoría**
- **Editar Categoría**
- **Visualizar Inventario**
- **Realizar Pedido**
- **Cancelar Pedido**
- **Confirmar Orden de Pedido**

[Acceder al Backlog en Trello](https://trello.com/invite/b/66e81fbbdd986ae76be41432/ATTI316dd4aa424008233ab8e7e63e6db5448F102F17/trabajo-python)


---


### GitHub y Versionado

- El proyecto está gestionado mediante GitHub, con control de versiones para registrar cambios importantes en la estructura y desarrollo del sistema.
- El primer commit incluye la configuración de las carpetas base, la estructura de la base de datos y el esquema de rutas inicial.

---

### Documentación del Proyecto

Para una descripción detallada de los requisitos y especificaciones del sistema, consulta el documento **SRS 1.1**: 
[Especificación de Requisitos del Software (SRS) 1.1](https://docs.google.com/document/d/1NW1u7IR9rL5aLbes2KhzWpooiADpHZZXL9GZh_jC1Ac/edit?usp=sharing)

---

### Próximos pasos

- Completar las tareas del MVP mencionadas en el backlog.
- Realizar pruebas de las funcionalidades implementadas para asegurar una correcta gestión del inventario, pedidos y flujo de usuarios.

---
**Diagramas**

**Diagrama Entidad-Relación**: Se está trabajando en el diseño de la base de datos para representar las relaciones entre productos, categorías y sucursales.
[Visualizar Diagrama](https://drive.google.com/file/d/1xe1qN12Ag5GsJhHbZIETTuqzBWr5H9Tt/view?usp=sharing)

Diagrama de Flujo de Creación de Productos: Este diagrama describirá el proceso para agregar nuevos productos al sistema y cómo se relacionan con las categorías existentes.
[Visualizar Diagrama](https://drive.google.com/file/d/18f7bv5xovs5DMgGNtxE6sXY1eDpMWt4O/view?usp=sharing)


Diagrama de Flujo de Creación de Categorías: Este diagrama mostrará el proceso paso a paso para agregar y gestionar categorías dentro del sistema.
[Visualizar Diagrama](https://drive.google.com/file/d/1lrYm0kE8UjbqD7Qw6xXH3JdOS3DqIzvB/view?usp=sharing)



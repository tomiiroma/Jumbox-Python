# Jumbox - Plataforma de Gestión de Inventarios en Supermercados

### Descripción

**Jumbox** es un sistema de gestión diseñado para una cadena de supermercados. La plataforma permite administrar productos, categorías, inventario y gestionar pedidos y transferencias entre sucursales. Su objetivo principal es mejorar la comunicación entre sucursales, mantener el inventario actualizado y facilitar el manejo de pedidos de forma rápida y eficaz.

Este proyecto es un trabajo práctico de la materia **Análisis y Metodología de Sistemas** desarrollado por:

- **Agustín Agüero**
- **Daniel Fernández**
- **Tomás Roma**

---

### Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **app/**: Contiene los controladores, modelos y la conexión a la base de datos (**SQLite3**).
- **static/**: Archivos de estilos CSS para la aplicación.
- **templates/**: Contiene los archivos HTML utilizados en la interfaz de usuario.
- **tests/**: Pruebas unitarias del sistema.
- **main.py**: Archivo principal que define las rutas del sistema y ejecuta la aplicación.

---

### Funcionalidades Clave

1. **Gestión de productos**
   - Agregar, editar y eliminar productos.
   - Asociar productos a categorías específicas.

2. **Gestión de categorías**
   - Crear, modificar y eliminar categorías para organizar productos.

3. **Inventario en tiempo real**
   - Visualización actualizada del stock en cada sucursal.

4. **Transferencia de productos entre sucursales**
   - Comunicación entre tiendas para equilibrar el inventario.

5. **Gestión de pedidos**
   - Crear, confirmar, modificar y cancelar pedidos.
   - Consultar historial de pedidos realizados.

---

### Estado Actual del Proyecto

El sistema está en la fase de desarrollo del **MVP (Producto Mínimo Viable)**. Se ha implementado la conexión a la base de datos y la estructura inicial de carpetas, junto con algunas funcionalidades básicas.

---

### Backlog de Tareas (Trello)

Actualmente, las tareas prioritarias del MVP son:

- **Usuarios**
  - Login
  - Registro de usuarios

- **Gestión de productos**
  - Agregar, editar y eliminar productos.

- **Gestión de categorías**
  - Crear, modificar y eliminar categorías.

- **Inventario y pedidos**
  - Visualizar inventario.
  - Realizar, cancelar y confirmar pedidos.

[Acceder al Backlog en Trello](https://trello.com/invite/b/66e81fbbdd986ae76be41432/ATTI316dd4aa424008233ab8e7e63e6db5448F102F17/trabajo-python)

---

### GitHub y Versionado

El proyecto está gestionado en GitHub, utilizando control de versiones para documentar cambios importantes.

- **Primer commit**: Configuración inicial de carpetas, base de datos y rutas principales.

---

### Documentación del Proyecto

- **Especificación de Requisitos (SRS 1.1)**:  
  [Ver documento](https://docs.google.com/document/d/1NW1u7IR9rL5aLbes2KhzWpooiADpHZZXL9GZh_jC1Ac/edit?usp=sharing)

---

### Diagramas

1. **Diagrama Entidad-Relación**  
   Representa las relaciones entre productos, categorías y sucursales.  
   [Visualizar diagrama](https://drive.google.com/file/d/1xe1qN12Ag5GsJhHbZIETTuqzBWr5H9Tt/view?usp=sharing)

2. **Diagrama de Flujo: Creación de Productos**  
   Describe el proceso para agregar nuevos productos y asociarlos a categorías.  
   [Visualizar diagrama](https://drive.google.com/file/d/18f7bv5xovs5DMgGNtxE6sXY1eDpMWt4O/view?usp=sharing)

3. **Diagrama de Flujo: Creación de Categorías**  
   Explica el proceso para agregar y gestionar categorías dentro del sistema.  
   [Visualizar diagrama](https://drive.google.com/file/d/1lrYm0kE8UjbqD7Qw6xXH3JdOS3DqIzvB/view?usp=sharing)

---

### Próximos pasos

1. Completar las tareas pendientes del MVP.
2. Realizar pruebas unitarias para validar las funcionalidades implementadas.
3. Ampliar el sistema con nuevas funcionalidades tras el MVP, como reportes de inventario y métricas de pedidos.

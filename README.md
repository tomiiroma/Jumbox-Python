#  Jumbox
####  Plataforma de Gestión de Inventarios en Supermercados

Este proyecto consiste en el desarrollo de un sistema de gestión para una cadena de supermercados. El sistema permite la administración de productos, categorías, inventario, y la gestión de pedidos y transferencias entre las diferentes sucursales. El objetivo principal del proyecto es proporcionar una herramienta eficiente para que las sucursales puedan comunicar sus necesidades de productos, mantener el inventario actualizado, y gestionar los pedidos de forma rápida y sencilla.



#####   El sistema está dividido en varias funcionalidades clave, que incluyen:

1. **Gestión de productos**: Permite agregar, eliminar y modificar productos en el sistema. Cada producto puede estar asociado a una categoría específica para facilitar su organización.

3. **Gestión de categorías**: Los productos pueden clasificarse en diferentes categorías, y el sistema permite agregar, modificar o eliminar estas categorías según sea necesario.

5. **Inventario en tiempo real**: Cada sucursal puede ver su propio inventario en tiempo real, lo que facilita la gestión del stock y ayuda a evitar sobrecargas o desabastecimientos.

7. **Transferencia de productos entre sucursales**: Las sucursales pueden solicitar productos entre ellas, facilitando la comunicación y el traspaso de mercancía para mantener el equilibrio en el inventario.

9. **Gestión de pedidos**: Las sucursales pueden crear, modificar y eliminar pedidos, manteniendo un historial de los mismos para mejorar la eficiencia de las operaciones.


El proyecto se está desarrollando utilizando Python como lenguaje principal, y el control de versiones se maneja a través de GitHub para asegurar un desarrollo colaborativo y bien organizado. A lo largo del proceso se mantiene la documentación actualizada para reflejar el estado y los avances del proyecto.


------------


####  Estado Actual del Proyecto:

Actualmente, el proyecto se encuentra en una fase inicial de desarrollo. A continuación, se detallan los avances y las funcionalidades implementadas hasta la fecha:

**Estado Actual del Proyecto**:
Actualmente, el proyecto se encuentra en una fase inicial de desarrollo. A continuación, se detallan los avances y las funcionalidades implementadas hasta la fecha:

**Clases implementadas**:

**Clase Producto**: Esta clase permite gestionar la información básica de los productos del supermercado. Los atributos de la clase incluyen:

- nombre
- precio
- marca
- estado (disponible/no disponible)
- descripción
- categoría

------------


**Backlog de Tareas (Trello)**
Las siguientes tareas están en progreso y pueden ser consultadas en el backlog de Trello:

-  Diagrama de clases
-  Diagrama de flujo de datos
-  Diagrama entidad-relación
-  Creación de la base de datos
-  Implementación de funcionalidades adicionales
- Diagrama de flujo de creación de categorías
- Diagrama de flujo de creación de productos

[Acceder a Trello](https://trello.com/invite/b/66e81fbbdd986ae76be41432/ATTI316dd4aa424008233ab8e7e63e6db5448F102F17/trabajo-python)


------------

**GitHub y versionado**:

- El proyecto ha sido subido a GitHub y ya cuenta con la primera versión, que incluye la estructura básica del sistema y la implementación de las clases mencionadas.
- Se ha utilizado control de versiones para registrar cambios importantes en la estructura del código y las primeras funcionalidades.

------------
**Diagramas**

**Diagrama Entidad-Relación**: Se está trabajando en el diseño de la base de datos para representar las relaciones entre productos, categorías y sucursales.
[Visualizar Diagrama](https://drive.google.com/file/d/1xe1qN12Ag5GsJhHbZIETTuqzBWr5H9Tt/view?usp=sharing)

Diagrama de Flujo de Creación de Productos: Este diagrama describirá el proceso para agregar nuevos productos al sistema y cómo se relacionan con las categorías existentes.
[Visualizar Diagrama](https://drive.google.com/file/d/18f7bv5xovs5DMgGNtxE6sXY1eDpMWt4O/view?usp=sharing)


Diagrama de Flujo de Creación de Categorías: Este diagrama mostrará el proceso paso a paso para agregar y gestionar categorías dentro del sistema.
[Visualizar Diagrama](https://drive.google.com/file/d/1lrYm0kE8UjbqD7Qw6xXH3JdOS3DqIzvB/view?usp=sharing)

------------


**Base de Datos**
La base de datos del sistema se llama jumbox y está diseñada para almacenar información relacionada con productos, categorías, inventarios, pedidos y sucursales. A continuación se presenta el script SQL utilizado para crear la estructura de la base de datos.

[Descargar SQL Dump](https://drive.google.com/file/d/1WYIBmXtLGFdGlk3vvCorVcRKfQR4wgtM/view?usp=sharing)

[Visualizar Tablas de la Base de Datos](https://docs.google.com/spreadsheets/d/1cNVlbS90rQW3PqvcyU2LpM1sm1Ki76bpymOZKNxrplU/edit?usp=sharing)


------------

**Próximos pasos**:

- Implementar la funcionalidad de crear,agregar,editar,eliminar productos.
- Implementar la funcionalidad de crear,agregar,editar,eliminar  categorias.
- Implementar la funcionalidad de transferencia de productos entre sucursales.
- Desarrollar la clase Pedido para gestionar los pedidos entre sucursales.
- Realizar pruebas de las funcionalidades ya implementadas para asegurar la correcta gestión del inventario y productos.

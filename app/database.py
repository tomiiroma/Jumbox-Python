-- Estructura de tabla para la tabla `categoria`
CREATE TABLE categoria (
  id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  visible INTEGER NOT NULL
);

--Estructura de tabla para la tabla `detalle_inventario`
CREATE TABLE detalle_inventario (
  id_detalle_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_inventario INTEGER,
  fk_producto INTEGER,
  fecha_modificacion TEXT NOT NULL,
  stock INTEGER NOT NULL,
  FOREIGN KEY (fk_inventario) REFERENCES inventario (id_inventario),
  FOREIGN KEY (fk_producto) REFERENCES producto (id_producto)
);

-- Estructura de tabla para la tabla `informacion_pedido`
CREATE TABLE informacion_pedido (
  id_informacion_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_producto INTEGER,
  fk_pedido INTEGER,
  cantidad INTEGER NOT NULL,
  FOREIGN KEY (fk_producto) REFERENCES producto (id_producto),
  FOREIGN KEY (fk_pedido) REFERENCES pedido (id_pedido)
);

-- Estructura de tabla para la tabla `inventario`
CREATE TABLE inventario (
  id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_sucursal INTEGER,
  FOREIGN KEY (fk_sucursal) REFERENCES sucursal (id_sucursal)
);

-- Estructura de tabla para la tabla `pedido`
CREATE TABLE pedido (
  id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_sucursal_origen INTEGER,
  fk_sucursal_destino INTEGER,
  FOREIGN KEY (fk_sucursal_origen) REFERENCES sucursal (id_sucursal),
  FOREIGN KEY (fk_sucursal_destino) REFERENCES sucursal (id_sucursal)
);

-- Estructura de tabla para la tabla `producto`
CREATE TABLE producto (
  id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_categoria INTEGER,
  marca TEXT NOT NULL,
  precio REAL NOT NULL,
  descripcion TEXT,
  estado TEXT NOT NULL,
  FOREIGN KEY (fk_categoria) REFERENCES categoria (id_categoria)
);

-- Estructura de tabla para la tabla `provincia`
CREATE TABLE provincia (
  id_provincia INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  visible INTEGER NOT NULL
);

-- Estructura de tabla para la tabla `sucursal`
CREATE TABLE sucursal (
  id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre_sucursal TEXT NOT NULL,
  fk_provincia INTEGER,
  localidad TEXT NOT NULL,
  calle TEXT NOT NULL,
  altura INTEGER NOT NULL,
  telefono TEXT,
  FOREIGN KEY (fk_provincia) REFERENCES provincia (id_provincia)
);


import sqlite3


conn = sqlite3.connect('jumbox.db')

cursor = conn.cursor()

#cursor.execute("INSERT INTO inventario (fk_sucursal) VALUES (2)")
cursor.execute("INSERT INTO detalle_inventario(fk_inventario, fk_producto, stock, fecha_modificacion) VALUES (1,1,20,'3-11-24')")

conn.commit()

conn.close()
import sqlite3
from datetime import datetime

# Conecta a la base de datos o créala si no existe
conexion = sqlite3.connect("BASEPROYECTO.db")

try:
    conexion.execute("""CREATE TABLE IF NOT EXISTS grabaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor TEXT,
        fecha TEXT,
        Mag1 REAL,
        Escala1 REAL,
        Mag2 REAL,
        Escala2 REAL
    )""")
    print("Se creó la tabla grabaciones")
except sqlite3.OperationalError:
    print("La tabla grabaciones ya existe")

# Función para insertar una grabación
def insertar_grabacion(autor, Mag1, Escala1, Mag2, Escala2):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO grabaciones (autor, fecha, canal, unidades_fisicas, vector_datos) VALUES (?, ?, ?, ?, ?)",
                       (autor, Mag1, Escala1, Mag2, Escala2))
        conexion.commit()
        print("Grabación insertada con éxito.")
    except Exception as e:
        print("Error al insertar la grabación:", str(e))
        conexion.rollback()

# Ejemplo de uso para insertar una grabación
autor = "Alexander"
Mag1 = 1
Escala1 = 0.5
Mag2 = 11
Escala2=1 
insertar_grabacion(autor, Mag1, Escala1, Mag2, Escala2)

# Cierra la conexión con la base de datos
###conexion.close()


cursor = conexion.cursor()

# Ejecuta una consulta SQL para seleccionar todos los registros de la tabla "grabaciones"
cursor.execute("SELECT * FROM grabaciones")

# Recupera todos los registros (filas) de la consulta
registros = cursor.fetchall()

# Imprime
for registro in registros:
    print(registro)
    
    
cursor.execute("DELETE FROM grabaciones")

# Confirma los cambios en la base de datos
conexion.commit() 

# Cierra la base de datos
conexion.close()
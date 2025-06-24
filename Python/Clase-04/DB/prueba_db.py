# Importamos Psycopg2 es una librería de Python que sirve como un adaptador para conectarse y trabajar con bases de datos PostgreSQL
import psycopg2
import os # Importamos el módulo os para acceder a las variables de entorno
from dotenv import load_dotenv # Importamos load_dotenv para cargar las variables de entorno desde el archivo .env

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# Conectamos a la base de datos
conexion = psycopg2.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)
    
print(conexion)

#Creamos un cursor para ejecutar consultas SQL
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona' # Consulta SQL para seleccionar todos los registros de la tabla persona
cursor.execute(sentencia) # Ejecutamos la consulta
resultado = cursor.fetchall() # Obtenemos todos los resultados de la consulta
print(resultado)

cursor.close() # Cerramos el cursor
conexion.close() # Cerramos la conexión a la base de datos

# Verificamos que las variables de entorno se cargaron correctamente
# print("=== Información de conexión ===")
# print(f"Host: {os.getenv('DB_HOST')}")
# print(f"Puerto: {os.getenv('DB_PORT')}")
# print(f"Base de datos: {os.getenv('DB_NAME')}")
# print(f"Usuario: {os.getenv('DB_USER')}")
# print("==============================")

# # Intentamos conectar a la base de datos con manejo de errores
# try:
#     conexion = psycopg2.connect(
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT"),
#         database=os.getenv("DB_NAME")
#     )
    
#     print("¡Conexión exitosa a PostgreSQL!")
    
#     # Verificamos que la conexión funciona ejecutando una consulta simple
#     cursor = conexion.cursor()
#     cursor.execute("SELECT version();")
#     version_db = cursor.fetchone()
#     print(f"Versión del servidor: {version_db[0]}")
#     cursor.close()
    
# except Exception as e:
#     print(f"Error de conexión detallado: {e}")
    
# finally:
#     # Cerramos la conexión si está abierta
#     if 'conexion' in locals() and conexion and not conexion.closed:
#         conexion.close()
#         print("Conexión a PostgreSQL cerrada.")




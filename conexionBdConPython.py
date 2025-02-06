import mysql.connector
import json

with open("datosbd.json","r") as archivo:
    config = json.load(archivo)

#ahora los datos de la conexion se leen de el archivo json
connection = mysql.connector.connect(
    user=config['user'],
    password=config['password'],
    host=config['host'],
    database=config['database']
)





#Datos de conexion:
# connection = mysql.connector.connect(
#     user='root',
#     password='Asir1234',
#     host='172.17.0.2',
#     database='coches'
# )

#Creo el objeto que gestionara la llamada
#y el retorno de los datos en Python, cursor.

cursor = connection.cursor()
cursor.execute("select * from coches")

#lo paso a un diccionario para leerlo con un bucle

res = cursor.fetchall()
for coche in res:
    print(coche)


cursor.close()
connection.close()
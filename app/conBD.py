import mysql.connector 
from datetime import date
from datetime import datetime

def conexion_bd():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "formulario",
        port=3306
        )

    if conexion:
        print("CONEXION EXITOSA")

    else:
        print("Error al conectarse con MySql: ")

    return conexion


conexion_bd()
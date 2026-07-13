import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

def cargar_datos():
    try:
        conexion_db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        consulta_sql = "SELECT * FROM ventas_mall_2026;"
        df = pd.read_sql(consulta_sql, conexion_db)
        return df

    except Exception as error:
        print(f"Hubo error al conectar: {error}")
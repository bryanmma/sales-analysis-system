import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
carpeta_reportes = os.path.join(base_dir, "archivos_exportados")

if not os.path.exists(carpeta_reportes):
    os.makedirs(carpeta_reportes)

ruta_01 = os.path.join(carpeta_reportes, "ingresos_sede.csv")
ruta_02 = os.path.join(carpeta_reportes, "top_productos.csv")
ruta_03 = os.path.join(carpeta_reportes, "ventas_tamanio.csv")
ruta_04 = os.path.join(carpeta_reportes, "metodo_pago_distribucion.csv")
ruta_05 = os.path.join(carpeta_reportes, "tipo_venta_distribucion.csv")

def guardar_reportes(ingresos_sede, rank, ventas_tama, ingresos_met, tipoventa):
    """Guarda los resultados del análisis en archivos CSV."""
    ingresos_sede.index.name = "sede"
    ingresos_sede.reset_index().to_csv(ruta_01, index=False)
    
    rank.index.name = "producto"
    rank.reset_index().to_csv(ruta_02, index=False)

    ventas_tama.to_csv(ruta_03)
    ingresos_met.to_csv(ruta_04)
    tipoventa.to_csv(ruta_05)
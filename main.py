from conexion import cargar_datos
from analisis import *
from graficos import *
from reportes import guardar_reportes
from utils import * 

def main():
    df = cargar_datos()
    if df is None: return 

    total_ingresos, total_unidades = indicadores(df)
    ingresos_sede = ingresos_por_sede(df)
    rank = ranking(df)
    ventas_tama = ventas_tamanio(df)
    ingresos_met = ingresos_metodo(df)
    tipoventa = tipos_de_venta(df)

    imprimir_indicadores(total_ingresos, total_unidades)
    imprimir_ventas_por_sede(ingresos_sede)
    imprimir_top_productos(rank)

    grafico_sede(ingresos_sede)
    grafico_top_productos(rank)
    grafico_ventas_tamanio(ventas_tama)
    grafico_metodos_pago(ingresos_met)
    grafico_tipo_venta(tipoventa)
    
    guardar_reportes(ingresos_sede, rank, ventas_tama, ingresos_met, tipoventa)

if __name__ == "__main__":
    main()
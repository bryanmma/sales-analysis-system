def imprimir_indicadores(total_ingresos, total_unidades):
    print("\n----- INDICADORES -----")
    print(f"Total ingresos: S/{total_ingresos:,.2f}")
    print(f"Total unidades: {total_unidades}")

def imprimir_ventas_por_sede(ingresos_sede):
    print("\n----- INGRESOS POR SEDE -----")
    for sede, ingreso in ingresos_sede.items():
        print(f"{sede}: S/{ingreso:,.2f}")

def imprimir_top_productos(rank):
    print("\n----- 3 PRODUCTOS MÁS VENDIDOS -----")
    for i, (producto, cantidad) in enumerate(rank.items(), 1):
        print(f"{i}. {producto}: {cantidad}")
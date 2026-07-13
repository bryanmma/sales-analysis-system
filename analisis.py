
# 1. Indicadores Generales:
def indicadores(df):
    df["ingreso"] = df["precio"] * df["cantidad"]
    total_ingresos = df["ingreso"].sum()
    total_unidades = df["cantidad"].sum()

    return total_ingresos, total_unidades

# 2. Ingresos por sede:
def ingresos_por_sede(df):
    df["ingreso"] = df["precio"] * df["cantidad"]
    ingresos_sede = df.groupby("sede")["ingreso"].sum().sort_values(ascending=True)
    return ingresos_sede

# 3. Productos más vendidos
def ranking(df):
    ranking = df.groupby("producto")["cantidad"].sum().nlargest(3)
    return ranking

# 4. Ventas por tamaño
def ventas_tamanio(df):
    ventas_tam = df.groupby("tamanio")["cantidad"].sum()
    return ventas_tam

5. # Distribución por método de pago (Ingreso en soles):
def ingresos_metodo(df):
    ingresos_met = df.groupby("metodo_pago")["precio"].sum()
    return ingresos_met

6. #Distribución por tipo de venta (cantidad)
def tipos_de_venta(df):
    tipoventa = df.groupby("tipo_venta")["cantidad"].sum()
    return tipoventa
import os
import matplotlib.pyplot as plt

# Define la ruta base donde está este archivo (graficos.py)
base_dir = os.path.dirname(os.path.abspath(__file__))
carpeta_graficos = os.path.join(base_dir, "graficos_estadisticos")

# Crear la carpeta automáticamente si no existe
if not os.path.exists(carpeta_graficos):
    os.makedirs(carpeta_graficos)

# Definir las rutas relativas
ruta_img01 = os.path.join(carpeta_graficos, "ingresos_sede.png")
ruta_img02 = os.path.join(carpeta_graficos, "top_productos.png")
ruta_img03 = os.path.join(carpeta_graficos, "ventas_tamanio.png")
ruta_img04 = os.path.join(carpeta_graficos, "distribucion_metodos.png")
ruta_img05 = os.path.join(carpeta_graficos, "distribucion_tipo_venta.png")

# --- FUNCIONES DE GRÁFICOS ---

def grafico_sede(ingresos_sede):
    plt.figure(figsize=(8,5))
    ingresos_sede.index = [str(i).title() for i in ingresos_sede.index]
    ax = ingresos_sede.plot(kind="bar", color="#4C72B0", edgecolor="black") 
    plt.bar_label(ax.containers[0], fmt='S/%1.2f', padding=3, fontsize=7)
    plt.title("INGRESOS POR SEDE", fontsize=18, fontweight="bold")
    plt.xlabel("SEDE")
    plt.ylabel("INGRESOS (S/)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(ruta_img01)
    plt.close()

def grafico_top_productos(productos):
    plt.figure(figsize=(8,5))
    productos.index = [str(i).title() for i in productos.index]
    ax = productos.plot(kind="barh", color="#3DAE61", edgecolor="black") 
    plt.bar_label(ax.containers[0], padding=3)
    plt.title("TOP 3 PRODUCTOS MÁS VENDIDOS", fontsize=18, fontweight="bold")
    plt.xlabel("CANTIDAD")
    plt.ylabel("PRODUCTOS")
    plt.tight_layout()
    plt.savefig(ruta_img02)
    plt.close()

def grafico_ventas_tamanio(ventas_ta):
    plt.figure(figsize=(8,5))
    ventas_ta.plot(kind="line", color="#D8A226", linewidth=3, marker="o", markersize=8) 
    for i, v in enumerate(ventas_ta):
        plt.text(i, v + 0.2, str(v), ha="center", fontweight="bold")
    plt.title("VENTAS POR TAMAÑO", fontsize=18)
    plt.xlabel("TAMAÑO")
    plt.ylabel("CANTIDAD")
    plt.tight_layout()
    plt.savefig(ruta_img03)
    plt.close()

def grafico_metodos_pago(metodos_pag):
    plt.figure(figsize=(8,5))
    ax = metodos_pag.plot(kind="barh", color="#D43434", edgecolor="black") 
    plt.bar_label(ax.containers[0], fmt='S/%1.2f', padding=3)
    plt.title("DISTRIBUCIÓN POR MÉTODO DE PAGO (Soles)", fontsize=18, fontweight="bold")
    plt.xlabel("MONTO TOTAL (S/)")
    plt.ylabel("MÉTODO DE PAGO")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(ruta_img04) 
    plt.close()

def grafico_tipo_venta(tipo_v):
    plt.figure(figsize=(8,5))
    ax = tipo_v.plot(kind="bar", color="#F3F30C", edgecolor="black") 
    plt.bar_label(ax.containers[0], padding=3, fontsize=8)
    plt.title("DISTRIBUCIÓN POR TIPO DE VENTA (CANTIDAD)", fontsize=18, fontweight="bold")
    plt.xlabel("TIPO DE VENTA", fontsize=12)
    plt.ylabel("CANTIDAD DE VENTAS", fontsize=12)
    plt.xticks(rotation=0) 
    plt.tight_layout()
    plt.savefig(ruta_img05) 
    plt.close()
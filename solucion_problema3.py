def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Módulo para determinar la cantidad exacta a pedir.
    Lógica: Si el stock actual es menor al mínimo, pide la diferencia.
    De lo contrario, pide cero.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def ejecutar_auditoria():
    # Matriz: [Código, Nombre, Stock Actual, Stock Mínimo]
    inventario = [
        [101, "Router MikroTik RB5009", 5, 10],
        [102, "SFP+ Module 10G", 15, 12],
        [103, "Patch Cord Fibra 1m", 8, 20],
        [104, "ONU Huawei HG8546M", 3, 15],
        [105, "Caja Nap 16 Puertos", 12, 10]
    ]

    print(f"{'ARTÍCULO':<25} | {'CANTIDAD A PEDIR'}")
    print("-" * 45)

    for articulo in inventario:
        nombre = articulo[1]
        actual = articulo[2]
        minimo = articulo[3]
        
        # Llamada al módulo/función solicitado
        pedido = calcular_cantidad_pedir(actual, minimo)
        
        print(f"{nombre:<25} | {pedido}")

if __name__ == "__main__":
    ejecutar_auditoria()
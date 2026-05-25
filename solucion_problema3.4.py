def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Lógica de negocio:
    - Si actual < mínimo: pide la diferencia.
    - Si actual >= mínimo: pide cero.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

def ejecutar_auditoria_isp():
    # Matriz con datos fijos: [Código, Nombre, Stock Mínimo]
    # El Stock Actual (posición 2) empezará en 0 y lo llenaremos por teclado
    datos_base = [
        ["HUA-01", "ONU Huawei HG8546M", 10],
        ["ZTE-02", "Tarjeta GPON 16P", 2],
        ["SFP-03", "Modulo SFP OLT C++", 15],
        ["FIB-04", "Bobina Fibra 1km", 5],
        ["SPL-05", "Splitter PLC 1x8", 20]
    ]
    
    inventario = []

    print("--- INGRESO DE AUDITORÍA DIARIA ---")
    
    # Llenamos la matriz con el stock que tú ingreses
    for item in datos_base:
        codigo, nombre, minimo = item
        print(f"\nArtículo: {nombre} (Mínimo requerido: {minimo})")
        
        # Aquí es donde interactúas con el CMD
        actual = int(input(f"Ingrese el Stock Actual para {nombre}: "))
        
        # Guardamos todo en la matriz final: [Código, Nombre, Actual, Mínimo]
        inventario.append([codigo, nombre, actual, minimo])

    # Salida de resultados
    print("\n" + "="*55)
    print(f"{'ARTÍCULO':<25} | {'STOCK':<7} | {'PEDIR'}")
    print("-" * 55)

    for fila in inventario:
        nombre_art = fila[1]
        stk_act = fila[2]
        stk_min = fila[3]
        
        pedido = calcular_cantidad_pedir(stk_act, stk_min)
        
        print(f"{nombre_art:<25} | {stk_act:<7} | {pedido} uds")
    print("="*55)

if __name__ == "__main__":
    ejecutar_auditoria_isp()
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Módulo para determinar la cantidad exacta a pedir.
    Si el stock actual es menor al mínimo, devuelve la diferencia.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

def ejecutar_auditoria_isp():
    # Matriz vacía que llenaremos dinámicamente
    inventario = []
    
    print("--- SISTEMA DE AUDITORÍA DE INVENTARIO GPON ---")
    
    # El requisito pide al menos 5 artículos
    for i in range(5):
        print(f"\nIngreso de datos - Artículo {i+1}:")
        codigo = input("Código de parte: ")
        nombre = input("Descripción (ej. ONU, OLT, SFP): ")
        actual = int(input(f"Stock actual de {nombre}: "))
        minimo = int(input(f"Stock mínimo de seguridad: "))
        
        # Guardamos la fila en nuestra matriz
        inventario.append([codigo, nombre, actual, minimo])

    # Salida de resultados
    print("\n" + "="*50)
    print(f"{'DESCRIPCIÓN TÉCNICA':<30} | {'PEDIDO MÍNIMO'}")
    print("-" * 50)

    for fila in inventario:
        # Extraemos datos de la matriz para procesarlos
        nombre_art = fila[1]
        stk_actual = fila[2]
        stk_minimo = fila[3]
        
        # Llamada a la función de lógica de negocio
        cantidad_a_pedir = calcular_cantidad_pedir(stk_actual, stk_minimo)
        
        print(f"{nombre_art:<30} | {cantidad_a_pedir} unidades")
    print("="*50)

if __name__ == "__main__":
    ejecutar_auditoria_isp()
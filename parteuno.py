def ejecutar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    porcentaje_inicial = 0.25
    ahorro_actual = 0.0
    retorno_anual_ahorros = 0.04

    costo_total = float(input("Ingrese el costo de la casa: "))
    salario_anual = float(input("Ingrese su salario anual: "))
    porcentaje_ahorro = float(input("Ingrese el porcentaje de ahorro mensual: "))

    inicial_casa = costo_total * porcentaje_inicial

    total_meses = 0
    while ahorro_actual <= inicial_casa:
        retorno_inversion = ahorro_actual * retorno_anual_ahorros / 12
        ahorro_mensual = salario_anual / 12 * porcentaje_ahorro

        ahorro_actual += retorno_inversion + ahorro_mensual
        total_meses += 1

    print("Numero de meses: " + str(total_meses))
    # FIN
    return

# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    ejecutar()

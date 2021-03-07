def ejecutar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    porcentaje_inicial = 0.25
    ahorro_actual = 0.0
    retorno_anual_ahorros = 0.04

    costo_total = float(input("Ingrese el costo de la casa: "))
    salario_anual = float(input("Ingrese su salario anual: "))
    porcentaje_ahorro = float(input("Ingrese el porcentaje de ahorro mensual: "))
    porcentaje_aumento = float(input("Ingrese el porcentaje de aumento semestral: "))

    inicial_casa = costo_total * porcentaje_inicial

    mes_actual = 0
    while ahorro_actual <= inicial_casa:
        retorno_inversion = ahorro_actual * retorno_anual_ahorros / 12
        ahorro_mensual = salario_anual / 12 * porcentaje_ahorro

        ahorro_actual += retorno_inversion + ahorro_mensual
        mes_actual += 1

        if mes_actual % 6 == 0:
            salario_anual += salario_anual * porcentaje_aumento

    print("Numero de meses: " + str(mes_actual))
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    ejecutar()

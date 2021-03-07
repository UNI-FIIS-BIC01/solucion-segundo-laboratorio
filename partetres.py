def ejecutar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    porcentaje_inicial = 0.25
    retorno_anual_ahorros = 0.04
    costo_total = 1000000
    porcentaje_aumento = 0.07

    salario_anual_inicial = float(input("Ingrese su salario anual: "))
    diferencia = 100

    tamanio_intervalo = 10000
    inicio_intervalo = 0
    fin_intervalo = tamanio_intervalo

    inicial_casa = costo_total * porcentaje_inicial
    me_alcanza = False
    porcentaje_ahorro = 0.0

    while inicio_intervalo < fin_intervalo:

        valor_actual = inicio_intervalo + (fin_intervalo - inicio_intervalo) / 2
        porcentaje_ahorro = valor_actual / tamanio_intervalo

        ahorro_actual = 0.0
        salario_anual = salario_anual_inicial

        for mes_actual in range(1, 37, 1):
            retorno_inversion = ahorro_actual * retorno_anual_ahorros / 12
            ahorro_mensual = salario_anual / 12 * porcentaje_ahorro

            ahorro_actual += retorno_inversion + ahorro_mensual
            if mes_actual % 6 == 0:
                salario_anual += salario_anual * porcentaje_aumento

        if abs(ahorro_actual - inicial_casa) < diferencia:
            me_alcanza = True
            break

        if ahorro_actual < inicial_casa:
            inicio_intervalo = valor_actual
        else:
            fin_intervalo = valor_actual

    if me_alcanza:
        print("Porcentaje de ahorro: " + str(porcentaje_ahorro))
    else:
        print("No es posible pagar la inicial en 36 meses")
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    ejecutar()

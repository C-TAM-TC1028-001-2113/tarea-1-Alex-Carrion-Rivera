def main():
    # escribe tu código abajo de esta línea
    saldo = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input('Dame el valor de ingresos: '))
    egresos = float(input('Dame el valor de egresos: '))
    no_cheques = int(input('Dame el número de cheques expedidos: '))

    saldo_final = (saldo + (ingresos - egresos - no_cheques) * .925)

    print('El saldo final de la cuenta es:', saldo_final)


if __name__ == '__main__':
    main()

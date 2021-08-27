def main():
    # escribe tu código abajo de esta línea
    no_mensajes = int(input('Dame el número de mensajes: '))
    no_megas = float(input('Dame el número de megas: '))
    no_min = int(input('Dame el número de minutos: '))

    costo_mensual = (no_mensajes + no_megas + no_min) * 0.8

    print('El costo mensual es:', costo_mensual)

if __name__ == '__main__':
    main()

def main():
    # escribe tu código abajo de esta línea
    x1 = int(input('Dame el valor de x1: '))
    y1 = int(input('Dame el valor de y1: '))
    x2 = int(input('Dame el valor de x2: '))
    y2 = int(input('Dame el valor de y2: '))

    m = (y2-y1) / (x2-x1)

    print('El valor de la pendiente es igual a:', m)

if __name__ == '__main__':
    main()

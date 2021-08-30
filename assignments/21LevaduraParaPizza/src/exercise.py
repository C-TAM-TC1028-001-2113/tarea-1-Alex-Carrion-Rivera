def main():
    # escribe tu código abajo de esta línea
    harina = float(input('Dame la cantidad de harina em gramos: '))

    gramos_lev = (harina * 50) / 1000

    print('Necesitas', gramos_lev, 'gramos de levadura')


if __name__ == '__main__':
    main()

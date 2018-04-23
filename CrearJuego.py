def CREAR_SOPA(x,y):
    """

    :param x:
    :param y:
    :return:
    """
    contador = 0
    matriz = []
    while (contador < x):
        contador2 = 0
        matriz.append([str(input("Ingrese una letra: "))])
        while(contador2 < y - 1):
            matriz[contador].append([str(input("Ingrese una letra: "))])
            contador2 = contador2 + 1
        contador = contador + 1
    return matriz

def CREAR_LISTA(num):
    """

    :param num:
    :return:
    """
    contador = 0
    lista =[]
    while (contador < num):
        lista.append(str(input("Ingrese una palabra: ")))
        contador = contador + 1
    return lista
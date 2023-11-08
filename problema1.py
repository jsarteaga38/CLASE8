def sumar_5_enteros():
    #Definición de variables
    lista = []
    contadorWhile= 0
    tamano = 5
    suma = 0

    #ingresar los números
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese número " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

        #Sumamos los números:
    contadorWhile = 0
    while contadorWhile < tamano:
            suma += lista[contadorWhile]
            contadorWhile += 1

    for numero in lista:
        print(numero,end=', ')

    print("\nLa suma de todos sus elementos es:")
    print(suma)

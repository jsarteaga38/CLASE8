''' Hasta ahora
hemos trabajado con variable
que permiten almacenar
un único valor
'''


edad = 12

altura = 1.79

nombre = "juan"

estado = True

'''
En python podemos
usar una variable
que almacene una 
colección de datos
y luego accederla
usando un subíndice
'''

# Lista de enteros
lista1 = [10, 5, 3, 9]

#lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]

#lista de string
lista3 = ["Lunes", "Martes", "Miércoles"]

'''
Lista de elementos 
de distinto tipo
'''

lista4 = ["juan", 45, 1.92, False]



if __name__ == '__main__':

    '''
    Cantidad de elementos de cada lista:
    '''

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print(lista1)



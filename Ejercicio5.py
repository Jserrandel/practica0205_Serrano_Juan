
def Cuadrado(lista):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    lista: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in lista:
        list.append(i**2)
    return list

print(Cuadrado([1, 2, 3, 4, 5]))
print(Cuadrado([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
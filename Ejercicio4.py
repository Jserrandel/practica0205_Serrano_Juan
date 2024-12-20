#Escribir una función que reciba una 
#muestra de números en una lista y devuelva su media.
def muestra(media):
    """Función que calcula la media de una muestra de números.
    Parámetros
    media: Es una lista de números
    Devuelve la media de los números en sample. 
    """
    return sum(media)/len(media)

print(muestra([1, 2, 3, 4, 5]))
print(muestra([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
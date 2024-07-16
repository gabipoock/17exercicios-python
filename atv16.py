#Filtrar números negativos de uma lista:
#Use `filter()` para encontrar todos os números negativos em uma lista.

lista = [24, -5, 8, 2, -15]
numeros=list(filter(lambda x: x<0, lista))
print('Lista de números: ', lista)

print('Os números negativos da lista são: ', numeros)


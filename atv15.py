#Enumerar os elementos de uma lista com um índice inicial diferente:
#Use `enumerate()` para listar os elementos de uma lista começando de um índice diferente de zero.

lista = [24, 5, 8, 2, 15]

for indice, valor in enumerate(lista, start=1):
    print(indice, valor)


#2) Use `sorted()` para ordenar uma lista de números em ordem crescente e decrescente.

print('\n///LISTA EMBARALHADA///')
print('[8, 9, 24, 3, 16, 1, 18, 49]\n')

numeros = [8, 9, 24, 3, 16, 1, 18, 49]
ordenados = sorted(numeros)

print('///LISTA EM ORDEM CRESCENTE///')
print(ordenados, '\n')

print('///LISTA EM ORDEM DECRESCENTE///')
decrescente = sorted(numeros, reverse=True)
print(decrescente)

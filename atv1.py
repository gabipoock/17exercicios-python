# Calcular potências usando `pow()`

print('Oioii, usuário! Vamos calcular potências?  :)')
base = int(input('Digite o número Base que deseja realizar a operação de potenciação: '))
expoente = int(input('Digite um número para ser o seu expoente: '))

resultado = pow(base, expoente)

print('O resultado da Base {} com o expoente {} é igual a: "{}".'.format(base, expoente, resultado))
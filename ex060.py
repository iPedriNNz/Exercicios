from math import factorial

valor = int(input('Digite um número para calcular seu fatorial: '))
fat = factorial(valor)
print('O resultado de {}! é {}'.format(valor, fat))

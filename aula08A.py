from math import ceil, sqrt

number = int(input('Digite um numero '))
squareroot = sqrt(number)
print('A raiz de {} é {}.'.format(number, ceil(squareroot)))
# ceil arrendonda pra cima

# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
number1 = int(input('Digite um número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))
max = number1
min = number1
if max < number2:
    max = number2
if max < number3:
    max = number3
if min > number2:
    min = number2
if min > number3:
    min = number3
print('O maior numero entre os três que você digitou é {} e o menor é {}'.format(max, min))

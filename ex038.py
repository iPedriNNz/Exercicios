# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
if number1 > number2:
    print('O primeiro valor é maior.')
elif number2 > number1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')

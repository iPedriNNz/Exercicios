# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
number = int(input('Digite um numero inteiro: '))
conversion = int(input('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL \nDigite sua escolha: '''))
if conversion == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(number, bin(number)[2:]))
elif conversion == 2:
    print('O numero {} convertido para OCTAL é igual a {}.'.format(number, oct(number)[2:]))
elif conversion == 3:
    print('O numero {} convertido para HEXADECIMAL é igual a {}.'.format(number, hex(number)[2:]))
elif conversion > 3:
    print('Escolha sua opção entre 1 e 3 !!!')

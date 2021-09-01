# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
machine = randint(0, 2)
player = int(input('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual a sua jogada ? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-' * 20)
print('O computador escolheu {}.'.format(itens[machine]))
print('O jogador escholheu {}.'.format(itens[player]))
print('=-' * 20)
if machine == 0:  # Pedra
    if player == 1:
        print('Você GANHOU!')
    elif player == 2:
        print('Você PERDEU!')
    else:
        print('EMPATE')
elif machine == 1:  # Papel
    if player == 2:
        print('Você GANHOU!')
    elif player == 0:
        print('Você PERDEU!')
    else:
        print('EMPATE')
elif machine == 2:  # Tesoura
    if player == 0:
        print('Você GANHOU!')
    elif player == 1:
        print('Você PERDEU!')
    else:
        print('EMPATE')

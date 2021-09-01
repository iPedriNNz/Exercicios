from random import randint
from time import sleep

tentativas = 0
print('=-' * 20)
print('Vou pensar em uma número de 0 a 10 e você tenta adivinhar...')
print('=-' * 20)
number = randint(0, 10)
sleep(1)
numberuser = int(input('Em qual numero eu pensei ? '))
while numberuser > 10:
    print('EU DISSE UM NÚMERO DE 0 A 10 !!')
    numberuser = int(input('Em qual numero eu pensei ? '))
print('PROCESSANDO....')
sleep(1)
tentativas += 1
while numberuser != number:
    print('ERROU !!! Vou te dar mais uma chance !')
    sleep(1)
    numberuser = int(input('Em qual numero eu pensei ? '))
    while numberuser > 10:
        print('EU DISSE UM NÚMERO DE 0 A 10 !!')
    tentativas += 1
print('PARABÉNS você acertou eu pensei no numero {}!'.format(number))
if tentativas == 1:
    print('Você só precisou de uma tentativa ! Quanta sorte !')
else:
    print('Voce precisou de {} tentativas para acertar.'.format(tentativas))

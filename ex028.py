from random import randint
from time import sleep

print('=-' * 20)
print('Vou pensar em uma número de 0 a 5...')
print('=-' * 20)
number = randint(0, 5)
sleep(3)
numberuser = int(input('Em qual numero eu pensei ? '))
print('PROCESSANDO....')
sleep(3)
if numberuser == number:
    print('PAARABÉNS você acertou eu pensei no numero {}!'.format(number))

elif numberuser > 5:
    print('Eu disse um número de 0 a 5 !!!')

else:
    print('GANHEI !!! eu pensei no numero {} e não no {} !'.format(number, numberuser))

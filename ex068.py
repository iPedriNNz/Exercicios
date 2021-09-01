from random import randint

cont = 0
victory = 0
print('==' * 20)
print('      VAMOS JOGAR PAR OU IMPAR')
print('==' * 20)
while True:
    player = int(input('Digite um número: '))
    machine = randint(1, 10)
    op = str(input('Par ou ímpar [P/I] ?'.strip().upper()))
    total = player + machine
    cont += 1
    if op in 'Pp':
        if (total % 2) == 0:
            print('=-' * 20)
            print(f'Você jogou {player} e o computador jogou {machine}. Total de {total}, deu PAR!!')
            print('=-' * 20)
            print('Você ganhou vamos jogar de novo...')
            victory += 1
        else:
            print('=-' * 20)
            print(f'Você jogou {player} e o computador jogou {machine}. Total de {total}, deu IMPAR!!')
            print('=-' * 20)
            print(f'GAME OVER! Você venceu {victory} vezes.')
            break
    if op in 'Ii':
        if (total % 2) != 0:
            print('==' * 20)
            print(f'Você jogou {player} e o computador jogou {machine}. Total de {total}, deu IMPAR!!')
            print('==' * 20)
            print('Você ganhou vamos jogar de novo...')
            victory += 1
        else:
            print('==' * 20)
            print(f'Você jogou {player} e o computador jogou {machine}. Total de {total}, deu PAR!!')
            print('==' * 20)
            print(f'GAME OVER! Você venceu {victory} vezes.')
            break
